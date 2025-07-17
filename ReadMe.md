## Defining DAGS
### Using the DAG Class Constructor
```python
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id='my_first_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(days=1), # or '0 0 * * *' for daily at midnight
    catchup=False,
    tags=['example', 'tutorial'],
    description='A simple DAG to demonstrate basic Airflow concepts.',
) as dag:
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    task2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
    )

    task3 = BashOperator(
        task_id='echo_hello',
        bash_command='echo "Hello Airflow!"',
    )

    # Define task dependencies
    task1 >> task2 >> task3
```
## Using the `@dag` Decorator
```python
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

@dag(
    dag_id='my_decorated_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(hours=1),
    catchup=False,
    tags=['decorator'],
)
def my_workflow():
    task1 = BashOperator(
        task_id='print_time',
        bash_command='date +%H:%M:%S',
    )

    task2 = BashOperator(
        task_id='echo_decorated',
        bash_command='echo "This is a decorated DAG!"',
    )

    task1 >> task2

my_workflow() # Call the function to register the DAG
```
