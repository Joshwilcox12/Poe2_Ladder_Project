import sys
import os
import pandas as pd
import io
from datetime import date
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from util.POE2_Ladder import final
from google.cloud import storage



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Josh/Desktop/PycharmProjects/PythonProject/gpc_info/gcs_key.json"


todays_date = date.today()
bucket_name = "poe2_bucket-1"
destination = "Ladder_Info/"
folder_list = ["dawn_of_the_hunt", "hc_dawn_of_the_hunt", "ssf_dawn_of_the_hunt", "hc_ssf_dawn_of_the_hunt"]
ladder_list = final()





def upload_blob_from_memory(bucket_name, contents, destination_blob_name):


    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

   
    
def loop_upload():
   for league in ladder_list:
       for key, df in league.items():
          if key in folder_list:
                   csv_buffer = io.StringIO()
                   df.to_csv(csv_buffer, index=False)
                   content = csv_buffer.getvalue()
                   blob_path = f"{destination}{key}_{todays_date}.csv"
                   upload_blob_from_memory(bucket_name,content,blob_path)


loop_upload()
#need to have google cloud credentials to upload