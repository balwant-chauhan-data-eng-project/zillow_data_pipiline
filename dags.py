import importlib.util
import json
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

import os



s3_bucket='cleaned-data-zone-csv-bucket-from-lambda'
file_key='transformed_data/04_09_2024.csv'

module_path = r'/home/ubuntu/airflow/zillow_data.py'

current_time = datetime.now()
current_time_in_string = current_time.strftime("%m_%d_%Y_%H_%M_%S")
s3_bucket='cleaned-data-zone-csv-bucket-from-lambda'
file_key=f'transformed_data/{current_time_in_string}'

def function_for_extracting_data(**kwargs):
    spec = importlib.util.spec_from_file_location('zillow_code', module_path)
    zillow_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(zillow_code) 
    zillow_code = zillow_code.generate_data()

    date_in_string = kwargs['date_string']

    output_directory = '/home/ubuntu/raw_data/'
    os.makedirs(output_directory, exist_ok=True)

    file_name = f'raw_data_{current_time_in_string}.json'
    output_file_path = os.path.join(output_directory, file_name)
     
     


    with open(output_file_path, 'w') as output_file:
        json.dump(zillow_code, output_file)

    output_list = [output_file_path, file_name]
    return output_list


def upload_to_s3(**kwargs):
    ti = kwargs['ti']
    output_file_path = ti.xcom_pull(task_ids='tsk_extract_zillow_data_var')[0]
    s3_hook = S3Hook(aws_conn_id='aws_con_id')  # Specify your AWS connection ID here
    s3_bucket = 'endtoendyoutube-ym-bucket-1'
    s3_key = f'raw_data/{current_time_in_string}.json'
    s3_hook.load_file(filename=output_file_path, key=s3_key, bucket_name=s3_bucket, replace=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 2),
    'email': ['balwantc070@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

with DAG('zillow_analytics_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_zillow_data_var = PythonOperator(
        task_id='tsk_extract_zillow_data_var',
        python_callable=function_for_extracting_data,
        op_kwargs={'date_string': current_time_in_string}
    )

    upload_to_s3 = PythonOperator(
        task_id='task_upload_to_s3',
        python_callable=upload_to_s3,
        provide_context=True
    )

    transfer_s3_to_redshift = S3ToRedshiftOperator(
        task_id="tsk_transfer_s3_to_redshift",
        aws_conn_id='aws_con_id',
        redshift_conn_id='conn_id_redshift',
        s3_bucket=s3_bucket,
        s3_key=file_key,
        schema="PUBLIC",
        table="zillowdata",
        copy_options=["csv IGNOREHEADER 1"],
    )











    extract_zillow_data_var >> upload_to_s3  >>  transfer_s3_to_redshift
