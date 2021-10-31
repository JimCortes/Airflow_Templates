import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    catchup=False,
) as dag:
    user_purchase_table = PostgresOperator(
        task_id="create_user_purchase_table",
        sql="""
            CREATE TABLE IF NOT EXISTS user_purchase (
            invoice_number varchar(20),
            stock_code varchar(20),
            detail varchar(1000),
            quantity int,
            inovoice_date timestamp,
            unit_price numeric(8,3),
            customer_id int,
            country varchar(20);
          """
    )
