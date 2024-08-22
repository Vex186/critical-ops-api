import requests
#vex1337
def get_profile_info(username):
    try:
        url = f'https://1-46-0.prod.copsapi.criticalforce.fi/api/public/profile?usernames={username}'
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        return f"Error: {e}"

def print_profile_info(profile):
    basic_info = profile[0]['basicInfo']
    print(f"User ID: {basic_info['userID']}")
    print(f"Name: {basic_info['name']}")
    print(f"Player Level: {basic_info['playerLevel']['level']}")
    print(f"Current XP: {basic_info['playerLevel']['current_xp']}")
    print(f"Next Level XP: {basic_info['playerLevel']['next_level_xp']}")
    print(f"Last Seen Time: {basic_info['lastSeenTime']}")
    
    user_settings = profile[0]['userSettings']
    print(f"Block Friend Requests: {user_settings['blockFriendRequests']}")
    print(f"Block Clan Requests: {user_settings['block_clan_requests']}")
    
    stats = profile[0]['stats']
    print("Seasonal Stats:")
    for season in stats['seasonal_stats']:
        print(f"  Season {season['season']}:")
        print(f"    Ranked - Kills: {season['ranked']['k']}, Deaths: {season['ranked']['d']}, Assists: {season['ranked']['a']}, Wins: {season['ranked']['w']}, Losses: {season['ranked']['l']}")
        print(f"    Casual - Kills: {season['casual']['k']}, Deaths: {season['casual']['d']}, Assists: {season['casual']['a']}, Wins: {season['casual']['w']}, Losses: {season['casual']['l']}")
        print(f"    Custom - Kills: {season['custom']['k']}, Deaths: {season['custom']['d']}, Assists: {season['custom']['a']}, Wins: {season['custom']['w']}, Losses: {season['custom']['l']}")
    
    ranked_info = stats['ranked']
    print(f"Highest Rank: {ranked_info['highest_rank']}")
    print(f"MMR: {ranked_info['mmr']}")
    print(f"Rank: {ranked_info['rank']}")

username = input("User Name: ")
profile = get_profile_info(username)
if isinstance(profile, list) and profile:
    print_profile_info(profile)
else:
    print(profile)

input("Çıkmak için Enter'a basın...")
