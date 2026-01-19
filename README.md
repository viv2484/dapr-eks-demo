# Dapr Pub/Sub Demo on EKS using AWS SNS/SQS

This repository demonstrates **Dapr Pub/Sub** using **AWS SNS and SQS** on an **EKS cluster** (`eks-workshop`). It includes:

- `productservice` — publishes messages to an SNS topic
- `orderservice` — subscribes via Dapr to messages in an SQS queue

> This setup requires an AWS account and proper IAM permissions for SNS and SQS.

---

## Prerequisites

- AWS EKS cluster (`eks-workshop`) with at least 1 worker node
- `kubectl` configured for the cluster
- `eksctl` installed
- `docker` installed
- `helm` installed
- `aws-cli` configured with a user that has permissions for:
  - `eks:*
  - `ecr:*
  - `sns:*`
  - `sqs:*`
  - `iam:PassRole` (if creating roles)
- Dapr CLI installed (optional, for dashboard)
- Docker and ECR access if building container images
---

## Project Structure

dapr-eks-demo/
├── k8s/
│   ├── pubsub.yaml               # Dapr component for AWS SNS/SQS
│   ├── product-deployment.yaml   # Kubernetes Deployment for ProductService
│   ├── order-deployment.yaml     # Kubernetes Deployment for OrderService
│   └── subscription.yaml         # Dapr Subscription linking topic to subscriber
├── src/
│   ├── productservice/           # ProductService source code (publisher)
│   │   ├── app.py
│   │   └── dockerfile
│   └── orderservice/             # OrderService source code (subscriber)
│       ├── app.py
│       └── dockerfile
└── README.md
