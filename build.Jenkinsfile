pipeline {
    agent any

    environment {
        DH_NAME = "selotapetm"
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
                {
                    sh '''
                    docker login -u $USERNAME -p $PASSWORD
                    docker build -t $DH_NAME/roberta-cicd:0.0.$BUILD_NUMBER .
                    docker push $DH_NAME/roberta-cicd:0.0.$BUILD_NUMBER
                    '''
                }

            }
            post {
                always{
                    sh 'docker image prune -a --force --filter "until=24h"'
                }
            }

        }
        stage('Trigger Deploy') {
            steps {
                build job: 'roberta-deploy', wait: false, parameters: [
                    string(name: 'ROBERTA_IMAGE_URL', value: "$DH_NAME/roberta-cicd:0.0.$BUILD_NUMBER")
                    ]
                }
            }
    }
}