pipeline {

    agent any
    parameters {
        choice(
            name: 'TEST_FILE',
            choices: [
                'test_pytest.py',
                'test_api.py',
                'test_pytest_features.py'
            ],
            description: 'Select the test file to execute'
        )
    }
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
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'pytest -vs %TEST_FILE% --alluredir=allure-results'
                }
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
