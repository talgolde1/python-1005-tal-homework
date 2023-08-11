pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def containerId = docker.build('world-of-games', '.').run("-p 8777:8777 -v ${WORKSPACE}/Scores.txt:/app/Scores.txt -d")
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
        stage('Stop Container') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('FAILURE') }
            }
            steps {
                script {
                    // Stop the container using the saved container ID
                    docker.container(env.CONTAINER_ID).stop()
                }
            }
        }
    }

    post {
        always {
            // Remove the image after the build is complete (optional)
            docker.image('world-of-games').remove()
        }
    }
}
