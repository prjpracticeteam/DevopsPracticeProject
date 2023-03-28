pipeline {
    agent any
    stages{
        stage ('git checkout') {
            steps {
                git branch: 'project_task1', url: 'https://github.com/prjpracticeteam/DevopsPracticeProject.git'
            }
        }
        stage ('docker build') {
            steps {
                sh 'docker build -t python .'
            }
        }
        stage ('docker run') {
            steps {
                sh 'docker run --name python3 python'
            }
        }
    }
}
