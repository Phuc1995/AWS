import json

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('battle-royale')

items = []

with open('items.json') as f:
    for row in f:
        items.append(json.loads(row))

print('')

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
