pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            sh 'echo "this is for sample"'
          }
        }

        stage('stage1.2') {
          steps {
            sleep 2
          }
        }

      }
    }

  }
}