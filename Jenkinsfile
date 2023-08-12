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
                    def container = docker.image('python:3.9').run("-p 8777:8777 -v /app/Scores.txt:/app/Scores.txt")
                    env.CONTAINER_ID = container.id
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        def appUrl = "http://localhost:8777"
                        bat 'python e2e.py' + appUrl
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
                    docker.image('python:3.9').inside("--rm -v /app/Scores.txt:/app/Scores.txt") {
                    }
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
