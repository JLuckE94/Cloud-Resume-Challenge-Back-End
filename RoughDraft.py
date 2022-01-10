import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('viewTable')

def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'id': 'ViewTable'
            }
        )
    return {
        'statusCode': 200,
        'body': response
    }#get

import json#update
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('viewTable')


def lambda_handler(event, context):
    response = table.update_item(Key={'id': 'ViewTable'},
                                 UpdateExpression='set viewCount = viewCount + :val'
                                 ,
                                 ExpressionAttributeValues={':val': Decimal(1)},

                                 ReturnValues='UPDATED_NEW'
                                 )
    return {'statusCode': 200, 'body': response}
