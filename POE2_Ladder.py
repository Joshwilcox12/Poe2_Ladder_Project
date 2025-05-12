from datetime import datetime
import time
import pandas
import requests
import schedule
import psycopg2
import os
from sqlalchemy import create_engine

#coonect to database
conn = psycopg2.connect(
    host ="localhost",
    port = "5432",
    database = "Path of Exile 2 Ladder",
    user = "postgres",
    password = "Codwaw"
)

#create cursor
cur = conn.cursor()





#function to pull data from poe2ladder
def job():
    print("Getting PoE 2 Ladder Daily Info")
    #header for api access
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://pathofexile2.com/ladder/HC%2520Dawn%2520of%2520the%2520Hunt',
        'Accept-Language': 'en-US',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    }
    #getting info
    response = requests.get(
        'https://pathofexile2.com/internal-api/content/game-ladder/id/HC%20Dawn%20of%20the%20Hunt',
        headers=headers,
    )
    #connection success, grab the lader info after pulling it as json file and the correct dictionary part
    if response.status_code == 200:
        ladder = response.json()
        ladder_info = ladder['context']['ladder']['entries']
        #make the data look pretty using pandas aka like a csv
        df = pandas.json_normalize(ladder_info)
        #replacing some header names to be better
        df.columns = [col.replace("character.", "") for col in df.columns]
        df.columns = [col.replace("account.","account_") for col in df.columns]
        player_list = df["account_name"].tolist()
        #creating a date to name the files with to track which file is which date
        datestamp = datetime.now().date()
        df["snapshot_date"] = datestamp # optional: add time to dataframe
        #convert it to csv file and save it, should make work on actuall ysaving at a location I want?
        df.to_csv(f"poe2_ladder_data/poe2_ladder_{datestamp}.csv", index=False, encoding='utf-8-sig')
        file_name = f"poe2_ladder_{datestamp}.csv"
        print(file_name)
        return player_list

    else:
        print(f"Error: Failed to get data {response.status_code}")



#now that the data is saved on in the folder as csv, also upload it to the database
def uploadcsv():
    datestamp = datetime.now().date()
    file_name = f"poe2_ladder_{datestamp}.csv"
    #look at csv
    df = pandas.read_csv(f'C:/Users/Josh/Desktop/PycharmProjects/PythonProject/poe2_ladder_data/{file_name}')
    #create connection with sqlalchemy
    engine = create_engine('postgresql+psycopg2://postgres:Codwaw@localhost:5432/Path of Exile 2 Ladder')
    #upload csv to database
    df.to_sql('hc_dawn_of_the_hunt', engine, if_exists ='append', index = False)


def main():
   job()
   uploadcsv()

main()