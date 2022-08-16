pipeline{
    environment {
        registry = "paulmercer/flaskdemo"
        registryCredentials = "dockerhub_id"
        dockerImage = ""
        HOME = "${env.WORKSPACE}"
    }

    agent any   
        stages {
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
                            dockerImage.push("latest")
                            dockerImage.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
            
        }
}