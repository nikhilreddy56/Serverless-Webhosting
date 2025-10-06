# Serverless-Webhosting
🧩 Overview

This project demonstrates how to host and deploy a Python-based application on a fully serverless AWS architecture using the following services:

Amazon S3 – for static file hosting (frontend, assets)

AWS Lambda – for backend logic and API endpoints

Amazon API Gateway – to expose Lambda functions as REST APIs

Amazon DynamoDB – for scalable, serverless database storage

Amazon CloudFront – as a global CDN for caching and secure content delivery

The architecture eliminates the need for managing traditional servers, ensuring high scalability, low operational overhead, and cost efficiency.


🪄 How It Works

Frontend is uploaded to an S3 bucket configured for static website hosting.

CloudFront sits in front of S3, serving static assets with caching and HTTPS.

User actions (like form submissions or button clicks) call the API Gateway endpoint.

API Gateway triggers the Lambda function (written in Python).

Lambda performs business logic and interacts with DynamoDB to fetch or store data.

Responses are sent back through API Gateway → CloudFront → Browser.

🛠️ Technologies Used

Python 3.x

AWS Lambda

Amazon API Gateway

Amazon DynamoDB

Amazon S3

Amazon CloudFront

AWS CLI


🧠 Example Use Case

This architecture can support applications such as:

Feedback collection app

To-do list or notes app

Lightweight REST APIs

Contact form submissions

Serverless dashboards