pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the Git repository
                git 'https://github.com/CFG113/black-chat.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build your application using Maven or Gradle
                sh 'mvn clean package'  // Adjust command as needed
            }
        }
        
        stage('Test') {
            steps {
                // Run JUnit tests
                sh 'mvn test'
            }

            post {
                always {
                    // Publish JUnit test results
                    junit '**/target/surefire-reports/*.xml'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy your application
                sh 'echo Deploying Application...'
            }
        }
        
        stage('Release') {
            steps {
                // Release stage commands
                sh 'echo Releasing Application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
