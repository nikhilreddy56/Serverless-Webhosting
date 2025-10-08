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
