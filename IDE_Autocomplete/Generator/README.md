# Generator of PyCharm/VS Code Autocomplete snippets for Apache Airflow

This scripts regenerates snippets used in PyCharm and VS Code based on public Airflow documentation. The script parses public Airflow pages listed in url.txt file, extracts the samples of all operators and sensors from these files and then generates files that can be used by IDEs for autocompletion.  

The script has been developed and tested in MacOS, and should also work in modern Linux workstations. There is no Windows equivalent at this point but contributions are welcome! 

To run the script, follow these steps:
1. Clone the repository to a local machine
2. Run the run.sh script
3. Output files are in Intellij and VSCode folders, use installation instructions for either IDE to install refreshed snippets 