pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -vs test_pytest.py --alluredir=allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure([
                    results: [
                        [path: 'allure-results']
                    ]
                ])
            }
        }
    }
}
