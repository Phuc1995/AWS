import boto3
import datetime
from dateutil.relativedelta import relativedelta

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DATE')

# for i in range (1,10):
#     now = datetime.now()
#     timestamp = datetime.timestamp(now)
#     print(timestamp)

# The BatchWriteItem API allows us to write multiple items to a table in one request.
for i in range(1,29):
    now = str(datetime.date.today() + relativedelta(days=i))
    with table.batch_writer() as batch:
        batch.put_item(Item={"ID":i,
        "DATE1": now,
        "USER1": "USER"+ str(i) 
        })

for i in range(1,29):
    now = str(datetime.date.today() + relativedelta(months=i))
    with table.batch_writer() as batch:
        batch.put_item(Item={"ID":i,
        "DATE1": now,
        "USER1": "USER1" 
        })
    
print("Insert item successs")