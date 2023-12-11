pipeline {
    agent {
        dockerfile {
            additionalBuildArgs '-t jenkins-chest_ct_ner'
            args '--gpus all'
        }
    }
    environment {
            TRACKING_URI = "http://192.168.1.76:9527"
            PROJECT_NAME = 'chest_ct_ner'
            NEW_DATA_DIR = './new_data'
            AWS_ACCESS_KEY_ID = "lxzZTFO4o2W68FznEfGT"
            AWS_SECRET_ACCESS_KEY = "CWYvxv6G1DQpPLT3NCuwbbbqNzz1rAhOHzAGka7e"
            MLFLOW_S3_ENDPOINT_URL = "https://s3.minio.wingene.k8s"
            MLFLOW_S3_IGNORE_TLS = true
            GITEA_CRED = credentials('3251a418-9084-4a30-a088-ed294f492388')
        }
    stages {
        stage('Data extraction') {
            steps {
                sh '1_data_extraction/run_data_extraction.sh'
            }
        }
        stage('Data validation') {
            steps {
                sh '2_data_validation/run_data_validation.sh'
            }
        }
        stage('Data preparation') {
            steps {
                sh '3_data_preparation/run_data_preparation.sh'
            }
        }
        stage('Model training') {
            steps {
                sh '4_model_training/run_model_training.sh'
            }
        }
    }
    post{
        always {
            cleanWs()
        }
    }
}
