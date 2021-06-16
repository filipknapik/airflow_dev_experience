# Local Apache Airflow development environment for Cloud Composer

This is to provide a local development for Cloud Composer. 
The model supports
- Creation of a local Airflow instance based on a regular Cloud Composer staging/test environment. Local environment uses the same Airflow image and PyPi modules as your cloud environment
- Local environment supports Airflow Web UI at http://localhost and supports Airflow CLI
- Changes to DAGs in a local DAG folder are immediately visible in the local Airflow envrionment (mounting)
- Built-in support for local Environment Variables, PyPi modules and Connections
- Built-in DAG tests with easy access through Visual Studio Code and PyCharm
- Built-in authentication to Google Cloud allows DAG testing with Google Cloud resources (e.g. BigQuery)
- Support for both Airflow 1.* and 2.*
- The model was tested mostly under macOS but should work with other Linux distributions. There is currently no support for Windows. 

How to use:
1. If not done yet, install gcloud and authenticate (gcloud auth login) to the project with a Cloud Composer environment that you will use for staging/testing
2. Identify a local folder you will use for DAG development. Ideally, link it with a source control tool like Cloud Source Repositories or GitLab

![VS Code](Images/VSCode.gif)

Example for PyCharm:

![VS Code](Images/PyCharm.gif)

In both cases, the code comes with a URL to the full specification and additional context on a particular Operator or Sensor. Both IDEs allow clicking on the link, which provides seamless documentation access. 

The repo also comes with a generator that automatically refreshes the configurations for both IDEs based on public Airflow documentation.

Next steps:
+ [Install PyCharm Autocomplete in your environment](Intellij_autocomplete/)
+ [Install VS Code Autocomplete in your environment](VSCode_autocomplete/)
+ [Regenerate the configurations for both IDEs based on Airflow documentation](Generator/)