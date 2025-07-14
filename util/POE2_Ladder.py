from datetime import datetime
from datetime import date
import pandas as pd
import requests
import os


# #coonect to database
# with open("db_creds.txt") as f:
#     host, port, db, user, password = [line.strip() for line in f]

# conn = psycopg2.connect(
#     host=host,
#     port=port,
#     database=db,
#     user=user,
#     password=password
# )
# #create cursor
# cur = conn.cursor()

leagues = ["Dawn%2520of%2520the%2520Hunt","HC%2520Dawn%2520of%2520the%2520Hunt","SSF%2520Dawn%2520of%2520the%2520Hunt","HC%2520SSF%2520Dawn%2520of%2520the%2520Hunt"]
date = date.today()



#function to pull data from poe2ladder
def ladder_api(ladder):
    print(f"Getting Daily {ladder} Info")
    #header for api access
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': f"https://pathofexile2.com/ladder/{ladder}",
        'Accept-Language': 'en-US',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    }
    #getting info
    url =  f"https://pathofexile2.com/internal-api/content/game-ladder/id/{ladder}"
    return requests.get(url,headers=headers)



def league_info(league_name):
    league_list = []

    for league in league_name:
        response = ladder_api(league)
        if response.status_code == 200:
            ladder = response.json()
            ladder_info = ladder['context']['ladder']['entries']
            df = pd.json_normalize(ladder_info)

            df.columns = [col.replace("character.", "") for col in df.columns]
            df.columns = [col.replace("account.","account_") for col in df.columns]

            class_mapping = {
                'Monk2': 'invoker',
                'Monk3': 'acolyte of chayula',
                'Ranger1': 'deadeye',
                'Ranger3': 'path finder',
                'Warrior1': 'titan',
                'Warrior2': 'warbringer',
                'Warrior3': 'smith of kitava',
                'Witch1': 'infernalist',
                'Witch2': 'bloodmage',
                'Witch3': 'lich',
                'Sorceress1': 'stormweaver',
                'Sorceress2': 'chronomancer',
                'Huntress1': 'amazon',
                'Huntress3': 'ritualist',
                'Mercenary1': 'tactician',
                'Mercenary2': 'witchhunter',
                'Mercenary3': 'gemling legionnaire',
            }

            df['class'] = df['class'].replace(class_mapping)

            datestamp = datetime.now().date()
            df["snapshot_date"] = datestamp

            
            league_dict = {league: df}
            league_list.append(league_dict)

        else:
            print(f"Error: Failed to get data {response.status_code}")

    return league_list





def update_keys(league_data):
#   all_dfs = []
#   directory = "C:/Users/Josh/Desktop/PycharmProjects/PythonProject/poe2_ladder_data"
  for i, league in enumerate(league_data):
    update_league ={}
    for name, data in league.items():
       update_name = name.replace("%2520","_").lower()
       update_league[update_name] = data 
       print(update_name)
    league_data[i] = update_league
  return league_data
#   for league_folders in os.listdir(directory):
#      for league in league_data:
#         for key in league:
#            if key == league_folders:
#               output_path = os.path.join(directory, league_folders, f"{key}_ladder_data_{date}.csv")
#               df = league[key]
#               df.to_csv(output_path, index=False)
#               all_dfs.append(df)
#   print(all_dfs[0].keys())
#   return all_dfs

response = league_info(leagues)
def final():
  
   value = update_keys(response)
   return value

final()














