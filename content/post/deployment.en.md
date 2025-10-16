---
date: '2021-08-13T00:00:00Z'
title: Deployment evolutions
tags:
- aws
- deployement
- container
- elasticsearch
- slack
- prose
---

## Case 1. "/whatis": a slack command server

Business: When Slack users input a command like "/whatis GDPR", search on wiki pages and respond in 3 seconds what GDPR is.

## Generation 1. servers on machines
![](/images/deployment/g1.png)

ElasticSearch: to respond in less than a second

Ngrok: to pierce the private network

### Gen 2. containerized
![](/images/deployment/g2.png)

Docker: to make deployments reliable

### Gen 3. Cloud (AWS EC2 + Amazon ElasticSearch Service)
![](/images/deployment/g3.png)

To get rid of on-premise server room, which occasionally suffers from power outages.

EC2: a drop-in replacement of bare metals

AWS ElasticSearch Service: a drop-in replacement of Elastic Search servers

### Gen 4. Serverless (AWS API Gateway + AWS Lambda + EventBridge)
![](/images/deployment/g4.png)

To get rid of EC2, which is occasionally stopped and need to manually restart and change slack configurations

API Gateway: ingress gateway; authentication

Lambda: pay-as-you-go; fast cold-starts

EventBridge: cron jobs

## Case 2. "GODIVA": Go Dependency Visualizer

Business: A static site, internal network access only

### Generation 1. Nginx + Docker + static files
![](/images/deployment/g1-2.png)

Nginx: to host a static site.

Docker: to make deployments reliable

### Gen 2. Cloud
![](/images/deployment/g2-2.png)

To get rid of BJO server room, which occasionally suffers from power outages.

Route 53: a DNS to resolve host to EC2's ip

EC2: to migrate from bare metals

### Gen 3. API Gateway + S3
![](/images/deployment/g3-2.png)

To get rid of EC2, which is occasionally stopped and need to manually restart.

Route 53: a DNS to resolve host to API Gateway's execution endpoint

API Gateway: ingress gateway; authentication

S3 files: a drop-in replacement of local files