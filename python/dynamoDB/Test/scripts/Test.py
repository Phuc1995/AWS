import datetime
from dateutil.relativedelta import relativedelta
# for i in range(1,10):
#     now = datetime.datetime.now()
#     date = now + datetime.timedelta(days=i)
#     print(date)

now = str(datetime.date.today() + relativedelta(days=2))
print(now)
# timestamp = datetime.datetime.timestamp(now)
# print('Timestamp: ', timestamp)

# dt_object = int(now.strftime("%d"))+ 1
# print('Date: ', dt_object)
print(type(now))

