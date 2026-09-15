
import urllib.request
import json
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def lambda_handler(event, context):


    url = 'https://api.football-data.org/v4/competitions/PL/matches'

    sports_api_key = os.getenv("SPORTS_API_KEY")

    headers = {
    "X-Auth-Token": sports_api_key
}




    # Make the API request

    req = urllib.request.Request(url, headers=headers)


    # Get the response

    with urllib.request.urlopen(req) as response:
        raw_data = response.read()

        # Parse the JSON data

    data = json.loads(raw_data.decode('utf-8'))

    # Get the matches

    matches = data.get('matches', [])
    
    # Get the first match

   

    if not matches:
        message = 'no matches found'

    else:
        game = []
        for match in matches[:3]:  # Get the first 3 matches
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            game.append(f'{home_team} vs {away_team}')

    # message to send to SNS

    message = '\n' + '\n'.join(game)
    
    

    sns = boto3.client('sns')

    response = sns.publish(

        TopicArn=os.getenv("SNS_TOPIC_ARN"),
        Message=message,
        Subject='Premier League Match Update'
        
    ) 

    


    return{

        'statusCode': 200,
        'body': 'Message sent!'

    }

if __name__ == "__main__":
    result = lambda_handler({}, {})
    print(result)