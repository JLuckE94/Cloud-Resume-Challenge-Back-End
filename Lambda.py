import json
import boto3
from decimal import Decimal
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ViewCount')


def lambda_handler(event, context):
    response = table.get_item(Key={'id': 'VCount'})

    response = table.update_item(Key={'id': 'VCount'},
                                 UpdateExpression='set Num = Num + :val'
                                 ,
                                 ExpressionAttributeValues={':val': Decimal(1)},
                                 ReturnValues='UPDATED_NEW')
    num = response['Attributes']['Num']
    json_value = {
        'statusCode': 200,
        'body': float(num),
        'isBase64Encoded': False,
        'headers': {"Access-Control-Allow-Origin": "*"},
        }

    return json_value
