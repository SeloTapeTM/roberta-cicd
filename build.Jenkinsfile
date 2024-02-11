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
                    echo "Good luck!"
                    snyk auth $SNYK_TOKEN
                    snyk ignore --id='SNYK-PYTHON-TRANSFORMERS-6135747'
                    snyk ignore --id='SNYK-DEBIAN11-ZLIB-6008961'
                    snyk container test $DH_NAME/roberta-cicd:$FULL_VER --file=Dockerfile --severity-threshold=critical
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
            docker system prune -a -f --filter "until=24h"
            docker builder prune -a -f --filter "until=24h"
            '''
            cleanWs()
        }
    }
}