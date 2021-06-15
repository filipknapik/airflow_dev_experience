# This script will be executed in the Airflow container during the environment start up
# You can use it to initiate, e.g. Airflow Connections or change other settings
#
# To add an Airflow connection, uncomment the line below and update the command as needed
# (details on this command at https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#add ) 
# airflow connections add [-h] [--conn-description CONN_DESCRIPTION] [--conn-extra CONN_EXTRA] [--conn-host CONN_HOST] [--conn-login CONN_LOGIN] [--conn-password CONN_PASSWORD] [--conn-port CONN_PORT] [--conn-schema CONN_SCHEMA] [--conn-type CONN_TYPE] [--conn-uri CONN_URI] conn_id