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

## How to use:
1. If not done yet, install gcloud and authenticate (gcloud auth login) to the project with a Cloud Composer environment that you will use for staging/test
2. Identify a local folder you will use for DAG development. Ideally, link it with a source control tool like Cloud Source Repositories or GitLab (git init and remote push)
3. Create a folder for local Airflow instance (independent of the DAG folder). Enter this folder and run 'git clone https://github.com/filipknapik/airflow_dev_experience'
4. Enter 'airflow_dev_experience/Local_Environment/' and run './start'. The first time you run it, you will be asked a few questions. If you want to modify your responses in the future, edit 'config/env.cfg'.
That's it!

Your Airflow environment is available at [http://localhost:8068](http://localhost:8068). 
DAGs from the folder you have provided when running ./start will automatically show up in the environment. 

 To change settings, edit:
  - PyPi packages: config/pypi.cfg
  - Airflow variables: config/variables.cfg
  - Connections: config/others.sh
...and run ./start to apply changes

 You may also use: 
  ./test - tests all your DAGs
  ./cli - starts a bash session with access to a local Airflow CLI
  ./pushdags - transfers local DAGs to a Composer development environment
  ./stop - stops local Airflow environment. Doesn't affect your local DAGs

