pipeline {
    agent any   
        stages {

            stage ('Hello')
            {
                steps {
                    sh s'echo Hello World'
                }
            }

            stage ('Testing'){
                steps{
                    sh 'pip install -r requirements.txt'
                    sh 'pytest-3 --junitxml results.xml'
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