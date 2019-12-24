import boto3
from boto3.dynamodb.conditions import Key, Attr
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
#table = dynamodb.Table('users')

#table.put_item(
#   Item={
#        'username': 'Phuc1995',
#        'first_name': 'Phuc',
#        'last_name': 'Nguyen',
#        'age': 25,
#        'account_type': 'standard_user',
#    }
    
#)


response = client.update_table(
    TableName = 'users',
    # ...snip...
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'YourGSIName',
                'KeySchema': [
                    {
                        'AttributeName': 'YourGSIFieldName',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            }
        }
    ],
    # ...snip...
)
item = response['Items']
print(item)