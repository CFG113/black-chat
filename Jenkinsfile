pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'mvn clean package' // Replace with your build commands
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'mvn test' // Replace with your test commands
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Analyzing Code Quality...'
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker build -t myapp .'
                sh 'docker run -d -p 8080:8080 myapp'
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing...'
                sh 'docker push myapp'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

