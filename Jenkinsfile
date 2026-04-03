pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('aceest-gym') {
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('aceest-gym') {
                    sh 'export PYTHONPATH=$(pwd) && python3 -m pytest -v'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('aceest-gym') {
                    sh 'docker build -t aceest-gym-app .'
                }
            }
        }
    }
}
