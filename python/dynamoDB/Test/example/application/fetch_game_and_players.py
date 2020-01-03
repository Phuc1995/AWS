import boto3

from entities import Game, UserGameMapping

dynamodb = boto3.client('dynamodb')

GAME_ID = "3d4285f0-e52b-401a-a59b-112b38c4a26b"


def fetch_game_and_users(game_id):
    resp = dynamodb.query(
        TableName='battle-royale',
        KeyConditionExpression="PK = :pk ",
        ExpressionAttributeValues={
            ":pk": { "S": "GAME#3d4285f0-e52b-401a-a59b-112b38c4a26b" }
            
        },
        #ScanIndexForward is the correct way to get items in descending order by the range key of the table or index you are querying
        ScanIndexForward=True
    )

    game = Game(resp['Items'][0])
    print('')
    #print('Test: ', game)
    game.users = [UserGameMapping(item) for item in resp['Items'][1:]]

    return game


game = fetch_game_and_users(GAME_ID)

print('Test: ',game)
for user in game.users:
    print(user)

