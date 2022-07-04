import os
import bigquery
import pandas as pd

def client():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bigquery_service_acct.json'
    client = bigquery.Client()
    return client

def bigquery_dataset(project_id, dataset_id):
    # 'sql-for-bigquery.github_source_data'
    source_dataset_id_full = "{}.{}".format(project_id, dataset_id)
    source_dataset = bigquery.Dataset(source_dataset_id_full)
    return source_dataset

def construct_dataset_name(project_id, dataset_id, table_id):
    return "`{}.{}.{}`".format(project_id, dataset_id, table_id)

def config_pandas_view():
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 50)
    pd.set_option('display.min_rows', 500)
    pd.set_option('display.max_colwidth', 150)
    pd.set_option('display.width', 90)
    pd.set_option('expand_frame_repr', True)
    pd.options.display.float_format ="{:,.2f}".format