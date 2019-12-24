import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

# When making a GetItem call, we specify the Primary Key attributes defined on our table for the desired item.
resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})

print(resp['Item'])