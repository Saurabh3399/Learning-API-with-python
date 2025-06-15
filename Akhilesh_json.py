import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
	"x-rapidapi-key": "59c97de795msh489edd0813b52d6p18b5dcjsn7d96aa7b34ed",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

match_data = response.json()

for i in range(3):
    # Navigate through the nested dictionary structure to reach 'matchInfo'
    # This assumes the structure is consistent:
    # typeMatches[0] -> seriesMatches[0] -> seriesAdWrapper -> matches[0] -> matchInfo
    match_info = match_data['typeMatches'][i]['seriesMatches'][0]['seriesAdWrapper']['matches'][0]['matchInfo']

    # Extract Team 1 details
    team1_data = match_info['team1']
    team1_name = team1_data['teamName']
    team1_sname = team1_data['teamSName']

    # Extract Team 2 details
    team2_data = match_info['team2']
    team2_name = team2_data['teamName']
    team2_sname = team2_data['teamSName']

    # Print the extracted information
    print(f"Team 1 Full Name: {team1_name}")
    # print(f"Team 1 Short Name: {team1_sname}")
    print(f"Team 2 Full Name: {team2_name}")
    # print(f"Team 2 Short Name: {team2_sname}")
    print('---------------------------------------------------')