# dead-letter-order
The internal order service for dead-letter

## Spec
The order service will be handling all operations related to customer orders. This includes creating orders, interfacing with SMS for confirmation & notifications, and the overall order flow.

**Required Methods**
- Create order
    - Create an order object in the database over gRPC
    - Trigger the rider choice algorithm
- Rider choice algorithm
    - Get the pool of available riders, and choose the best one based on ratings, bike type, etc.
- SMS delivery flow
    - Based on the chosen rider, send SMS notifications to confirm that order pickup can occur
        - If the rider cannot pickup the order, choose the next best rider and confirm with them, and so on
    - Confirm with the rider that pickup has occurred
    - Give the customer updates on their order status
    - Handle SMS images from the rider for order confirmation
- Other miscellaneous functions
    - Refund, dispute, etc.

## Important Cluster Info
- The DB service can be located at `dead-letter-data.dead-letter.svc.cluster.local` within the cluster
- The message bus can be located at `rabbitmq-dead-letter.rabbitmq-dead-letter.svc.cluster.local` within the cluster
- Ensure you are running through Tilt to be able to interface with both services
- These variables will be automatically injected into the container via Kubernetes under these environment variables:
    - DB_SERVICE_URL
    - MQ_URL

## Generating Client Stubs
- You can generate Python client stubs using the Make target: `make proto/gen`
- You will also need to install `protoc-gen-python`
    - Install instructions [here](https://github.com/danielgtaylor/python-betterproto)

## Usage
1. Configure the personal access token under the CR_PAT variable in the GitHub Actions Secrets
2. On push, the workflow will run and 
    - Build the Docker image
    - Publish the Docker image under USERNAME/REPO_NAME:COMMIT_SHA to the GHCR (not Docker hub)
