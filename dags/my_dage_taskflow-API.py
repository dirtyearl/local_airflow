from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.helpers import chain


@dag(start_date=datetime(2023, 1, 1), description='A simple tutorial DAG', 
     tags=['data_science'], schedule='@daily', catchup=False)
def my_dag():

    @task
    def print_a():
        return print('hi from task a')
    
    @task
    def print_b():
        return print('hi from task b')
    
    @task
    def print_c():
        return print('hi from task c')
    
    @task
    def print_d():
        return print('hi from task d')
    
    @task
    def print_e():
        return print('hi from task e')
    
    chain(print_a(), [print_b(), print_c()], [print_d(), print_e()])

my_dag()