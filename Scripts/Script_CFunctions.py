from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage
import os
import subprocess
import requests
import random
import pandas as pd
from google.cloud import bigquery
import functions_framework
from datetime import datetime
import time

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def cloud_function(cloud_event):


    project_id = 'proyecto'
    region = 'region'


    job_client = dataproc.JobControllerClient(client_options={
        'api_endpoint': '{}-dataproc.googleapis.com:443'.format(region)
    })


    cluster_name = 'nombrecluster'


    job = {
        'placement': {
            'cluster_name': cluster_name
        },
        'pyspark_job': {
            'main_python_file_uri': 'gs://direccion_del/script.py'
        }
    }

    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job})
    response = operation.result()

    # You can log job status
    print('Job finished successfully: {}'.format(response.status.state == dataproc.types.JobStatus.State.DONE))


    return 'Job submitted and cluster deleted successfully'