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
                sh 'python3 -m pip3 install --upgrade pip3'
                sh 'pip3 install -r requirements.txt' 
                sh 'python3 download_models.py'
            }
        }
    }
}
