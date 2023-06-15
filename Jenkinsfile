pipeline{
    agent any
//    agent{
//     label "docker-agent-python"
//    }

    triggers{
        pollSCM "* * * * *"

    }

    stages{
        stage ("Build"){
            steps{
                echo "Building..."
                sh """
                pip install -r requirements.txt
               
                """

            }
        }

        
        stage ("Test"){
            steps{
                echo "Testing..."
                sh """
                python3 hello.py 

                """
            }
        }

        stage ("Deploy"){
            steps{
                echo "Deliver..."
                sh """
                echo "delivering stuff ..."
                
                """
            }
        }

    }
}