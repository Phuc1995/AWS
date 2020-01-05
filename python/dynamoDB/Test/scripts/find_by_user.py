import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.client('dynamodb')

USER = "USER1"

def find_by_user(user):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :user ",
            ExpressionAttributeValues={
                ":user": { "S": "USER1" }
                
            },
            #ScanIndexForward is the correct way to get items in descending order by the range key of the table or index you are querying
            ScanIndexForward = True 
        )
    return resp

def find_by_user_and_date(user, date):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :user and DATE1 = :date",
            ExpressionAttributeValues={
                ":user": { "S": user },
                ":date": {"S": date}
                
            },
            ScanIndexForward = False 
        )
    return resp

def find_by_user_between_date(user, date_begin, date_end):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :user and DATE1 between :date_begin and :date_end",
            ExpressionAttributeValues={
                ":user": { "S": user },
                ":date_begin": {"S": date_begin},
                ":date_end": {"S": date_end}
            },
            ScanIndexForward = True 
        )
    return resp

def find_by_user_less(user, date):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :user and DATE1 >:date",
            ExpressionAttributeValues={
                ":user": { "S": user },
                ":date": {"S": date},
            },
            ScanIndexForward = True 
        )
    return resp

def find_by_user_begin_withs(user, date):
    resp = dynamodb.query(
            TableName='DATE',
            KeyConditionExpression="USER1 = :user and begins_with(DATE1,:date)",
            ExpressionAttributeValues={
                ":user": { "S": user },
                ":date": {"S": date},
            },
            ScanIndexForward = True 
        )
    return resp

# user = find_by_user_between_date("USER1","2020-04-5","2020-12-5")
# user = find_by_user_less("USER1","2020-04-05")
user = find_by_user_begin_withs('USER1',"2020-01")

for i in user['Items']:
    print(i.get('DATE1').get('S'), '-', i.get('USER1').get('S'))