pipeline {
    agent { 
        node {
            label 'jenkins-blender-tester'
        }
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                echo "Pulling repo from github.."
                git url: 'https://github.com/ChaPerx64/BlenderTester23.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 tests_runner.py "/usr/bin/blender" . 200 200
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}