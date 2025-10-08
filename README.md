🧠 Serverless Web Hosting using AWS Lambda, API Gateway, S3, CloudFront & DynamoDB

This project demonstrates a fully serverless web application hosted on AWS using:

Amazon S3 + CloudFront for hosting the frontend,

API Gateway + Lambda (post_function.py & get_function.py) for backend logic, and

DynamoDB for storing and retrieving student data.

🏗️ Architecture Overview

Frontend

Hosted on Amazon S3, distributed globally via CloudFront.

Communicates with API Gateway endpoints for data operations.

Backend

API Gateway exposes REST API endpoints /students for GET and POST.

get_function.py Lambda handles fetching data from DynamoDB.

post_function.py Lambda handles inserting data into DynamoDB.

DynamoDB table stores student records in a NoSQL format.


The two Lambda functions — get_function.py and post_function.py — are integrated with API Gateway as the GET and POST methods of the /students endpoint. The GET method (get_function.py) retrieves all student records from the DynamoDB table and returns them to the frontend, while the POST method (post_function.py) accepts JSON input from the client, adds a new student entry to the DynamoDB table, and returns a success response. Both methods are configured with CORS enabled, allowing the frontend hosted on S3/CloudFront to securely interact with the API.
