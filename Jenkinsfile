pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\staff\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest'
            }
        }

    }
}