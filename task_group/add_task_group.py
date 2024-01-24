from airflow.decorators import task, dag, task_group
import datetime


@dag(start_date=datetime.datetime(2024, 1, 1), schedule="@daily")
def Add_Task_Group():
    @task
    def Task(i=0):
        print("Running Task {i}")

    s = Task.override(task_id=f'Start_Task')()

    @task_group(group_id='task_group_1')
    def Task_Group():
        for i in [1, 2, 3]:
            t = Task.override(task_id=f'Task_{i}')()

    s >> Task_Group()


Add_Task_Group()
