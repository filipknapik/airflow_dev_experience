# Local Airflow development environment for Cloud Composer

The model supports:
- Local Airflow instance based on you Cloud Composer staging/test environment. Local Airflow environment uses the same Airflow image and PyPi modules as your Cloud Composer environment
- Local environment provides Airflow Web UI at http://localhost and Airflow CLI through terminal
- Changes to DAGs in a local DAG folder are immediately visible in the local Airflow envrionment (no syncing)
- Support for local Airflow Variables, PyPi modules and Connections
- Built-in DAG tests with easy access through Visual Studio Code and PyCharm
- Built-in authentication to Google Cloud allows local DAG runs with Google Cloud resources (e.g. BigQuery)
- Support for DAG push to the staging Composer environment (although recommended path is through source control)
- Works with Airflow 1.* and 2.*
- The model was created under macOS but should work with other Linux distributions. There is currently no support for Windows. 

## Installation guide
1. If not done yet, install gcloud and select a project (gcloud config set project *myprojectid*) with a Cloud Composer environment that you use for staging/test
2. Identify a local folder you use for your DAGs. Ideally, link it with a source control tool like Cloud Source Repositories (git init and remote push)
3. Create a folder for local Airflow instance (outside of the DAG folder). Enter this folder and run 'git clone https://github.com/filipknapik/airflow_dev_experience'
4. Enter 'airflow_dev_experience/Local_Environment/' folder and run './start'. The first time you run it, you will be asked a few questions. If you want to modify your responses in the future, edit 'config/env.cfg'.

That's it!

Your Airflow environment is available at [http://localhost:8068](http://localhost:8068). 
Edit DAGs in the /DAGs folder of the Local environment. 

If you provided a proper Service Account key, your DAGs will be able to orchestrate tasks in Google Cloud. 

## Interacting with the tool using shell scripts
 You may also use: 
  - ./test - tests all your DAGs
  - ./cli - starts a bash session with access to a local Airflow CLI
  - ./pushdags - transfers local DAGs to a Composer development environment
  - ./stop - stops local Airflow environment. Doesn't affect your local DAGs
  
 To change settings, edit:
  - PyPi packages: config/pypi.cfg
  - Airflow variables: config/variables.cfg
  - Connections: config/others.sh
...and run ./start to apply changes

## Interacting with the tool using VS Code
 Open new VS Code window and open 'Local_Environment' folder that you have cloned. All your DAGs are available in the DAGs subfolder (they are linked there from the actual folder that you have provided for your DAGs)

 You may also use: 
  - ./test - tests all your DAGs
  - ./cli - starts a bash session with access to a local Airflow CLI
  - ./pushdags - transfers local DAGs to a Composer development environment
  - ./stop - stops local Airflow environment. Doesn't affect your local DAGs

 To change settings, edit:
  - PyPi packages: config/pypi.cfg
  - Airflow variables: config/variables.cfg
  - Connections: config/others.sh
...and run ./start to apply changes


