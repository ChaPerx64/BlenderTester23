pipeline {
    agent { 
        node {
            label 'jenkins-blender-tester'
        }
    }
    stages {
        stage('Image resolution input') {
            steps {
                input message: 'Enter resolution', ok: 'Enter', parameters: [string(defaultValue: '500', name: 'x_resolution', trim: true), string(defaultValue: '500', name: 'y_resolution', trim: true)]
            }
        }
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
                python3 tests_runner.py "/blender-3.3.11-linux-x64.tar/blender" . 1000 1000 --create-dir=True
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