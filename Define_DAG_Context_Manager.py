import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="Define_DAG_Context_Manager",
        start_date=datetime.datetime(2024, 1, 1),
        schedule="@daily",
):
    task1 = EmptyOperator(task_id="task1")
    task2 = EmptyOperator(task_id="task2")
    task1 >> task2