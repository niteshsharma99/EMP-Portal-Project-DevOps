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

        stage("pylint testing"){
            steps{
                sh "pip install pylint"
                sh "pylint app.py"
            }
        }

    }

    post{
        always{

            sript{

                step{
                def buildStatus = currentBuild.currentResult ?: 'UNKNOWN'
                def color = buildStatus== 'SUCCESS' ? 'good' : 'danger'
                }
                slackSend(
                    channel: '#devops-project',
                    color: color,
                    message: "Build ${env.BUILD_NUMBER} ${buildStatus}: STAGE=${env.STAGE_NAME}",
                    teamDomain: 'xaidv05',
                    tokenCredentialId: 'slackcred'
                )
                }
            }
        }
    
}
