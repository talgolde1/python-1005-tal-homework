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
                    def containerId = docker.build("world-of-games")
                    env.CONTAINER_ID = containerId
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image("world-of-games").withRun("-p 8777:8777 -v ${WORKSPACE}/Scores.txt:/app/Scores.txt") {
                        sh 'sleep 10'
                    }
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
                docker.image("world-of-games").remove()
            }
        }
        success {
            script {
                docker.withRegistry('https://registry.example.com', 'dockerhub-credentials') {
                    docker.image("world-of-games").push
                }
            }
        }
    }
}

