from google.cloud import bigquery

client = bigquery.Client()

# Define el nombre de tu dataset y tabla en BigQuery
dataset_id = 'datosMaps'
table_id = 'maps_api'

# Crea una referencia a la tabla
table_ref = client.dataset(dataset_id).table(table_id)

# Crea una consulta SQL para eliminar los registros duplicados
sql = f"""
    CREATE OR REPLACE TABLE `{dataset_id}.{table_id}`
    AS SELECT * EXCEPT(row_num)
    FROM (
        SELECT
        *, ROW_NUMBER() OVER (PARTITION BY author_name, text, rating, time ORDER BY time DESC) as row_num
        FROM `{dataset_id}.{table_id}`
    )
    WHERE row_num = 1
"""

# Ejecuta la consulta
query_job = client.query(sql)
query_job.result()
