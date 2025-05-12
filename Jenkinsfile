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
                    // Obtener IP del host de forma confiable
                    def SERVER_IP = sh(
                        script: "hostname -I | awk '{print \$1}'",
                        returnStdout: true
                    ).trim()
                    
                    // Mostrar URL permanente (no temporal)
                    echo """
                    ============================================
                    ¡Aplicación Django desplegada correctamente!
                    
                    Accede a la aplicación en:
                    http://${SERVER_IP}:8000
                    
                    Para detenerla manualmente ejecuta:
                    docker-compose down
                    ============================================
                    """
                    
                    // Guardar la URL como artefacto
                    writeFile file: 'app_url.txt', text: "http://${SERVER_IP}:8000"
                    archiveArtifacts artifacts: 'app_url.txt'
                }
            }
        }
    }
    
}
