import datetime
from airflow.decorators import task, dag
import random


@dag(start_date=datetime.datetime(2024, 1, 1), schedule='@daily')
def Tasks_Branching():
    @task.branch
    def Branching_Func():
        return 'task_'+str(random.randint(2, 5))

    @task
    def Start_Task(input=1):
        print('Running {input} Task')

    s = Start_Task()
    b = Branching_Func()

    s >> b

    for i in range(2, 6):
        t = Start_Task.override(task_id=f'task_{i}')()
        b >> t


Tasks_Branching()
