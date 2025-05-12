
import time
from datetime import datetime

import pandas
import pandas as pd
import requests

import os
datestamp = datetime.now().date()
csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'poe2_ladder_data/poe2_ladder_{datestamp}.csv')
df = pd.read_csv(csv_file_path).head(100)

account_list = df[df['dead'] == False]['account_name'].tolist()
#later I want to try having ladder players be a value from database and be looped through by python to look up each players item listing
print(f"Account List: {account_list}")

def check_auth_response(response, context=""):
    if response.status_code == 403:
        raise RuntimeError(f"403 Forbidden: Likely expired cookies or Cloudflare block in {context}.")
    elif response.status_code == 429:
        raise RuntimeError(f"429 Too Many Requests: Rate-limited in {context}. Try increasing sleep time.")
    elif not response.ok:
        raise RuntimeError(f"{response.status_code} Error in {context}: {response.text[:200]}")
def first_api(ladder_player):

    with open("POESESSID.txt","r") as f:
        poesessid = f.read().strip()
        cookies = {
        'POESESSID': poesessid,
        'cf_clearance': 'sVCZPjgg1t3huhcpw.YVVmjjGp_bt6qTQh_W4Aitf7k-1746258148-1.2.1.1-yVsVdB2qLgHmvk6NSVLY.52W8HFGYFeS.FTUwJrClyPFYmZ3hXW7zzbn1liTNRXNO9VyZA3jkW71.IMUtytLqSiqlG9J6M13H4arHVRwqyOSvYxMR_IKnJyf3W5KQ8J3T_jgimEqRbr1SP.8ICeVcB4uVwtZycXuorchdhtfqzZeiVqD_7apcu.AtCVNtRe8axk5ShXuujajigPWZrpJaLO5tfoE0.q_tgH1jexbfDkB7nsDK80JczfdZNi1k9re2t7nIlYmilUvr8awXJalVdaMeCz05PMRHva90kjanwGvIZhXZaphNI.L9w9X8v52_DcAOzCGhLS18KUnXf8MBuNvnUYV3dKpfRxFRjEkEDsl7aQc4YxyyK0sW5mvfucu',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.pathofexile.com',
            'priority': 'u=1, i',
            'referer': 'https://www.pathofexile.com/trade2/search/poe2/HC%20Dawn%20of%20the%20Hunt',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"135.0.7049.115"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }



        json_data = {
            'query': {
                'status': {
                    'option': 'any',
                },
                'stats': [
                    {
                        'type': 'and',
                        'filters': [],
                    },
                ],
                'filters': {
                    'trade_filters': {
                        'filters': {
                            'account': {
                                'input': ladder_player,
                            },
                        },
                    },
                },
            },
            'sort': {
                'price': 'asc',
            },
        }

        response = requests.post(
            'https://www.pathofexile.com/api/trade2/search/poe2/HC%20Dawn%20of%20the%20Hunt',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        check_auth_response(response, context=f"first_api for {ladder_player}")
        listings = response.json()
        listings_query_id = listings['id']
        listings_id = listings['result']
        return listings_query_id, listings_id






def value_extract_requirement(item):
    item_list = item
    for entry in item_list:
        item_data = entry.get('item', {})
        for req in item_data.get('requirements', []):
            dic_name = req.get("name", "").strip().replace(" ", "_").replace('[', '').replace(']', '').split("|")[0]
            item_data[f'requirements_{dic_name}'] = req['values'][0][0]


    return item_list



def value_extract_properties(item):
    MAX_PROPERTIES = 6
    for entry in item:
        item_data = entry.get('item', {})
        for i in range(1, MAX_PROPERTIES + 1):
            item_data.setdefault(f'property_{i}',None)
        key_num = 1
        for prop in item_data.get('properties', []):
            if '|' in prop['name']:
                name = prop['name'].replace('[', '').replace(']', '').split('|')[1]
            else:
                name = prop['name'].replace('[', '').replace(']', '')

            if prop.get('values'):

                values = prop['values'][0][0]
            else:
                values = None
            item_data[f'property_{key_num}'] = f'{name}:{values}'
            key_num += 1

def value_extract_explicit_mod(item):
    for entry in item:
        item_data = entry.get('item', {})

        # Always create 6 empty mod fields
        for i in range(1, 7):
            item_data[f"explicit_mod{i}"] = None

        # If there are mods, fill in up to 6
        explicit_mods = item_data.get('explicitMods', [])
        for idx, mod in enumerate(explicit_mods[:6], start=1):
            mods = mod.split()
            cleaned_values = []
            for value in mods:
                clean_value = value.replace('[', '').replace(']', '')
                if '|' in clean_value:
                    clean_value = clean_value.split('|')[1]
                cleaned_values.append(clean_value)
            result = ' '.join(cleaned_values)
            item_data[f"explicit_mod{idx}"] = result


def value_extract_implicit_mod(item):
    for entry in item:
        item_data = entry.get('item', {})

        for i in range(1,4):
            item_data[f"implicit_Mods{i}"] = None

        implicit_mods = item_data.get('implicitMods',[])
        for idx, mod in enumerate(implicit_mods[:3], start=1):
            mods = mod.split()
            cleaned_values = []
            for value in mods:
                clean_value = value.replace('[', '').replace(']', '')
                if '|' in clean_value:
                    clean_value = clean_value.split('|')[1]
                cleaned_values.append(clean_value)
            result = ' '.join(cleaned_values)
            item_data[f"implicit_Mods{idx}"] = result



def second_api(query_id, item_list_id):
    cookies = {
        'cf_clearance': 'your_cf_clearance_here',  # Replace with your actual clearance
        'POESESSID': 'your_session_id_here',  # Replace with your actual session ID
    }

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.115 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'query': query_id,
        'realm': 'poe2',
    }

    all_chunks = []
    chunk_size = 10

    for i in range(0, len(item_list_id), chunk_size):
        chunk = item_list_id[i:i + chunk_size]
        combined_list_id = ','.join(chunk)

        response = requests.get(
            url=f'https://www.pathofexile.com/api/trade2/fetch/{combined_list_id}',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        check_auth_response(response, context=f"second_api chunk {i}-{i + chunk_size}")
        if response.status_code == 200:
            player_listings = response.json()
            item_values = player_listings['result']
            value_extract_requirement(item_values)
            value_extract_properties(item_values)
            value_extract_explicit_mod(item_values)
            value_extract_implicit_mod(item_values)
            df = pd.json_normalize(item_values)
            all_chunks.append(df)
        else:
            print(f"Chunk {i}-{i + chunk_size}: Error {response.status_code}")

        time.sleep(5)  # Sleep to avoid rate limits

    # Combine and export the results
    if all_chunks:
        full_df = pd.concat(all_chunks, ignore_index=True)

        return full_df
    else:
        return None


# Main function that iterates through each player in the account_list
def main():
    print(f"{datestamp} Top 100 player Item Listings")
    all_players_df = []
    if not account_list:
        print("No players to process in the account list.")

        return  # Exit early if account_list is empty

    for player in account_list:

        print(f"Processing player {player}...")
        query_id, item_list_id = first_api(player)
        player_df = second_api(query_id, item_list_id)
        if player_df is not None:
           all_players_df.append(player_df)
        time.sleep(1)
    if all_players_df:
       final_df = pd.concat(all_players_df, ignore_index=True)
       final_df = final_df[["id", "listing.indexed", "listing.stash.name", "listing.account.name",
                           "listing.price.type", "listing.price.amount", "listing.price.currency",
                           "item.realm", "item.league", "item.id", "item.name", "item.typeLine",
                           "item.baseType", "item.rarity", "item.ilvl", "item.identified",
                            "item.requirements_Level", "item.requirements_Strength",
                             "item.requirements_Dexterity","item.requirements_Intelligence","item.implicitMods",
                            "item.implicit_Mods1", "item.implicit_Mods2", "item.implicit_Mods3", "item.explicitMods", "item.explicit_mod1",
                             "item.explicit_mod2", "item.explicit_mod3", "item.explicit_mod4", "item.explicit_mod5", "item.explicit_mod6",
                              "item.corrupted", "item.sockets", "item.grantedSkills","item.property_1","item.property_2"
                             ,"item.property_3","item.property_4","item.property_5","item.property_6"]].rename(columns={
                            "listing.indexed": "indexed_at",
                            "listing.stash.name": "stash_name",
                            "listing.account.name": "account_name",
                            "listing.price.type": "price_type",
                            "listing.price.amount": "price_amount",
                            "listing.price.currency": "price_currency",
                            "item.realm": "realm",
                            "item.league": "league",
                            "item.id": "item_id",
                            "item.name": "item_name",
                            "item.typeLine": "type_line",
                            "item.baseType": "base_type",
                            "item.rarity": "rarity",
                            "item.ilvl": "item_level",
                            "item.identified": "identified",
                            "item.property_1": "properties1",
                            "item.property_2": "properties2",
                            "item.property_3": "properties3",
                            "item.property_4": "properties4",
                            "item.property_5": "properties5",
                            "item.property_6": "properties6",
                            "item.requirements_Level": "level_requirements",
                            "item.requirements_Strength": "strength_requirements",
                            "item.requirements_Dexterity": "dexterity_requirements",
                            "item.requirements_Intelligence": "intelligence_requirements",
                            "item.explicit_mod1": "explicit_mod1",
                            "item.explicit_mod2": "explicit_mod2",
                            "item.explicit_mod3": "explicit_mod3",
                            "item.explicit_mod4": "explicit_mod4",
                            "item.explicit_mod5": "explicit_mod5",
                            "item.explicit_mod6": "explicit_mod6",
                            "item.implicitMods": "implicit_mods",
                            "item.implicit_Mods1" :"implicit_mods1",
                            "item.implicit_Mods2":"implicit_mods2",
                            "item.implicit_Mods3":"implicit_mods3",
                            "item.corrupted": "corrupted",
                            "item.sockets": "num_sockets",
                            "item.grantedSkills": "granted_skills"
})

       final_df.to_csv(f"player_listings/all_players_listings_{datestamp}.csv", index=False, encoding='utf-8-sig')
       print("Saved combined CSV.")


if __name__ == "__main__":
    main()  # This will start the process when the script is run