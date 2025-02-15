# Kubernetes Mini Project

This project demonstrates how to deploy a **MongoDB** database with **Mongo Express** in a Kubernetes cluster using **Minikube**. The setup includes ConfigMaps, Secrets, Deployments, and Services to ensure secure and scalable deployment. Additionally, this project helps you understand Kubernetes concepts like managing environment variables securely, exposing services, and deploying scalable applications.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Ubuntu Users**:
  - **Minikube**
  - **Kubectl**
  - **Docker** (optional, as Minikube can use its built-in container runtime)

- **Windows Users**:
  - **WSL (Windows Subsystem for Linux)**
  - **Docker Desktop** (with Kubernetes enabled)
  - **Minikube**
  - **Kubectl**

## Project Structure

```
├── deployment.yaml           # MongoDB Deployment & Service
├── mongo-configmap.yaml      # ConfigMap for MongoDB
├── mongo-express.yaml        # Mongo Express Deployment & Service
├── secrets.yaml              # Secrets for MongoDB credentials
```

## What You Can Do With This Project

- Deploy a MongoDB instance in a Kubernetes cluster.
- Secure database credentials using Kubernetes Secrets.
- Store and manage environment configurations using ConfigMaps.
- Deploy Mongo Express, a web-based MongoDB admin interface.
- Access Mongo Express to interact with your MongoDB database via a web browser.
- Learn how Kubernetes Services work to expose internal applications.
- Understand the process of running containers efficiently in a Kubernetes cluster.

## Setup and Deployment

### Step 1: Start Minikube

Start Minikube with Docker as the driver:

```sh
minikube start --driver=docker
```

### Step 2: Apply Secrets

Secrets store sensitive information like database credentials. Apply the secret:

```sh
kubectl apply -f secrets.yaml
```

### Step 3: Apply ConfigMap

ConfigMaps are used to store non-sensitive configuration data:

```sh
kubectl apply -f mongo-configmap.yaml
```

### Step 4: Deploy MongoDB

Apply the MongoDB deployment and service:

```sh
kubectl apply -f deployment.yaml
```

Check if the MongoDB pod is running:

```sh
kubectl get pods
```

### Step 5: Deploy Mongo Express

Apply the Mongo Express deployment and service:

```sh
kubectl apply -f mongo-express.yaml
```

### Step 6: Access Mongo Express Dashboard

Since Mongo Express service is exposed as a `LoadBalancer`, you need to access it via Minikube’s service tunnel:

```sh
minikube service mongo-express-service
```

This will open the Mongo Express UI in your browser.

## Verifying the Setup

- Check all running pods:
  ```sh
  kubectl get pods
  ```
- Check all services:
  ```sh
  kubectl get services
  ```
- View logs of MongoDB:
  ```sh
  kubectl logs -l app=mongodb
  ```
- View logs of Mongo Express:
  ```sh
  kubectl logs -l app=mongo-express
  ```

## Cleanup

To delete all resources created in this project:

```sh
kubectl delete -f secrets.yaml
kubectl delete -f mongo-configmap.yaml
kubectl delete -f deployment.yaml
kubectl delete -f mongo-express.yaml
```

Stop Minikube:

```sh
minikube stop
```

## Conclusion

This project provides a simple yet effective setup for deploying a **MongoDB** database along with **Mongo Express** in a Kubernetes cluster. It demonstrates essential concepts such as ConfigMaps, Secrets, Deployments, and Services in Kubernetes.



