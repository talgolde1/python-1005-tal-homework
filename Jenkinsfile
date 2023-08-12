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
                    def containerId = docker.build("world-of-games")  // Use the correct image name
                    env.CONTAINER_ID = containerId
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    def container = docker.image("world-of-games").withRun("-p 8777:8777 -v ${WORKSPACE}/Scores.txt:/app/Scores.txt") {
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
        success {
            script {
                docker.withRegistry('', 'dockerhub-credentials') {
                    docker.image("world-of-games").push("${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
