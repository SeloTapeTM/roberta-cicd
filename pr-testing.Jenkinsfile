pipeline {
    agent any

    stages {
        stage('Installs') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install pytest
                '''
            }
        }
        stage('Unittest') {
            steps {
                sh 'python3 -m pytest --junitxml results.xml tests'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'results.xml'
                }
            }
        }
        stage('Lint') {
            steps {
                sh 'echo "linting"'
            }
        }
        stage('Functional test') {
            steps {
                sh 'echo "testing"'
            }
        }
    }
}