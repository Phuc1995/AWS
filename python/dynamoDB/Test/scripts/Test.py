import datetime

# for i in range(1,10):
#     now = datetime.datetime.now()
#     date = now + datetime.timedelta(days=i)
#     print(date)

now = datetime.datetime.now()
timestamp = datetime.datetime.timestamp(now)
print('Timestamp: ', timestamp)

dt_object = datetime.datetime.fromtimestamp(timestamp)
print('Date: ', dt_object)

