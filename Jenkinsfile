pipeline {
    agent any

     environment {
        KUBECONFIG = credentials('KUBECONFIG')
    }

    stages {
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/Zunaied/Devops-task-v1.git", branch: "main"
            }
        }

        stage("Docker Build") {
            steps {
                echo "Building the image"
                sh "docker build -t api ."
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "Pushing the image to Docker Hub"
                script {
                    withCredentials([usernamePassword(credentialsId: "docker-hub-cred", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                        def imageName = "${env.dockerHubUser}/api:v4"
                        sh "docker tag api $imageName"
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker push $imageName"
                    }
                }
            }
        }


        stage("Deploy to container") {
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
         stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f /var/lib/jenkins/workspace/check/k8s-manifest/secret.yml --kubeconfig=${KUBECONFIG}"
                    sh "kubectl apply -f /var/lib/jenkins/workspace/check/k8s-manifest/deployment.yml --kubeconfig=${KUBECONFIG}"
                    sh "kubectl apply -f /var/lib/jenkins/workspace/check/k8s-manifest/service.yml --kubeconfig=${KUBECONFIG}"
                }
                }
            }
        }
}
    

