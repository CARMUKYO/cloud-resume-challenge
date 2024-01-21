import boto3
from botocore.exceptions import ClientError
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCountTable')

def lambda_handler(event, context):
    try:
        # Increment the visit count in DynamoDB
        response = table.update_item(
            Key={'ID': 'visitors'},
            UpdateExpression='ADD visits :val',
            ExpressionAttributeValues={':val': 1},
            ReturnValues='UPDATED_NEW'
        )

        new_visit_count = response['Attributes']['visits']

        # Convert Decimal to a serializable float
        new_visit_count = float(new_visit_count)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "http://carmukyo-resume-website.s3-website-ap-southeast-2.amazonaws.com",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({
                "message": "Visit count updated successfully",
                "newVisitCount": new_visit_count
            })
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
