pipeline {
    options {
        timestamps()
    }

    agent any

    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u=root'
                }
            }
            steps {
    script {
        sh 'apk add --update python3 py3-pip'
        sh 'python3 -m venv /path/to/venv'
        sh '/path/to/venv/bin/pip install unittest2==1.1.0'
        sh '/path/to/venv/bin/pip install xmlrunner'
        sh '/path/to/venv/bin/python3 test.py'
    }
}
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
    }
}
