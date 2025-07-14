import time
from datetime import datetime

import pandas
import pandas as pd
import requests

import os
# datestamp = datetime.now().date()
# csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'poe2_ladder_{datestamp}.csv')
# df = pd.read_csv(csv_file_path).head(100)
#
# account_list = df[df['dead'] == False]['account_name'].tolist()
# #later I want to try having ladder players be a value from database and be looped through by python to look up each players item listing
#
#
# def check_auth_response(response, context=""):
#     if response.status_code == 403:
#         raise RuntimeError(f"403 Forbidden: Likely expired cookies or Cloudflare block in {context}.")
#     elif response.status_code == 429:
#         raise RuntimeError(f"429 Too Many Requests: Rate-limited in {context}. Try increasing sleep time.")
#     elif not response.ok:
#         raise RuntimeError(f"{response.status_code} Error in {context}: {response.text[:200]}")
# def first_api(ladder_player):
#     cookies = {
#     'POESESSID': '80e3488108332c7f7b59ead4266233b5',
#     'cf_clearance': 'sVCZPjgg1t3huhcpw.YVVmjjGp_bt6qTQh_W4Aitf7k-1746258148-1.2.1.1-yVsVdB2qLgHmvk6NSVLY.52W8HFGYFeS.FTUwJrClyPFYmZ3hXW7zzbn1liTNRXNO9VyZA3jkW71.IMUtytLqSiqlG9J6M13H4arHVRwqyOSvYxMR_IKnJyf3W5KQ8J3T_jgimEqRbr1SP.8ICeVcB4uVwtZycXuorchdhtfqzZeiVqD_7apcu.AtCVNtRe8axk5ShXuujajigPWZrpJaLO5tfoE0.q_tgH1jexbfDkB7nsDK80JczfdZNi1k9re2t7nIlYmilUvr8awXJalVdaMeCz05PMRHva90kjanwGvIZhXZaphNI.L9w9X8v52_DcAOzCGhLS18KUnXf8MBuNvnUYV3dKpfRxFRjEkEDsl7aQc4YxyyK0sW5mvfucu',
#     }
#
#     headers = {
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
#         'content-type': 'application/json',
#         'origin': 'https://www.pathofexile.com',
#         'priority': 'u=1, i',
#         'referer': 'https://www.pathofexile.com/trade2/search/poe2/HC%20Dawn%20of%20the%20Hunt',
#         'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
#         'sec-ch-ua-arch': '"x86"',
#         'sec-ch-ua-bitness': '"64"',
#         'sec-ch-ua-full-version': '"135.0.7049.115"',
#         'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-model': '""',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-ch-ua-platform-version': '"10.0.0"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest',
#         # 'cookie': 'POESESSID=80e3488108332c7f7b59ead4266233b5; cf_clearance=sVCZPjgg1t3huhcpw.YVVmjjGp_bt6qTQh_W4Aitf7k-1746258148-1.2.1.1-yVsVdB2qLgHmvk6NSVLY.52W8HFGYFeS.FTUwJrClyPFYmZ3hXW7zzbn1liTNRXNO9VyZA3jkW71.IMUtytLqSiqlG9J6M13H4arHVRwqyOSvYxMR_IKnJyf3W5KQ8J3T_jgimEqRbr1SP.8ICeVcB4uVwtZycXuorchdhtfqzZeiVqD_7apcu.AtCVNtRe8axk5ShXuujajigPWZrpJaLO5tfoE0.q_tgH1jexbfDkB7nsDK80JczfdZNi1k9re2t7nIlYmilUvr8awXJalVdaMeCz05PMRHva90kjanwGvIZhXZaphNI.L9w9X8v52_DcAOzCGhLS18KUnXf8MBuNvnUYV3dKpfRxFRjEkEDsl7aQc4YxyyK0sW5mvfucu',
#     }
#
#
#
#     json_data = {
#         'query': {
#             'status': {
#                 'option': 'any',
#             },
#             'stats': [
#                 {
#                     'type': 'and',
#                     'filters': [],
#                 },
#             ],
#             'filters': {
#                 'trade_filters': {
#                     'filters': {
#                         'account': {
#                             'input': ladder_player,
#                         },
#                     },
#                 },
#             },
#         },
#         'sort': {
#             'price': 'asc',
#         },
#     }
#
#     response = requests.post(
#         'https://www.pathofexile.com/api/trade2/search/poe2/HC%20Dawn%20of%20the%20Hunt',
#         cookies=cookies,
#         headers=headers,
#         json=json_data,
#     )
#     check_auth_response(response, context=f"first_api for {ladder_player}")
#     listings = response.json()
#     listings_query_id = listings['id']
#     listings_id = listings['result']
#     # combined_list_id = ','.join(listings_id)
#     return listings_query_id, listings_id
#
# #next step to try: maybe clean up the code above so more readable and know what is happening
# #Then try to convert the list to a string of each id then concat to end of the search url for the other api?
#
#
#
#
#
#
# def second_api(query_id, item_list_id):
#     cookies = {
#         'cf_clearance': 'your_cf_clearance_here',  # Replace with your actual clearance
#         'POESESSID': 'your_session_id_here',  # Replace with your actual session ID
#     }
#
#     headers = {
#         'accept': '*/*',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.115 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest',
#     }
#
#     params = {
#         'query': query_id,
#         'realm': 'poe2',
#     }
#
#     all_chunks = []
#     chunk_size = 10
#
#     for i in range(0, len(item_list_id), chunk_size):
#         chunk = item_list_id[i:i + chunk_size]
#         combined_list_id = ','.join(chunk)
#
#         response = requests.get(
#             url=f'https://www.pathofexile.com/api/trade2/fetch/{combined_list_id}',
#             params=params,
#             cookies=cookies,
#             headers=headers,
#         )
#         check_auth_response(response, context=f"second_api chunk {i}-{i + chunk_size}")
#         if response.status_code == 200:
#             player_listings = response.json()
#             results = player_listings['result']
#
#             all_chunks.append(results)
#         else:
#             print(f"Chunk {i}-{i + chunk_size}: Error {response.status_code}")
#
#         time.sleep(2)  # Sleep to avoid rate limits
#
#     # Combine and export the results
#     if all_chunks:
#
#         print(type(all_chunks))
#         print(all_chunks[0])
#     else:
#         return None



