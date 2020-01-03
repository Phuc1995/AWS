import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.client('dynamodb')

USER = "USER1"

def find_by_user(user):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :pk ",
            ExpressionAttributeValues={
                ":pk": { "S": "USER1" }
                
            },
            #ScanIndexForward is the correct way to get items in descending order by the range key of the table or index you are querying
            ScanIndexForward=True
        )
    return resp

user = find_by_user(USER)
for i in user['Items']:
    print(i.get('DATE').get('S'))