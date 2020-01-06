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
                "AttributeName": "DATE1",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "USER1",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "DATE1",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 20,
            "WriteCapacityUnits": 20
        }
    )
    print("Table created successfully.")
except Exception as e:
    print("Could not create table. Error:")
    print(e)