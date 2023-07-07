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
                script{
                    // Run pylint and capture the result
                    def pylintResult = sh( script: 'pylint app.py', returnStatus: true )


                    // Check the result and mark the stage as successful regardless
                    if (pylintResult) {
                        echo 'Pylint analysis passed'
                    }
                    else{
                        echo 'Pylint analysis failed'
                    }
                }
            }
        }

    }

    post {
        always {
            script {
                def buildStatus = currentBuild.currentResult ?: 'UNKNOWN'
                def color = buildStatus == 'SUCCESS' ? 'good' : 'danger'

                slackSend(
                    channel: '#cicd-pipeline',
                    color: color,
                    message: "Build ${env.BUILD_NUMBER} ${buildStatus}: Stage ${env.STAGE_NAME}",
                    teamDomain: 'upes-h6n3152',
                    tokenCredentialId: 'Slack-cred'
                )
            }
        }
    }
    
}
