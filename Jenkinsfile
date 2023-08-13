pipeline {
    agent any

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
                    def containerId = docker.build("python:3.9")
                    env.CONTAINER_ID = containerId
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    def container = docker.image('python:3.9').run("-p 5000:5000 -v /app/Scores.txt:/app/Scores.txt")
                    env.CONTAINER_ID = container.id
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        bat 'python e2e.py'
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
                def containerId = env.CONTAINER_ID ?: ""
                if (containerId) {
                    def container = docker.image('python:3.9').stop("${containerId}")
                }
            }
        }
        success {
            script {
                docker.withRegistry('', 'dockerhub-credentials') {
                    docker.image("python:3.9").push("${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
