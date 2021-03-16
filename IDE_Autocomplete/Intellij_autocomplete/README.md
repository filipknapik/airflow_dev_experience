# PyCharm Autocomplete for Apache Airflow

This code enables Airflow Operators and Sensors autocomplete for PyCharm. 

To install Airflow Autocomplete for PyCharm, follow these steps:
1. Clone this repo to your local file system
2. Open PyCharm
2. Go to File -> Manage IDE Settings -> Import Settings
3. Use the IDE_Autocomplete/Intellij_autocomplete/settings.zip file from the repo you have just cloned
4. **Important:** Uncheck all items to be important, leave only Templates and Templates (Live) settings checked. This will not delete any of your existing settings, instead it will create a new Template group called Airflow. To see it, go to Preferences -> Editor -> Live Templates -> Airflow

Note: this autocomplete applies only to Python files so please ensure that you select appropriate file type in the editor