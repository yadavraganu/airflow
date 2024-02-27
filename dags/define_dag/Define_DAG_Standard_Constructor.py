import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

dag = DAG(
    dag_id="Define_DAG_Standard_Constructor",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
)
task1 = EmptyOperator(task_id="task1", dag=dag)
task2 = EmptyOperator(task_id="task2", dag=dag)
task1 >> task2
