pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    def containerId = docker.build("python:3.9")  // Use the correct image name
                    env.CONTAINER_ID = containerId
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    def container = docker.image("python:3.9").withRun("-p 8777:8777 -v ${WORKSPACE}/Scores.txt:/app/Scores.txt") {
                        sh 'sleep 10'
                    }
                    env.CONTAINER_ID = container.id
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python e2e.py'
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
                    docker.image("python:3.9").inside("--rm -v ${containerId}:/app") {
                        sh 'echo Cleaning up the container'
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
