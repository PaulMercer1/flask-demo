pipeline{
    environment {
        registry = "paulmercer/flaskdemo"
        registryCredentials = "dockerhub_id"
        dockerImage = ""
        HOME = "${env.WORKSPACE}"
    }

    agent any   
        stages {
            stage ('Testing'){
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

            stage ("Deploy to swarm") {
                steps {
                    sshPublisher(publishers: [sshPublisherDesc(configName: 'SwarmManager', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'cd /home/jenkins/swarm && docker stack deploy -c home/jenkins/swarm/docker-compose.yaml flask-app', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/home/jenkins/swarm', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '**/docker-compose.yaml, **/nginx.conf')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true)])
                }
            }

            stage ("Clean up"){
                steps {
                    script {
                        sh 'docker image prune --all --force --filter "until=168h"'
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