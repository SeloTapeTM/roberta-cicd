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
        }
    }
}