import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    print("Event received:", event)
    try:
        # Extract values from the event
        student_id = str(event['studentid'])   # ensure correct type
        name = event['name']
        student_class = event['class']
        age = int(event['age'])
        
        # Test table connection
        print("Attempting to write to DynamoDB table:", table.name)

        # Write data to DynamoDB
        response = table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )

        print("DynamoDB put_item response:", response)

        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully!')
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
