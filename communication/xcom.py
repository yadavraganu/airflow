from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime


def Set_Xcom_Task(ti):
    ti.xcom_push(key='Task1', value={'Name': 'Test'})


def Get_Xcom_Task(ti):
    val = ti.xcom_pull(key='Task1', task_ids='task1')
    print(f'Pulled Value from xcom {val}')


with DAG(start_date=datetime(2024, 1, 1), dag_id='Xcom', schedule='@daily', catchup=False):
    task1 = PythonOperator(task_id='task1', python_callable=Set_Xcom_Task)
    task2 = PythonOperator(task_id='task2', python_callable=Get_Xcom_Task)
    task1 >> task2
