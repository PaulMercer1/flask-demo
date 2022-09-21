pipeline {
    agent any   
        stages {

            stage ('Hello')
            {
                steps {
                    sh 'echo Hello World'
                }
            }

            stage ('Testing'){
                steps{
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest --junitxml results.xml'
                }
            }

            stage ('Goodbye')
            {
                steps {
                    sh 'echo goodbye World'
                }
            }
        }
           
    
    post {
        always {
            junit "*.xml"
        }
    }   
}