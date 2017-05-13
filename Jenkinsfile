#!groovy
node {
    ws { timestamps { ansiColor('xterm') {
        stage('Get Code') {
            checkout scm
        }

        stage('Build') {
            sh pwd() + '/scripts/run_python.sh'
        }
    }}}
}
