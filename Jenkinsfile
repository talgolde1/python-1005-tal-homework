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
                    docker.build("my-flask-app")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image("my-flask-app").withRun('-p 8777:8777 -v $(pwd)/Scores.txt:/Scores.txt') {
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
                docker.image("my-flask-app").remove()
            }
        }
        success {
            script {
                docker.withRegistry('', 'dockerhub-credentials') {
                    docker.image("my-flask-app").push("${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
