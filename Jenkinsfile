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
    def pythonVersion = "py27"

    try {
        pythonVersion = PYTHON_VERSION
        echo "Variable PYTHON_VERSION set, using: " + pythonVersion
    } catch(err) {
        echo "Variable PYTHON_VERSION not set, using default: " + pythonVersion
    }

    ws { timestamps { ansiColor('xterm') {
        stage('Get Code') {
            checkout scm
            // adjusting the build description:
            def gitDetails = getGitDetails(pwd())
            def dockerDetails = getDockerDetails()
            currentBuild.description = "Python:" + pythonVersion + ", commit:$gitDetails.commit" + ", last by:$gitDetails.author" + ", Docker:" + dockerDetails.version
        }

        stage('Build') {
            withEnv(["PYTHON_VERSION=" + pythonVersion]) {
                sh pwd() + '/scripts/run_python.sh'
            }
        }
    }}}
}
