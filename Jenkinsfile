pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Django Tests') {
            steps {
                sh 'docker-compose run web python manage.py test --noinput'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    post {
        always {
            sh 'docker-compose down'  // Limpia contenedores después del build
        }
    }
}
