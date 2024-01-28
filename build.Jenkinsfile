pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'echo building....'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-userpass', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
                {
                    sh '''
                       docker login -u $USERNAME --password-stdin $PASSWORD
                       docker build selotapetm/roberta-cicd
                       docker tag selotapetm/roberta-cicd selotapetm/roberta-cicd:1.0
                       docker push selotapetm/roberta-cicd:1.0
                       '''
                }

            }
        }
    }
}