---
date: '2018-09-06T01:00:00Z'
title: On Performance
tags:
- prose
---

## Why ?
- economic efficiency ( do more and faster with less)
- a major goal in code refactoring/optimization phase ( build first, optimize later )

## Aspects of performance

### Metrics ( monitoring )

- availibility: down times, crash times, GC times
- response time: average, .95 quantile
- throughput: query per second, degree of concurrency
- resource usage: cpu idle, memory used, disk used & io, network io, instance counts

### Profiling analysis ( what costs how much )

request cost distribution over phases:

- browser rendering time
- external network latency
- internal network latency
- business backend execution time
- database execution latency time

resource usage distribution over lines of codes:

- memory allocation & release ( memory leak detection )
- file handle allocation & release ( file handle leaks )

### Dependency analysis ( what depends on what )

- dependency defintion & managements ( package management tools, artifact repos )
- dependency loops detection ( must be DAG to build and run )
- conflicts resolution
- visualization of dependencies

### Benchmarking (comparison of changes)

- set up test group and control group (baseline)
- input & output standarization & quantification
- statistical metric comparation of groups and times

## Common bottlenecks of performance

single points of failure: any "master" node without backup or automatic election mechanism

### Database slow queries

- no index
- vague or wrong usage of index
- too many data rows

### Business logic defects

- unecessary nested loops or recursion
- unecessary synchronized and/or sequential execution flow (n+1 issue)

## How to improve performance

### Code level

- add specific and proper indexes
- use batch execution
- use connection pools (use random sleep)
- guard read with cache middlewares
- throttle write with message queues
- use statics and consts when possible
- proactively clean up costly objects
- less synchronized logs

### Arch level

- parallelization and asynchronization when possible
- scale up and down service instances with flow & load changes
- do data partitions
- read and write flow separation
- hot and cold data separation
- build up performance environments for testing

## Build up performance environments for testing
- real requests recording & playback
- containment and provision
- tests management for benchmarking

## Tools

- metrics collection: filebeat, fluentd for logs; prometheus for key-value metrics
- metrics aggregation: logstash, fluentd
- frontend solutions: kibana, grafana
- visualization diagrams: comparison: histograms; analysis: flamegraph; relationship: force-directed graphs, circos
- http request load & stress test: gatlin, ab
- profiling: pprof for golang

## Design patterns & mindsets

- epoll in a loop ( servers )
- async & await ( avoiding callback hell )
- divide & conquer ( map then reduce )
- trading time for space ( like file sorts ), or space for time ( any kinds of indexes )
- event based ( fire and forget )
- master-minions
- separate list from detail
- in distributed systems: pick two among consistency, availability and partition-tolerance