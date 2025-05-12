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
                script {
                    // Obtiene la IP de la máquina
                    def IP = sh(script: "hostname -I | awk '{print \$1}'", returnStdout:true).trim()
                    // Muestra la URL (aunque luego se limpie con down)
                    echo " Aplicación temporalmente disponible en: http://${IP}:8000"
                    echo " Nota: Los contenedores se detendrán al finalizar el pipeline (por el 'docker-compose down')"
                }
            }
        }
    }
    post {
        always {
            sh 'docker-compose down'
            echo " Contenedores limpiados. Para usar la app, ejecuta manualmente: docker-compose up -d"
        }
        success {
            echo "Pipeline completado! Para acceder a la app:"
            echo "1. Ejecuta manualmente: docker-compose up -d"
            echo "2. Abre en tu navegador: http://\$(hostname -I | awk '{print \$1}'):8000"
        }
    }
}
