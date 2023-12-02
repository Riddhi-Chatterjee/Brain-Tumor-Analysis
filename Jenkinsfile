pipeline {
    agent any 

    environment {
            CI = 'true'
            registry = 'riddhich/brain-tumor-analysis'
            DOCKERHUB_CRED = credentials('CRED_DOCKER')
            registryCredential = 'CRED_DOCKER'
            dockerimage = ''
    }

    stages {
        stage('Git pull') {
            steps {
                git url: 'https://github.com/Riddhi-Chatterjee/Brain-Tumor-Analysis.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh 'pip3 install --upgrade pip' //Upgrading pip3
                sh 'pip3 install -r requirements.txt' //Installing the required libraries
                sh '''cd backend
                      python3 download_models.py''' //Downloading our models from google drive
            }
        }
        stage('Test') {
            steps {
                sh '''cd backend
                      python3 Brain_Tumor_Classification/test.py''' //Testing the classifier 
            }
        }
        stage('Build backend docker image') {
			steps {
			    sh '/usr/local/bin/docker build -t '+registry+'-backend:latest backend/'
			}   
		}
        stage('Build frontend docker image') {
            steps {
                sh '/usr/local/bin/docker build -t '+registry+'-frontend:latest frontend/'
            }   
        }
        stage('Login to DockerHub') {
            steps {
                sh '/usr/local/bin/docker login -u "riddhich" -p "rocker@43893"'
            }
        }
        stage('Push backend docker image to DockerHub') {
			steps {
			    sh '/usr/local/bin/docker push '+registry+'-backend:latest'
			}
		}
        stage('Push frontend docker image to DockerHub') {
            steps {
                sh '/usr/local/bin/docker push '+registry+'-frontend:latest'
            }
        }
        stage('Free local space') {
            steps {
                sh '/usr/local/bin/docker rmi '+registry+'-backend:latest'
                sh '/usr/local/bin/docker rmi '+registry+'-frontend:latest'
            }
        }
    }
}
