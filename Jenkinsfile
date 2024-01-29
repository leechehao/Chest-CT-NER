pipeline {
    agent {
        // docker { image 'bryant' }
        dockerfile {
            additionalBuildArgs '-t jenkins-chest_ct_ner'
            args '--gpus all'
        }
    }
    environment {
            TRACKING_URI = credentials('75541b4f-29c2-4667-8903-986d54e66a0b')
            EXPERIMENT_NAME = 'Chest-CT-NER'
            REGISTERED_MODEL_NAME = 'chest-ct-ner'
            PROJECT_NAME = 'chest_ct_ner'
            NEW_DATA_DIR = './new_data'
            AWS_ACCESS_KEY_ID = credentials('57a926de-56bd-4634-840d-986f704ce9bd')
            AWS_SECRET_ACCESS_KEY = credentials('c522bcb8-8c81-486a-8022-f1f70c016a26')
            MLFLOW_S3_ENDPOINT_URL = credentials('f9527c9d-6b16-4677-b7e7-0bfac884a319')
            MLFLOW_S3_IGNORE_TLS = true
            GITEA_CRED = credentials('726c3241-f2bf-4628-83fd-d9e143737241')
            TOKEN = credentials('ef19446d-6168-4562-8bf2-935f46a48ab7')
            TOKEN_NAME = credentials('43bdeab8-2091-4c48-adc5-6b62c94e714b')
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
        stage('Model evaluation') {
            steps {
                sh '5_model_evaluation/run_model_evaluation.sh'
            }
        }
        stage('Model validation') {
            steps {
                sh '6_model_validation/run_model_validation.sh'
            }
        }
    }
    post{
        always {
            cleanWs()
        }
        // failure {
        //     slackSend(color: "danger", message: "Failed Pipeline: ${env.JOB_NAME}\nSomething is wrong with ${env.BUILD_URL}")
        //     mail to: 'bryant.lee@wingene.com.tw',
        //          subject: "Failed Pipeline: ${env.JOB_NAME}",
        //          body: "Something is wrong with ${env.BUILD_URL}"
        // }
    }
}
