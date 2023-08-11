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
                    docker.build("world-of-games")  // Use the correct image name
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image("world-of-games").withRun('-p 8777:8777 -v $(pwd)/Scores.txt:/app/Scores.txt') {
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
                docker.image("world-of-games").remove()  // Use the correct image name
            }
        }
        success {
            script {
                docker.withRegistry('', 'dockerhub-credentials') {
                    docker.image("world-of-games").push("${env.BUILD_NUMBER}")  // Use the correct image name
                }
            }
        }
    }
}
