def img
pipeline {
    environment{
        registry = "vishalt7/EMP-Portal-Project-DevOps"
        registryCredential = 'DOCKERHUB'
        githubCredential = 'None'
        dockerImage=''
    }
    agent any
    
    parameters{
        choice(
            choices: ['Dev', 'Prod'],
            description: 'Select the Target Environment',
            name: 'TARGET_ENVIRONMENT'
            )
    }
    
    stages{
        
        stage("Git Checkout"){
            steps{
               checkout scmGit(branches: [[name: '*/feature1920']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vishalt7/EMP-Portal-Project-DevOps.git']])
            }
        }

        stage("Install Packages"){
            steps{
                script{
                    sh 'echo password | sudo -S apt-get install pip -y'
                    sh 'echo password | sudo -S pip install -r requirements.txt'
                }

            }
        }
    }
}
