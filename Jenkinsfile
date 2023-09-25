pipeline {
    agent { 
        node {
            label 'jenkins-blender-tester'
        }
    }
    parameters {
        string(name: "x_resolution", trim: true, description: "the width of the rendered image")
        string(name: "y_resolution", trim: true, description: "the height of the rendered image")
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
                pytest -sv test_blender.py --x_resolution $x_resolution --y_resolution $y_resolution --blender_path "blender" --output_path "/results"
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '/results/*'
            sh '''
            rm -r '/results/*'
            '''
        }
    }
}