import time

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

# When adding a global secondary index to an existing table, you cannot query the index until it has been backfilled.
# This portion of the script waits until the index is in the “ACTIVE” status, indicating it is ready to be queried.
while True:
    if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        print('Waiting for index to backfill...')
        time.sleep(5)
        table.reload()
    else:
        break

# When making a Query call, you use the KeyConditionExpression parameter to specify the hash key on which you want to query.
# If you want to use a specific index, you also need to pass the IndexName in our API call.
resp = table.query(
    # Add the name of the index you want to use in your query.
    IndexName="CategoryIndex",
    KeyConditionExpression=Key('Category').eq('Suspense'),
)
print("Test: ",table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE')
print("The query returned the following items:")
for item in resp['Items']:
    print(item)