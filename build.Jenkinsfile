pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        DH_NAME = "selotapetm"
        FULL_VER = "0.0.$BUILD_NUMBER"
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
                {
                    sh '''
                    docker login -u $USERNAME -p $PASSWORD
                    docker build -t $DH_NAME/roberta-cicd:$FULL_VER .
                    docker push $DH_NAME/roberta-cicd:$FULL_VER
                    '''
                }
                withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')])
                {
                    sh '''
                    export SNYK_TOKEN
                    echo $SNYK_TOKEN
                    snyk container test $DH_NAME/roberta-cicd:$FULL_VER --file=Dockerfile
                    '''
                }

            }
        }
        stage('Trigger Deploy') {
            steps {
                build job: 'roberta-deploy', wait: false, parameters: [
                    string(name: 'ROBERTA_IMAGE_URL', value: "$DH_NAME/roberta-cicd:$FULL_VER")
                    ]
                }
            }
    }
    post {
        always {
            sh '''
            docker system prune -a --force
            '''
            cleanWs()
        }
    }
}