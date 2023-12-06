pipeline {
    agent any 

    environment {
            CI = 'true'
            registry = 'riddhich/brain-tumor-analysis'
            DOCKERHUB_CREDENTIALS = credentials('Riddhi-DockerHub-Creds')
            dockerimage = ''
    }

    stages {
        stage('Git pull') {
            steps {
                git url: 'https://github.com/Riddhi-Chatterjee/Brain-Tumor-Analysis.git', branch: 'main'
            }
        }
        // stage('Build') {
        //     steps {
        //         sh 'pip3 install --upgrade pip' //Upgrading pip3
        //         sh 'pip3 install -r requirements.txt' //Installing the required libraries
        //         sh '''cd backend
        //               python3 download_models.py''' //Downloading our models from google drive
        //     }
        // }
        // stage('Test') {
        //     steps {
        //         sh '''cd backend
        //               python3 Brain_Tumor_Classification/test.py''' //Testing the classifier 
        //     }
        // }
        // stage('Build backend docker image') {
		// 	steps {
        //         script {
        //             sh 'docker build -t '+registry+'-backend:latest backend/'
        //             try {
        //                 sh 'docker rmi -f $(docker images -a -q -f "dangling=true")'
        //             } 
        //             catch (Exception e) {
        //                 echo "No images to delete... continuing with the pipeline..."
        //             }
        //         }
		// 	}   
		// }
        // stage('Build frontend docker image') {
        //     steps {
        //         script {
        //             sh 'docker build -t '+registry+'-frontend:latest frontend/'
        //             try {
        //                 sh 'docker rmi -f $(docker images -a -q -f "dangling=true")'
        //             } 
        //             catch (Exception e) {
        //                 echo "No images to delete... continuing with the pipeline..."
        //             }
        //         }
        //     }   
        // }
        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        // stage('Push backend docker image to DockerHub') {
		// 	steps {
		// 	    sh 'docker push '+registry+'-backend:latest'
		// 	}
		// }
        // stage('Push frontend docker image to DockerHub') {
        //     steps {
        //         sh 'docker push '+registry+'-frontend:latest'
        //     }
        // }
        // stage('Free local space') {
        //     steps {
        //         sh 'docker rmi -f $(docker images -q)'
        //     }
        // }
        stage('Ansible Deploy') {
            steps {
                ansiblePlaybook becomeUser: 'null',
                colorized: true,
                installation: 'Ansible',
                inventory: 'inventory',
                playbook: 'ansible-playbook.yml',
                sudoUser: 'null',
            }
        }
    }
}
