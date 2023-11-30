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
                sh 'pip3 install --upgrade pip3 -r requirements.txt' 
                sh 'python3 download_models.py'
            }
        }
    }
}
