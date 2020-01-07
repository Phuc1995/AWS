<<<<<<< HEAD
import time

a = time.time()

b = time.time()
=======
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
>>>>>>> bf52863c3792e6104df67c73c6e461e6c23a682c

print(b-a)
