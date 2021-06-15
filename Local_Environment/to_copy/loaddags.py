from airflow.models import DagBag
import sys
import subprocess

red = "\033[0;31m"
neutral = "\033[0m"

dagbag = DagBag()

if dagbag.import_errors != {}:
    print(red + "Error importing DAG(s)")
    for key in dagbag.import_errors:
        print(key + ":" + dagbag.import_errors[key])
    print(neutral)
    exit(1)

for DAG_ID in dagbag.dag_ids:
    print(DAG_ID+"...", end='')
    dag = dagbag.get_dag(dag_id=DAG_ID)

    if dag is None:
        print(red + "DAG is not created: " + DAG_ID + neutral)
        exit(2)
    elif len(dag.tasks)==0:
        print(red + "The following DAG has no tasks: " + DAG_ID + neutral)
        exit(3)
    else:
        print("\033[0;32mOK\033[0m")