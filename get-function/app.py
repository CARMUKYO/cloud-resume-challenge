import boto3
AWS_REGION = 'ap-southeast-2'
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
from botocore.exceptions import ClientError
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCountTable')

def lambda_handler(event, context):
    try:
        # Get the current visit count from DynamoDB
        response = table.get_item(
            Key={'ID': 'visitors'}
        )

        visit_count = response.get('Item', {}).get('visits', 0)

        # Convert Decimal to a serializable float
        visit_count = float(visit_count)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "http://carmukyo-resume-website.s3-website-ap-southeast-2.amazonaws.com",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({
                "message": "Visit count retrieved successfully",
                "visitCount": visit_count
            })
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "http://carmukyo-resume-website.s3-website-ap-southeast-2.amazonaws.com",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
