# IDE Autocomplete for Apache Airflow

IDE Autocomplete provides Airflow developers with live templates for Operators and Sensors, automatically suggested by an IDE during DAG editing. 

Example for VS Code:

![VS Code](Images/VSCode.gif)

Example for PyCharm:

![VS Code](Images/PyCharm.gif)

In both cases, the code comes with a URL to the full specification and additional context on a particular Operator or Sensor. Both IDEs allow clicking on the link, which provides seamless documentation access. 

The repo also comes with a generator that automatically refreshes the configurations for both IDEs based on public Airflow documentation.

Next steps:
+ [Install PyCharm Autocomplete in your environment](Intellij_autocomplete/)
+ [Install VS Code Autocomplete in your environment](VSCode_autocomplete/)
+ [Regenerate the configurations for both IDEs based on Airflow documentation](Generator/)