pipeline {
    agent any   
        stages {
            stage ('Testing'){
                steps{
                    sh 'pip install -r requirements.txt'
                    sh 'pytest-3 --junitxml results.xml'
                }
            }
        }
           
    
    post {
        always {
            junit "*.xml"
        }
    }   
}