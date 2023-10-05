pipeline {
    agent any
    
    environment {
        // Define your Docker Hub credentials as environment variables
        DOCKER_HUB_USERNAME = credentials('docker-hub-username')
        DOCKER_HUB_PASSWORD = credentials('docker-hub-password')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build the Docker image with a specific tag
                    def dockerImage = docker.build(12Saifsayyed/saifimage:latest")
                    
                    // Authenticate with Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        // Push the Docker image to Docker Hub
                        dockerImage.push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Clean up the Docker workspace
            cleanWs()
        }
    }
}
