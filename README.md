🧠 Serverless Web Hosting using AWS Lambda, API Gateway, S3, CloudFront & DynamoDB

This project demonstrates a fully serverless web application hosted on AWS. It uses Amazon S3 and CloudFront for static web hosting, API Gateway and Lambda for backend logic, and DynamoDB as the database layer — eliminating the need for traditional servers.

🏗️ Architecture Overview

Frontend

Amazon S3 hosts a static website (HTML, and JS).

Amazon CloudFront delivers the website globally with low latency and HTTPS.

Backend

Amazon API Gateway acts as the REST API endpoint, exposing backend routes to the frontend.

AWS Lambda hosts serverless compute functions triggered via API Gateway.

Amazon DynamoDB stores and retrieves data with low-latency access.
