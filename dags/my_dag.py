from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain

def print_a():
    return print('hi from task a')

def print_b():
    return print('hi from task b')

def print_c():
    return print('hi from task c')

def print_d():
    return print('hi from task d')

def print_e():
    return print('hi from task e')

default_args = {
    'retries': 3,
}

with DAG('my_dage', start_date=datetime(2023, 1, 1), 
         default_args=default_args,
         description='A simple tutorial DAG',
         tags=['data_science'],
         schedule='@daily', 
         catchup=False):

    # Define tasks here
    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b)
    task_c = PythonOperator(task_id='task_c', python_callable=print_c)
    task_d = PythonOperator(task_id='task_d', python_callable=print_d)
    task_e = PythonOperator(task_id='task_e', python_callable=print_e)

    chain(task_a, [task_b, task_c], [task_d, task_e])
