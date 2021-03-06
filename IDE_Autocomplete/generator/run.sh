#!/bin/sh

# Refresh files
python3 ./go.py

# Copy Intellij file
cd ../Intellij_autocomplete
rm templates/Airflow.xml
mv ../generator/Airflow.xml templates/Airflow.xml

# Refresh Intellij settings ZIP file
zip -r settings.zip templates/Airflow.xml

# Move VS code file
cd ../generator
rm ../VSCode_autocomplete/python.json
mv python.json ../VSCode_autocomplete/python.json