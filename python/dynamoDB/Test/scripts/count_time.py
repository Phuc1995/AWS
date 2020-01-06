import json
import boto3
import time
import datetime
from dateutil.relativedelta import relativedelta

data = {}
data = []

now = datetime.datetime.now()
for i in range (1,5000):
    now = str(datetime.date.today() + relativedelta(days=i))
    data.append(
        {
            'USER1':'USER1',
            'DATE1': now,
        }
    )

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

start_time = time.time()
print('Start time: ', time.asctime( time.localtime(start_time)))

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DATE')
with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)

end_time = time.time()
print('Insert success')
print('End time: ', time.asctime( time.localtime(end_time)), '-',(end_time-start_time))
