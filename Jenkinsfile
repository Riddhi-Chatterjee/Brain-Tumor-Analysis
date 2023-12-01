pipeline {
    agent any 

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
                sh 'python3 download_models.py' //Downloading our models from google drive
                sh 'tar czf BrainTumorAnalysis.tar.gz Brain_Tumor_Classification static templates backend.py download_models.py frontend.py Jenkinsfile requirements.txt' //Creating a compressed archive of the required files and directories
            }
        }
        stage('Test') {
            steps {
                sh 'python3 Brain_Tumor_Classification/test.py'//Testing the classifier
            }
        }
    }
}
