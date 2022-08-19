pipeline{
    environment {
        registry = "paulmercer/flaskdemo"
        registryCredentials = "dockerhub_id"
        dockerImage = ""
        HOME = "${env.WORKSPACE}"
    }

    agent any   
        stages {
            stage ("Testing") {
                steps{
                    sh 'pip install -r requirements.txt'
                    sh 'pytest-3 --junitxml results.xml'
                }
            }

            stage ('Build Docker Image'){
                steps{
                    script {
                        dockerImage = docker.build(registry)
                    }
                }
            }

            stage ("Push to Docker Hub"){
                steps {
                    script {
                        docker.withRegistry('', registryCredentials) {
                            dockerImage.push("${env.BUILD_NUMBER}")
                            dockerImage.push("latest")                    
                        }
                    }
                }
            }

            stage ("Clean up"){
                steps {
                    script {
                        sh "docker rmi $registry:$BUILD_NUMBER"
                        sh "docker rmi $registry:latest"
                    }
                }
            }            
        }
    
    post {
        always {
            junit "*.xml"
        }
    }
}