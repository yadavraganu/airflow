from airflow.operators.empty import EmptyOperator
from airflow import DAG
from datetime import datetime
from airflow.models.baseoperator import cross_downstream, chain

dag = DAG(dag_id="Task_Relations",
          start_date=datetime(2024, 1, 1),
          schedule='@daily')

t1 = EmptyOperator(task_id='Task1', dag=dag)
t2 = EmptyOperator(task_id='Task2', dag=dag)
t3 = EmptyOperator(task_id='Task3', dag=dag)
t4 = EmptyOperator(task_id='Task4', dag=dag)
t5 = EmptyOperator(task_id='Task5', dag=dag)
t6 = EmptyOperator(task_id='Task6', dag=dag)
t7 = EmptyOperator(task_id='Task7', dag=dag)
t8 = EmptyOperator(task_id='Task8', dag=dag)
t9 = EmptyOperator(task_id='Task9', dag=dag)
t10 = EmptyOperator(task_id='Task10', dag=dag)
t11 = EmptyOperator(task_id='Task11', dag=dag)

"""t1.set_downstream(t2)
t2.set_downstream([t3, t4])
cross_downstream([t3, t4],[t5, t6])
chain([t5, t6], [t7, t8],[t9, t10])"""

t1 >> t2 >> [t3, t4]
t3 >> [t5, t6]
t4 >> [t5, t6]
t5 >> t7 >> t9
t6 >> t8 >> t10
[t9, t10] >> t11