# query_id, item_list_id = first_api('interein#1284')
# second_api(query_id, item_list_id)


ten_items = [{'id': 'bec05862e49464661e2e5ad3a345a6f36004f9bd6cc3c12594ea6a9855865d2e', 'listing': {'method': 'psapi', 'indexed': '2025-04-23T03:48:14Z', 'stash': {'name': '~b/o 1 divine', 'x': 22, 'y': 5}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 독사의 상처 루비(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 23, 상단 6)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL1J1YnlKZXdlbCIsInciOjEsImgiOjEsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/8ef1a48ec8/RubyJewel.png', 'league': 'HC Dawn of the Hunt', 'id': 'bec05862e49464661e2e5ad3a345a6f36004f9bd6cc3c12594ea6a9855865d2e', 'name': 'Viper Wound', 'typeLine': 'Ruby', 'baseType': 'Ruby', 'rarity': 'Rare', 'ilvl': 82, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': '[Jewel]', 'values': [], 'displayMode': 0}], 'explicitMods': ['[Minion|Minions] have 8% increased maximum Life', '13% increased [Stun] Buildup', '14% increased [Totem|Totem] Placement speed', '18% increased [Defences] from Equipped [Shield]'], 'descrText': 'Place into an allocated Jewel Socket on the Passive Skill Tree. Right click to remove from the Socket.', 'frameType': 2, 'extended': {'mods': {'explicit': [{'name': 'of Ancestry', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3374165039', 'min': '10', 'max': '20'}]}, {'name': 'Fortuitous', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_770672621', 'min': '5', 'max': '15'}]}, {'name': 'Shielding', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_145497481', 'min': '18', 'max': '32'}]}, {'name': 'of Stunning', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_239367161', 'min': '10', 'max': '20'}]}]}, 'hashes': {'explicit': [['explicit.stat_770672621', [1]], ['explicit.stat_239367161', [3]], ['explicit.stat_3374165039', [0]], ['explicit.stat_145497481', [2]]]}}}}, {'id': 'e531642040dd72ba089c6e811d1adf8f57efa49526b9431b6bdccb7ecc266c2e', 'listing': {'method': 'psapi', 'indexed': '2025-04-25T22:57:50Z', 'stash': {'name': '~b/o 1 divine', 'x': 9, 'y': 0}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 혼란 발굽 모래맹세 샌들(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 10, 상단 1)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 2, 'h': 2, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9Cb290cy9CYXNldHlwZXMvQm9vdHNJbnQwNSIsInciOjIsImgiOjIsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/2f27d465e1/BootsInt05.png', 'league': 'HC Dawn of the Hunt', 'id': 'e531642040dd72ba089c6e811d1adf8f57efa49526b9431b6bdccb7ecc266c2e', 'name': 'Anarchy Hoof', 'typeLine': 'Sandsworn Sandals', 'baseType': 'Sandsworn Sandals', 'rarity': 'Rare', 'ilvl': 78, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': 'Boots', 'values': [], 'displayMode': 0}, {'name': '[EnergyShield|Energy Shield]', 'values': [['79', 1]], 'displayMode': 0, 'type': 18}], 'requirements': [{'name': 'Level', 'values': [['75', 0]], 'displayMode': 0, 'type': 62}, {'name': '[Intelligence|Int]', 'values': [['131', 0]], 'displayMode': 1, 'type': 65}], 'explicitMods': ['30% increased Movement Speed', '6% increased [EnergyShield|Energy Shield]', '+97 to maximum Mana', '+30 to [Intelligence|Intelligence]', '+24% to [Resistances|Fire Resistance]', '+13 to [StunThreshold|Stun Threshold]'], 'frameType': 2, 'extended': {'es': 95, 'es_aug': True, 'mods': {'explicit': [{'name': 'of the Kiln', 'tier': 'S4', 'level': 36, 'magnitudes': [{'hash': 'explicit.stat_3372524247', 'min': '21', 'max': '25'}]}, {'name': "Cheetah's", 'tier': 'P5', 'level': 70, 'magnitudes': [{'hash': 'explicit.stat_2250533757', 'min': '30', 'max': '30'}]}, {'name': 'Gentian', 'tier': 'P8', 'level': 43, 'magnitudes': [{'hash': 'explicit.stat_1050105434', 'min': '90', 'max': '104'}]}, {'name': "Pixie's", 'tier': 'P1', 'level': 10, 'magnitudes': [{'hash': 'explicit.stat_4015621042', 'min': '6', 'max': '13'}, {'hash': 'explicit.stat_915769802', 'min': '8', 'max': '13'}]}, {'name': 'of the Savant', 'tier': 'S7', 'level': 66, 'magnitudes': [{'hash': 'explicit.stat_328541901', 'min': '28', 'max': '30'}]}]}, 'hashes': {'explicit': [['explicit.stat_2250533757', [1]], ['explicit.stat_4015621042', [3]], ['explicit.stat_1050105434', [2]], ['explicit.stat_328541901', [4]], ['explicit.stat_3372524247', [0]], ['explicit.stat_915769802', [3]]]}}}}, {'id': '0beb0b5d966e36d8551844000f3894acbd135ccb1875788d0715b0ddb2aa8abd', 'listing': {'method': 'psapi', 'indexed': '2025-04-27T09:09:59Z', 'stash': {'name': '~b/o 1 divine', 'x': 23, 'y': 1}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 독사의 중지 에메랄드(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 24, 상단 2)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL0VtZXJhbGRKZXdlbCIsInciOjEsImgiOjEsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/0df7b1d23b/EmeraldJewel.png', 'league': 'HC Dawn of the Hunt', 'id': '0beb0b5d966e36d8551844000f3894acbd135ccb1875788d0715b0ddb2aa8abd', 'name': 'Viper Pause', 'typeLine': 'Emerald', 'baseType': 'Emerald', 'rarity': 'Rare', 'ilvl': 81, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': '[Jewel]', 'values': [], 'displayMode': 0}], 'explicitMods': ['15% increased [Evasion|Evasion Rating]', '19% increased chance to [Shock]', '8% increased [Attack] Damage', '11% increased [Pinned|Pin] Buildup'], 'descrText': 'Place into an allocated Jewel Socket on the Passive Skill Tree. Right click to remove from the Socket.', 'frameType': 2, 'extended': {'mods': {'explicit': [{'name': 'Combat', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_2843214518', 'min': '5', 'max': '15'}]}, {'name': 'of Shocking', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_293638271', 'min': '10', 'max': '20'}]}, {'name': 'Evasive', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_2106365538', 'min': '10', 'max': '20'}]}, {'name': 'of Pinning', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3473929743', 'min': '10', 'max': '20'}]}]}, 'hashes': {'explicit': [['explicit.stat_2106365538', [2]], ['explicit.stat_293638271', [1]], ['explicit.stat_2843214518', [0]], ['explicit.stat_3473929743', [3]]]}}}}, {'id': 'a32a0abaa6499ffcb4a9276af6c7d197d71afca8ce0f9f12cc589d2a79f61053', 'listing': {'method': 'psapi', 'indexed': '2025-04-25T23:49:51Z', 'stash': {'name': '~b/o 1 divine', 'x': 23, 'y': 9}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 빛나는 돌 사파이어(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 24, 상단 10)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL1NhcHBoaXJlSmV3ZWwiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MSwicmVhbG0iOiJwb2UyIn1d/976a8c1642/SapphireJewel.png', 'league': 'HC Dawn of the Hunt', 'id': 'a32a0abaa6499ffcb4a9276af6c7d197d71afca8ce0f9f12cc589d2a79f61053', 'name': 'Luminous Stone', 'typeLine': 'Sapphire', 'baseType': 'Sapphire', 'rarity': 'Rare', 'ilvl': 80, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': '[Jewel]', 'values': [], 'displayMode': 0}], 'explicitMods': ['11% increased [Chaos] Damage', '11% increased [CriticalDamageBonus|Critical Spell Damage Bonus]', '16% increased [ESRechargeRate|Energy Shield Recharge Rate]', '10% increased Duration of [DamagingAilments|Damaging Ailments] on Enemies'], 'descrText': 'Place into an allocated Jewel Socket on the Passive Skill Tree. Right click to remove from the Socket.', 'frameType': 2, 'extended': {'mods': {'explicit': [{'name': 'of Unmaking', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_274716455', 'min': '10', 'max': '20'}]}, {'name': 'of Suffusion', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_1829102168', 'min': '5', 'max': '10'}]}, {'name': 'Chaotic', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_736967255', 'min': '6', 'max': '12'}]}, {'name': 'Fevered', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_2339757871', 'min': '10', 'max': '20'}]}]}, 'hashes': {'explicit': [['explicit.stat_736967255', [2]], ['explicit.stat_274716455', [0]], ['explicit.stat_2339757871', [3]], ['explicit.stat_1829102168', [1]]]}}}}, {'id': 'f9884b7ee0315f841b33c11debefc60509901c56beaa2859f707c9d6d36baa2f', 'listing': {'method': 'psapi', 'indexed': '2025-04-30T21:11:09Z', 'stash': {'name': '~b/o 1 divine', 'x': 19, 'y': 21}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 겁쟁이의 유물 사슬 허리띠(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 20, 상단 22)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 2, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQmVsdHMvVW5pcXVlcy9Db3dhcmRzTGVnYWN5IiwidyI6MiwiaCI6MSwic2NhbGUiOjEsInJlYWxtIjoicG9lMiJ9XQ/8fbdb591b3/CowardsLegacy.png', 'league': 'HC Dawn of the Hunt', 'id': 'f9884b7ee0315f841b33c11debefc60509901c56beaa2859f707c9d6d36baa2f', 'name': "Coward's Legacy", 'typeLine': 'Mail Belt', 'baseType': 'Mail Belt', 'rarity': 'Unique', 'ilvl': 81, 'identified': True, 'note': '~price 10 exalted', 'corrupted': True, 'properties': [{'name': 'Belt', 'values': [], 'displayMode': 0}], 'requirements': [{'name': 'Level', 'values': [['40', 0]], 'displayMode': 0, 'type': 62}], 'implicitMods': ['12% reduced [Flask|Flask] Charges used', 'Has 2 [Charm] Slots'], 'explicitMods': ['-12 to [Strength|Strength]', '+20 to [Dexterity|Dexterity]', '30% increased Life and Mana Recovery from [Flask|Flasks]', 'You are considered on [LowLife|Low Life] while at 75% of maximum Life or below instead'], 'flavourText': ['Death is your most important duty.\r', 'Face it, or curse your bloodline for all eternity.'], 'frameType': 3, 'extended': {'mods': {'explicit': [{'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_2310741722', 'min': '30', 'max': '40'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_4080418644', 'min': '-20', 'max': '-10'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3261801346', 'min': '20', 'max': '30'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_356835700', 'min': '75', 'max': '75'}]}], 'implicit': [{'name': '', 'tier': '', 'level': 50, 'magnitudes': [{'hash': 'implicit.stat_644456512', 'min': '15', 'max': '10'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'implicit.stat_1416292992', 'min': '1', 'max': '3'}]}]}, 'hashes': {'explicit': [['explicit.stat_4080418644', [1]], ['explicit.stat_3261801346', [2]], ['explicit.stat_2310741722', [0]], ['explicit.stat_356835700', [3]]], 'implicit': [['implicit.stat_644456512', [0]], ['implicit.stat_1416292992', [1]]]}}}}, {'id': '4865b0b9c6eb5b9bb66bd9e0bc7cfe1d3d52cd4594d701158f4608be881d96cb', 'listing': {'method': 'psapi', 'indexed': '2025-05-01T23:31:02Z', 'stash': {'name': '~b/o 1 divine', 'x': 17, 'y': 20}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 최면의 발굽 모래맹세 샌들(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 18, 상단 21)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 2, 'h': 2, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9Cb290cy9CYXNldHlwZXMvQm9vdHNJbnQwNSIsInciOjIsImgiOjIsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/2f27d465e1/BootsInt05.png', 'league': 'HC Dawn of the Hunt', 'id': '4865b0b9c6eb5b9bb66bd9e0bc7cfe1d3d52cd4594d701158f4608be881d96cb', 'name': 'Hypnotic Hoof', 'typeLine': 'Sandsworn Sandals', 'baseType': 'Sandsworn Sandals', 'rarity': 'Rare', 'ilvl': 80, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': 'Boots', 'values': [], 'displayMode': 0}, {'name': '[EnergyShield|Energy Shield]', 'values': [['75', 0]], 'displayMode': 0, 'type': 18}], 'requirements': [{'name': 'Level', 'values': [['75', 0]], 'displayMode': 0, 'type': 62}, {'name': '[Intelligence|Int]', 'values': [['131', 0]], 'displayMode': 1, 'type': 65}], 'explicitMods': ['30% increased Movement Speed', '+15 to maximum Life', '+102 to maximum Mana', '9% increased [ItemRarity|Rarity of Items] found', '+35% to [Resistances|Lightning Resistance]', '5.4 Life Regeneration per second'], 'frameType': 2, 'extended': {'es': 90, 'es_aug': True, 'mods': {'explicit': [{'name': "Cheetah's", 'tier': 'P5', 'level': 70, 'magnitudes': [{'hash': 'explicit.stat_2250533757', 'min': '30', 'max': '30'}]}, {'name': 'of Plunder', 'tier': 'S1', 'level': 3, 'magnitudes': [{'hash': 'explicit.stat_3917489142', 'min': '6', 'max': '10'}]}, {'name': 'Gentian', 'tier': 'P8', 'level': 43, 'magnitudes': [{'hash': 'explicit.stat_1050105434', 'min': '90', 'max': '104'}]}, {'name': 'of the Starfish', 'tier': 'S4', 'level': 17, 'magnitudes': [{'hash': 'explicit.stat_3325883026', 'min': '4.1', 'max': '6'}]}, {'name': 'of the Maelstrom', 'tier': 'S6', 'level': 60, 'magnitudes': [{'hash': 'explicit.stat_1671376347', 'min': '31', 'max': '35'}]}, {'name': 'Hale', 'tier': 'P1', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3299347043', 'min': '10', 'max': '19'}]}]}, 'hashes': {'explicit': [['explicit.stat_2250533757', [0]], ['explicit.stat_3299347043', [5]], ['explicit.stat_1050105434', [2]], ['explicit.stat_3917489142', [1]], ['explicit.stat_1671376347', [4]], ['explicit.stat_3325883026', [3]]]}}}}, {'id': '11c19ed08d7436722f0dca6b0521dd873ad17e49f1fca7934f606c389d31bd7c', 'listing': {'method': 'psapi', 'indexed': '2025-04-22T11:18:41Z', 'stash': {'name': '~b/o 1 divine', 'x': 22, 'y': 3}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 대재앙 편린 루비(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 23, 상단 4)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL1J1YnlKZXdlbCIsInciOjEsImgiOjEsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/8ef1a48ec8/RubyJewel.png', 'league': 'HC Dawn of the Hunt', 'id': '11c19ed08d7436722f0dca6b0521dd873ad17e49f1fca7934f606c389d31bd7c', 'name': 'Cataclysm Sliver', 'typeLine': 'Ruby', 'baseType': 'Ruby', 'rarity': 'Rare', 'ilvl': 80, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': '[Jewel]', 'values': [], 'displayMode': 0}], 'explicitMods': ['14% increased [Melee] Damage', '[Minion|Minions] have 7% increased Area of Effect', '12% increased [Warcry|Warcry] Speed', '25% increased [Stun|Stun Buildup] with [Mace|Maces]'], 'descrText': 'Place into an allocated Jewel Socket on the Passive Skill Tree. Right click to remove from the Socket.', 'frameType': 2, 'extended': {'mods': {'explicit': [{'name': 'of Lungs', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_1316278494', 'min': '10', 'max': '20'}]}, {'name': 'of Thumping', 'tier': 'S0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_872504239', 'min': '15', 'max': '25'}]}, {'name': 'Clashing', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_1002362373', 'min': '5', 'max': '15'}]}, {'name': 'Companion', 'tier': 'P0', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3811191316', 'min': '5', 'max': '10'}]}]}, 'hashes': {'explicit': [['explicit.stat_1002362373', [2]], ['explicit.stat_3811191316', [3]], ['explicit.stat_1316278494', [0]], ['explicit.stat_872504239', [1]]]}}}}, {'id': '96cec6f298a26e372512d97673d40a4476b21c966847fd54c3c7f1dd3ec90cb8', 'listing': {'method': 'psapi', 'indexed': '2025-05-02T12:59:04Z', 'stash': {'name': '~b/o 1 divine', 'x': 2, 'y': 20}, 'whisper': '@evade_ii 안녕하세요, 10 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 가시나무 칼날 나선 창(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 3, 상단 21)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 10, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 4, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9PbmVIYW5kV2VhcG9ucy9PbmVIYW5kU3BlYXJzLzFIU3BlYXIxMyIsInciOjEsImgiOjQsInNjYWxlIjoxLCJyZWFsbSI6InBvZTIifV0/adad4234d0/1HSpear13.png', 'league': 'HC Dawn of the Hunt', 'id': '96cec6f298a26e372512d97673d40a4476b21c966847fd54c3c7f1dd3ec90cb8', 'name': 'Bramble Edge', 'typeLine': 'Helix Spear', 'baseType': 'Helix Spear', 'rarity': 'Rare', 'ilvl': 82, 'identified': True, 'note': '~price 10 exalted', 'properties': [{'name': '[Spear]', 'values': [], 'displayMode': 0}, {'name': '[Physical] Damage', 'values': [['57-105', 1]], 'displayMode': 0, 'type': 9}, {'name': 'Fire Damage', 'values': [['16-28', 4]], 'displayMode': 0, 'type': 10}, {'name': '[Critical|Critical Hit] Chance', 'values': [['5.00%', 0]], 'displayMode': 0, 'type': 12}, {'name': 'Attacks per Second', 'values': [['1.60', 0]], 'displayMode': 0, 'type': 13}], 'requirements': [{'name': 'Level', 'values': [['65', 0]], 'displayMode': 0, 'type': 62}, {'name': '[Strength|Str]', 'values': [['45', 0]], 'displayMode': 1, 'type': 63}, {'name': '[Dexterity|Dex]', 'values': [['116', 0]], 'displayMode': 1, 'type': 64}], 'grantedSkills': [{'name': 'Grants Skill', 'values': [['Spear Throw', 25]], 'displayMode': 0, 'icon': 'https://web.poecdn.com/gen/image/WzIxLDE0LHsiayI6IjJEQXJ0L1NraWxsSWNvbnMvSHVudHJlc3NJY2VTcGVhciIsInJlYWxtIjoicG9lMiJ9XQ/da079143ea/HuntressIceSpear.png'}], 'explicitMods': ['54% increased [Physical] Damage', 'Adds 16 to 28 [Fire|Fire] Damage', '+448 to [Accuracy|Accuracy] Rating', 'Gain 10 Mana per Enemy Killed', '12% increased [Stun|Stun] Duration'], 'frameType': 2, 'extended': {'dps': 190.4, 'pdps': 155.2, 'edps': 35.2, 'dps_aug': True, 'pdps_aug': True, 'mods': {'explicit': [{'name': 'of Impact', 'tier': 'S1', 'level': 5, 'magnitudes': [{'hash': 'explicit.stat_748522257', 'min': '11', 'max': '13'}]}, {'name': 'Flaming', 'tier': 'P5', 'level': 33, 'magnitudes': [{'hash': 'explicit.stat_709508406', 'min': '14', 'max': '21'}, {'hash': 'explicit.stat_709508406', 'min': '22', 'max': '33'}]}, {'name': 'Serrated', 'tier': 'P2', 'level': 11, 'magnitudes': [{'hash': 'explicit.stat_1509134228', 'min': '50', 'max': '64'}]}, {'name': "Ranger's", 'tier': 'P8', 'level': 63, 'magnitudes': [{'hash': 'explicit.stat_691932474', 'min': '347', 'max': '450'}]}, {'name': 'of Enveloping', 'tier': 'S4', 'level': 34, 'magnitudes': [{'hash': 'explicit.stat_1368271171', 'min': '10', 'max': '14'}]}], 'implicit': [{'name': '', 'tier': '', 'level': 1, 'magnitudes': None}]}, 'hashes': {'explicit': [['explicit.stat_1509134228', [2]], ['explicit.stat_709508406', [1]], ['explicit.stat_691932474', [3]], ['explicit.stat_1368271171', [4]], ['explicit.stat_748522257', [0]]]}}}}, {'id': 'd8eb6801752af497354c3f7907b18c723434520108a89c062d578a79bd41da8c', 'listing': {'method': 'psapi', 'indexed': '2025-05-08T17:45:35Z', 'stash': {'name': '~b/o 1 divine', 'x': 22, 'y': 23}, 'whisper': '@evade_ii 안녕하세요, 15 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 지옥불 죔쇠 판금 허리띠(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 23, 상단 24)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 15, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 2, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQmVsdHMvVW5pcXVlcy9JbmZlcm5vY2xhc3AiLCJ3IjoyLCJoIjoxLCJzY2FsZSI6MSwicmVhbG0iOiJwb2UyIn1d/8b588f973c/Infernoclasp.png', 'league': 'HC Dawn of the Hunt', 'id': 'd8eb6801752af497354c3f7907b18c723434520108a89c062d578a79bd41da8c', 'name': 'Infernoclasp', 'typeLine': 'Plate Belt', 'baseType': 'Plate Belt', 'rarity': 'Unique', 'ilvl': 81, 'identified': True, 'note': '~price 15 exalted', 'corrupted': True, 'properties': [{'name': 'Belt', 'values': [], 'displayMode': 0}], 'requirements': [{'name': 'Level', 'values': [['24', 0]], 'displayMode': 0, 'type': 62}], 'enchantMods': ['+22% to [Resistances|Lightning Resistance]'], 'implicitMods': ['+128 to [Armour]', 'Has 1 [Charm] Slot'], 'explicitMods': ['+148 to [Armour]', '+15 to [Strength|Strength]', '+4% to [MaximumResistances|Maximum Fire Resistance]', '+45% to [Resistances|Fire Resistance]'], 'flavourText': ['Tempered by the forbidden flame.'], 'frameType': 3, 'extended': {'mods': {'explicit': [{'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_4080418644', 'min': '10', 'max': '20'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_809229260', 'min': '100', 'max': '150'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3372524247', 'min': '30', 'max': '50'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_4095671657', 'min': '3', 'max': '5'}]}], 'implicit': [{'name': '', 'tier': '', 'level': 31, 'magnitudes': [{'hash': 'implicit.stat_809229260', 'min': '100', 'max': '140'}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'implicit.stat_1416292992', 'min': '1', 'max': '3'}]}], 'enchant': [{'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'enchant.stat_1671376347', 'min': '20', 'max': '25'}]}]}, 'hashes': {'explicit': [['explicit.stat_809229260', [1]], ['explicit.stat_4080418644', [0]], ['explicit.stat_4095671657', [3]], ['explicit.stat_3372524247', [2]]], 'implicit': [['implicit.stat_809229260', [0]], ['implicit.stat_1416292992', [1]]], 'enchant': [['enchant.stat_1671376347', [0]]]}}}}, {'id': '92968c66ac48e8ec886ae0724c8a55cd643749fb811dd4036ee1d35c829c9ac2', 'listing': {'method': 'psapi', 'indexed': '2025-04-28T11:48:42Z', 'stash': {'name': '~b/o 1 divine', 'x': 23, 'y': 13}, 'whisper': '@evade_ii 안녕하세요, 15 exalted(으)로 올려놓은 HC Dawn of the Hunt 리그의 증오의 갑 목걸이 달의 목걸이(을)를 구매하고 싶습니다 (보관함 탭 "~b/o 1 divine", 위치: 왼쪽 24, 상단 14)', 'account': {'name': 'interein#1284', 'online': {'league': 'HC Dawn of the Hunt'}, 'lastCharacterName': 'evade_ii', 'language': 'ko_KR', 'realm': 'poe2'}, 'price': {'type': '~price', 'amount': 15, 'currency': 'exalted'}}, 'item': {'realm': 'poe2', 'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQW11bGV0cy9CYXNldHlwZXMvTHVuYXJBbXVsZXQiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MSwicmVhbG0iOiJwb2UyIn1d/e0eef02a23/LunarAmulet.png', 'league': 'HC Dawn of the Hunt', 'id': '92968c66ac48e8ec886ae0724c8a55cd643749fb811dd4036ee1d35c829c9ac2', 'name': 'Hate Locket', 'typeLine': 'Lunar Amulet', 'baseType': 'Lunar Amulet', 'rarity': 'Rare', 'ilvl': 82, 'identified': True, 'note': '~price 15 exalted', 'properties': [{'name': 'Amulet', 'values': [], 'displayMode': 0}], 'requirements': [{'name': 'Level', 'values': [['52', 0]], 'displayMode': 0, 'type': 62}], 'implicitMods': ['+25 to maximum [EnergyShield|Energy Shield]'], 'explicitMods': ['+82 to [Accuracy|Accuracy] Rating', '+106 to maximum Mana', '+49 to [Spirit|Spirit]', '+28 to [Strength|Strength]', '+29% to [Resistances|Fire Resistance]', '+26% to [Resistances|Lightning Resistance]'], 'frameType': 2, 'extended': {'mods': {'explicit': [{'name': "Countess'", 'tier': 'P5', 'level': 47, 'magnitudes': [{'hash': 'explicit.stat_3981240776', 'min': '47', 'max': '50'}]}, {'name': 'of the Furnace', 'tier': 'S5', 'level': 48, 'magnitudes': [{'hash': 'explicit.stat_3372524247', 'min': '26', 'max': '30'}]}, {'name': 'Focused', 'tier': 'P3', 'level': 20, 'magnitudes': [{'hash': 'explicit.stat_803737631', 'min': '61', 'max': '84'}]}, {'name': 'of the Tempest', 'tier': 'S5', 'level': 49, 'magnitudes': [{'hash': 'explicit.stat_1671376347', 'min': '26', 'max': '30'}]}, {'name': 'Chalybeous', 'tier': 'P9', 'level': 53, 'magnitudes': [{'hash': 'explicit.stat_1050105434', 'min': '105', 'max': '124'}]}, {'name': 'of the Leviathan', 'tier': 'S7', 'level': 66, 'magnitudes': [{'hash': 'explicit.stat_4080418644', 'min': '28', 'max': '30'}]}], 'implicit': [{'name': '', 'tier': '', 'level': 18, 'magnitudes': [{'hash': 'implicit.stat_3489782002', 'min': '20', 'max': '30'}]}]}, 'hashes': {'explicit': [['explicit.stat_803737631', [2]], ['explicit.stat_1050105434', [4]], ['explicit.stat_3981240776', [0]], ['explicit.stat_4080418644', [5]], ['explicit.stat_3372524247', [1]], ['explicit.stat_1671376347', [3]]], 'implicit': [['implicit.stat_3489782002', [0]]]}}}}]
specific_key = ten_items

for entry in specific_key:
    item_data = entry.get('item',{})
    key_num = 1
    for mod in item_data.get('explicitMods', []):
        mods = mod.split()
        cleaned_values = []
        for value in mods:
            clean_value = value.replace('[','').replace(']','')

            if '|' in clean_value:
                clean_value = clean_value.split('|')[1]
            cleaned_values.append(clean_value)

        result = ' '.join(cleaned_values)


        item_data[f"explicit_mod{key_num}"] = result
        key_num += 1

print(specific_key[0]['item'])


df = pd.json_normalize(specific_key)

df.to_csv("works.csv", index= False, encoding='utf-8-sig')




#now I should be able to use this to get most things I want.





