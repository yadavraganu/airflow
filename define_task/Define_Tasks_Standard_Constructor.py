import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
        dag_id="Define_Tasks_Context_Manager",
        start_date=datetime.datetime(2024, 1, 1),
        schedule="@daily",
):
    task1 = BashOperator(task_id="task1", bash_command="""echo 'Running task1'""")
    task2 = BashOperator(task_id="task2", bash_command="""echo 'Running task2'""")
    task1 >> task2
