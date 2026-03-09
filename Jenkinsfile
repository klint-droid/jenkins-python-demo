pipeline {
    agent any

    stages {
        stage('install dependencies') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('run tests') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest test_app.py'
            }
        }
        stage('run app') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }
    }
}