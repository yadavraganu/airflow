import datetime
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2024, 1, 1), schedule="@daily")
def Define_DAG_Decorator():
    task1 = EmptyOperator(task_id="task1")
    task2 = EmptyOperator(task_id="task2")
    task1 >> task2


Define_DAG_Decorator()