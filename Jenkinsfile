pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "python:3.9"
        CONTAINER_ID = ""
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Print Workspace Path') {
            steps {
                script {
                    echo "Workspace path: ${WORKSPACE}"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    dockerImage = docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Run the Docker container
                    if (isUnix()) {
                        CONTAINER_ID = dockerImage.run("-p 8777:8777 -v /app/Scores.txt:/app/Scores.txt -d")
                            .id
                    } else {
                        CONTAINER_ID = dockerImage.run("-p 8777:8777 -v C:/path/to/Scores.txt:/app/Scores.txt -d")
                            .id
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        if (isUnix()) {
                            sh 'python e2e.py'
                        } else {
                            bat 'python e2e.py'
                        }
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                if (CONTAINER_ID) {
                    if (isUnix()) {
                        sh "docker stop ${CONTAINER_ID}"
                    } else {
                        bat "docker stop ${CONTAINER_ID}"
                    }
                }
            }
        }
        success {
            script {
                if (isUnix()) {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
    }
}

def isUnix() {
    return agent.label == null || agent.label.startsWith('linux')
}
