from airflow.decorators import dag, task
from datetime import datetime
from pprint import pprint


@dag(start_date=datetime(2023, 6, 1), schedule='@daily', params={'param1': 'Hi', 'param2': 'Hello'}, catchup=False)
def Dag_With_Context():
    @task
    def Task_Access_Params(**context):
        pprint("Hello From Task_Access_Params")
        pprint(context['params'])

    @task
    def Task_Access_Conf(**context):
        pprint("Hello From Task_Access_Conf")
        pprint(context['conf'].as_dict())

    @task
    def Task_Access_Dag_Run_Date(**context):
        pprint("Hello From Task_Access_Dag_Run_Date")
        pprint(context['ds'])

    @task
    def Task_Details(**context):
        for i in context:
            pprint("Hello From Task_Dag_Run")
            pprint(i)

    Task_Access_Params() >> Task_Access_Conf() >> Task_Access_Dag_Run_Date() >> Task_Details()


Dag_With_Context()
