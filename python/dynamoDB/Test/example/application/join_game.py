import boto3

from entities import Game, UserGameMapping

dynamodb = boto3.client('dynamodb')

GAME_ID = "c6f38a6a-d1c5-4bdf-8468-24692ccc4646"
USERNAME = 'vlopez'


def join_game_for_user(game_id, username):
    try:
        resp = dynamodb.transact_write_items(
            TransactItems=[
                {
                    # If such an entity did already exist, that would mean this user already joined the game.
                    "Put": {
                        "TableName": "battle-royale",
                        "Item": {
                            "PK": {"S": "GAME#{}".format(game_id) },
                            "SK": {"S": "USER#{}".format(username) },
                            "game_id": {"S": game_id },
                            "username": {"S": username }
                        },
                        #https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html
                        "ConditionExpression": "attribute_not_exists(SK)",
                        #to get item attributes when a condition check fails
                        #https://docs.amazonaws.cn/en_us/amazondynamodb/latest/APIReference/API_ConditionCheck.html
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD"
                    },
                },
                {
                    "Update": {
                        "TableName": "battle-royale",
                        "Key": {
                            "PK": { "S": "GAME#{}".format(game_id) },
                            "SK": { "S": "#METADATA#{}".format(game_id) },
                        },
                        "UpdateExpression": "SET people = people + :p",
                        "ConditionExpression": "people <= :limit",
                        "ExpressionAttributeValues": {
                            ":p": { "N": "1" },
                            ":limit": { "N": "50" }
                        },
                        #the valid values are: NONE, ALL_OLD, UPDATED_OLD, ALL_NEW, UPDATED_NEW
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD"
                    }
                }
            ]
        )
        print("Added {} to game {}".format(username, game_id))
        return True
    except Exception as e:
        print("Could not add user to game")

join_game_for_user(GAME_ID, USERNAME)
