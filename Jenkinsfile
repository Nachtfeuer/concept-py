#!groovy

def getGitDetails(path) {
    dir(path) {
        return [
            commit:sh(script: 'git rev-parse --short HEAD' , returnStdout:true).trim(),
            author:sh(script: 'git log -1 --format="%an"', returnStdout: true).trim()
        ]
    }
}

node {
    ws { timestamps { ansiColor('xterm') {
        stage('Get Code') {
            checkout scm
            def gitDetails = getGitDetails(pwd())
            currentBuild.description = "Python:" + PYTHON_VERSION + ", commit:$gitDetails.commit" + ", last by:$gitDetails.author"
        }

        stage('Build') {
            sh pwd() + '/scripts/run_python.sh'
        }
    }}}
}
