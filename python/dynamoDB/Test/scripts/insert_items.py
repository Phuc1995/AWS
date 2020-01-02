import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DATE')

# for i in range (1,10):
#     now = datetime.now()
#     timestamp = datetime.timestamp(now)
#     print(timestamp)

# The BatchWriteItem API allows us to write multiple items to a table in one request.
for i in range(1,100):
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=i)
    with table.batch_writer() as batch:
        batch.put_item(Item={"ID":str(i),
        "DATE": date.isoformat(" ","seconds"),
        "USER": "USER" + str(i),
        })
    for j in range(1,60):
        date2 = now + datetime.timedelta(days=j)
        with table.batch_writer() as batch:
            batch.put_item(Item={
            "DATE": date.isoformat(" ","seconds"),
            "USER": "USER" + str(i),
            })
print("Insert item successs")