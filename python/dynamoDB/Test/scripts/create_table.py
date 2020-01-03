import boto3

dynamodb = boto3.client('dynamodb')

try:
    dynamodb.create_table(
        TableName='DATE',
        AttributeDefinitions=[
            {
                "AttributeName": "USER1",
                "AttributeType": "S"
            },
            {
                "AttributeName": "DATE",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "USER1",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "DATE",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully.")
except Exception as e:
    print("Could not create table. Error:")
    print(e)
