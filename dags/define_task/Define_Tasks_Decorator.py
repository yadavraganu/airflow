import datetime
from airflow.decorators import task, dag


@dag(start_date=datetime.datetime(2024, 1, 1), schedule='@daily')
def Define_Tasks_Decorator():
    @task
    def First_Task():
        print('Running First Task')

    @task
    def Second_Task():
        print('Running Second Task')

    Second = Second_Task()
    First = First_Task()

    First >> Second


Define_Tasks_Decorator()
