
# Part: A - Develop & Deploy a REST API

 The Final Architecture for CI/CD Workflow: 
 ![workflow](https://github.com/Zunaied/Devops-task-v1/blob/main/images/ci-cd%20workflow%20diagram.png)

 
## API Creation using OpenWeather API
This application, implemented in [app.py](./app.py), collects data from the OpenWeather API using an API key and provides responses to the following endpoints:
 
## Endpoints
   - `/api/hello`: Returns data from OpenWeather.
   ![api/hello](https://github.com/Zunaied/Devops-task-v1/blob/main/images/Screenshot%202024-01-21%20171510.png)
   - `/api/health`: Health check API endpoint.
   ![api/health](https://github.com/Zunaied/Devops-task-v1/blob/main/images/api%20health.png)

The application runs on port 5500.

## Containerize the application using docker
The application has been containerized using Docker. The Dockerfile used for containerization can be found at [Dockerfile](./Dockerfile). The Dockerfile is based on the `python:3.9-slim` image. It copies all the necessary files into the container and installs the required dependency packages.
![docker output](https://github.com/Zunaied/Devops-task-v1/blob/main/images/docker%20output.png)


## CI/CD Workflow for Container

1. **Dockerfile Creation:**

   - The Dockerfile ([Dockerfile](./Dockerfile)) contains all the necessary instructions to build the application image.
2.  **GitHub Webhook Integration:**

   - Integrate a webhook in the GitHub repository settings that triggers Jenkins on each new commit.

   - This ensures an automated and streamlined CI/CD workflow, initiating the pipeline as soon as changes are pushed to the repository.
   ![webhook](https://github.com/Zunaied/Devops-task-v1/blob/main/images/github%20webhook.png)

3. **Jenkins Setup:**

   - Jenkins is configured to watch the Git repository for changes.

   - Upon detecting a new commit, Jenkins triggers a pipeline to build the Docker image.

   - The pipeline then pushes the built image to Docker Hub with a specified version.
![push-image](https://github.com/Zunaied/Devops-task-v1/blob/main/images/pushing%20image%20to%20docker%20hub.png)


4. **Docker Compose Deployment:**

   - Docker Compose ([docker-compose.yml](./docker-compose.yml)) is used to define and manage the multi-container Docker application.

   - The deployed application uses the Docker image from Docker Hub with the specified version.

   - Docker Compose ensures a clean and robust deployment by stopping the existing containers, releasing ports, and then starting the new containers.
![docker-compose-output](https://github.com/Zunaied/Devops-task-v1/blob/main/images/deploy%20w%20dc.png)

Container is running in 5500 port of the server
![docker-container](https://github.com/Zunaied/Devops-task-v1/blob/main/images/container%20creation.png)

![docker-output](https://github.com/Zunaied/Devops-task-v1/blob/main/images/container%20output.png)

![docker-output-2](https://github.com/Zunaied/Devops-task-v1/blob/main/images/container%20output-2.png)


## Kubernetes Deployment using jenkins CI/CD

This CI/CD process automates the deployment of the application to a Kubernetes cluster. The Kubernetes manifests, including deployment, service, and secret files, are organized in the [k8s-manifest](./k8s-manifest) directory.
### Manifest Files

- [Deployment](./k8s-manifest/deployment): Specifies the number of replicas and configurations for the application deployment.
- [Service](./k8s-manifest/service): Defines a NodePort service, exposing the application on port 30005.
- [Secret](./k8s-manifest/secret): Contains sensitive information, such as the OpenWeather API key.

![k8s-cd](https://github.com/Zunaied/Devops-task-v1/blob/main/images/k8s-cd.png)



### Jenkins Configuration

The [Jenkinsfile](./Jenkinsfile) is configured to authenticate with the Kubernetes cluster. It references the kubeconfig file as a secret and sets it in the environment.
![jenkins-pipeline](https://github.com/Zunaied/Devops-task-v1/blob/main/images/overall%20output.png)

### Kubernetes Deployment Stage

In the Jenkinsfile, a specific stage is dedicated to Kubernetes deployment.
![k8s-deploy](https://github.com/Zunaied/Devops-task-v1/blob/main/images/k8s-deploy.png)

 ![api/hello](https://github.com/Zunaied/Devops-task-v1/blob/main/images/Screenshot%202024-01-21%20171510.png)

![api/health](https://github.com/Zunaied/Devops-task-v1/blob/main/images/api%20health.png)


