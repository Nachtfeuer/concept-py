#!groovy

def getGitDetails(path) {
    dir(path) {
        return [
            commit:sh(script: 'git rev-parse --short HEAD' , returnStdout:true).trim(),
            author:sh(script: 'git log -1 --format="%an"', returnStdout: true).trim()
        ]
    }
}

def getDockerDetails() {
    return [
        version:sh(script: "docker version -f '{{json .}}'|jq -r '.Client.Version'", returnStdout:true).trim()
    ]
}

node {
    ws { timestamps { ansiColor('xterm') {
        stage('Get Code') {
            checkout scm
            // adjusting the build description:
            def gitDetails = getGitDetails(pwd())
            def dockerDetails = getDockerDetails()
            currentBuild.description = "Python:" + PYTHON_VERSION + ", commit:$gitDetails.commit" + ", last by:$gitDetails.author" + ", Docker:" + dockerDetails.version
        }

        stage('Build') {
            sh pwd() + '/scripts/run_python.sh'
        }
    }}}
}
