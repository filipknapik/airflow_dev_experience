# VS Code Autocomplete for Apache Airflow

This code enables Airflow Operators and Sensors autocomplete for VS Code as shown below:

![VS Code](../Images/VSCode.gif)

To install Airflow Autocomplete for VS Code, follow this process:
1. Open VS Code
2. Go to Preferences -> User Snippets and type in **python.json**
3. If the python.json file has no other snippets (empty JSON), replace its contents with the contents of python.json file from this folder
4. If the python.json file in your VS Code has some user snippets in it, add the contents of python.json file in this folder into your VS Code python.js, ensuring that newly added snippets are placed inside the curly brackets of the local python.json file. 

Note: this autocomplete applies only to Python files so please ensure that you select appropriate file type in the editor