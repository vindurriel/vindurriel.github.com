---
date: '2018-09-06T00:00:00Z'
title: On Dev-Ops
tags:
- prose
- dev-ops
- k8s
---

dev: executable + configuration (dependency, parameters)

integration: some devs + networking

dev-ops: integration + resources + changes

## Networking:  connecting the dots

a phone call metaphor:

- who is it?  ( domain names, Layer 7 in OSI )
- can you hear me?  ( data transfer through Layer 1-4 of OSI )
- do you understand?  ( messaging, Layer 5-7 in OSI)

## How does k8s tackle networking problems

k8s abstracts a networking topology as:

- Cluster: a set of nodes
  - Nodes: machines (bare-metal, virtual)
    - Pods: in-node application units, works on Layer 4
      - Containers: in-pod, one for each process
  - Services: cross-node naming on Layer 7, load-balancing to Pods matched by labels

## Why Pods?

1. one container = one process, end of discussion. ( key contribution to the containerization community )
2. for tightly-coupled containers / processes ( e.g. sharing files ), compose them into an pod / application ( side-car mode )
3. one pod = one ip = one container network

## Why Services?

1. for callers: depend on interface, not implementation:  A->B => A->Interface->B , easy for testing and issue isolation
2. for callees: load-balancing, high-availability
3. loose coupling: caller do not need to know callee's routes.
4. more controllable and efficient than DNS, which is cached and propagated

## How does routing work in k8s?

- same pod: use file (socket) or localhost:port
- across-pod, same node: use service, pod1 -> service2 -> pod2
- across-node, in cluster: also use service, pod1 -> service2 -> node1 -> node2 -> pod2
- cluster -> outside: not controlled by k8s, pod1 -> node1 -> ... -> outside
- cluster <- outside:
  - special services (LoadBalancer/NodePort)
  - Ingress (a Layer 7 proxy mapping domain names to in-cluster services)


## Resources: all we got is all we need

kinds of resources:
- allocated (exclusive):
  - names (e.g. service name)
  - ip
  - port
- sharing (non-exclusive, limited in sum):
  - cpu
  - memory
  - disk space
  - IO (disk, network)

## How does k8s tackle resource problems?

- allocated:
  - names: using namespaces to contain and distinguish names
  - ip: every service and pod have an ip, so no conflict on node ip (if do not use nodePort)
  - port: support the same ports on different pods /  services
- sharing:
  - cpu / memory: user specifies required and limits on container level, k8s reduces usage by not creating / killing pods
  - disk space: k8s kills pods on low disk space ( even kills itself )
  - IO: not managed

## Changes: an orchestration of operations

typical system operations:

- roll-out ( new++, old-- )
- roll-back ( asap )
- health-check based high-availability
- execute in sequential steps
- autoscale for traffic changes

## How does k8s orchestrate incremental changes?

### roll-out and roll-back

k8s uses *Deployments* for roll-out and roll-backs

- *Deployments*: defines wanted state and how to get there
  - *ReplicaSet Old*: a set of interchangable old pods
    - old Pods-- in a roll-out
  - *ReplicaSet New*: a set of interchangable new pods
    - new Pods++ in a roll-out

### Health-check based high-availability

k8s uses two kinds of Probes on two kinds of objects:

|probe    |on object|checks if ...                                    |what to do on repeated success                |what to do on repeated failure                 |
|---------|---------|-------------------------------------------------|----------------------------------------------|-----------------------------------------------|
|liveness |container|the process within is up                         |                                              |container is killed and restarted              |
|readiness|container|the process within is ready to accept traffic    |                                              |                                               |
|readiness|pod      |all containers within are ready to accept traffic|pod is attached to service with matching label|pod is removed from service with matching label|

### Execute in sequential steps

k8s uses Init Containers to execute sequential steps for a pod.

each init container starts in sequence, runs to exit, then next. 

for example, init containers can be used to wait for dependencies.

### Autoscaling for traffic changes

k8s provides [horizontal pod autoscale](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale)

moreover, *operator pattern* is k8s' key contribution to dev-ops community, by defining 3rd-party resource and writing operators on it, users could turn declarative descriptions of system states to imperative execution plans, translating what to how:

```yaml
wanted_state:
	redis-slave:
		version: 3.2
		replicas: 3
		wait-for-service: ["redis-master"]
```

```python
def operator(wanted_state):
	while(True):
		if current_state() == wanted_state:
			break
		do_operate()
```

