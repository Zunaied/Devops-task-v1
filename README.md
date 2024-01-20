
# Part: A - Develop & Deploy a REST API

## API Creation using OpenWeather API
This application, implemented in [app.py](./app.py), collects data from the OpenWeather API using an API key and provides responses to the following endpoints:

- `/api/hello`: Returns data from OpenWeather.
- `/api/health`: Health check API endpoint.

The application runs on port 5500.


## Endpoints

- `/api/hello`: Description of this endpoint.
- `/health`: Description of health check endpoint.

## Containerize the application using docker
The application has been containerized using Docker. The Dockerfile used for containerization can be found at [Dockerfile](./Dockerfile). The Dockerfile is based on the `python:3.9-slim` image. It copies all the necessary files into the container and installs the required dependency packages.




## CI/CD Workflow for Container

1. **Dockerfile Creation:**

   - The Dockerfile ([Dockerfile](./Dockerfile)) contains all the necessary instructions to build the application image.

2. **Jenkins Setup:**

   - Jenkins is configured to watch the Git repository for changes.

   - Upon detecting a new commit, Jenkins triggers a pipeline to build the Docker image.

   - The pipeline then pushes the built image to Docker Hub with a specified version.

3. **Docker Compose Deployment:**

   - Docker Compose ([docker-compose.yml](./docker-compose.yml)) is used to define and manage the multi-container Docker application.

   - The deployed application uses the Docker image from Docker Hub with the specified version.

   - Docker Compose ensures a clean and robust deployment by stopping the existing containers, releasing ports, and then starting the new containers.
   


## Kubernetes Deployment using jenkins CI/CD

This CI/CD process automates the deployment of the application to a Kubernetes cluster. The Kubernetes manifests, including deployment, service, and secret files, are organized in the [k8s-manifest](./k8s-manifest) directory.
### Manifest Files

- [Deployment](./k8s-manifest/deployment): Specifies the number of replicas and configurations for the application deployment.
- [Service](./k8s-manifest/service): Defines a NodePort service, exposing the application on port 30005.
- [Secret](./k8s-manifest/secret): Contains sensitive information, such as the OpenWeather API key.

### Jenkins Configuration

The [Jenkinsfile](./Jenkinsfile) is configured to authenticate with the Kubernetes cluster. It references the kubeconfig file as a secret and sets it in the environment.

### Kubernetes Deployment Stage

In the Jenkinsfile, a specific stage is dedicated to Kubernetes deployment. 


