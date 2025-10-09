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

<img width="1084" height="331" alt="image" src="https://github.com/user-attachments/assets/b9e82be7-365c-4f1f-8857-a5a6b3e8ad4a" />

<img width="1145" height="507" alt="image" src="https://github.com/user-attachments/assets/9108418a-01e8-4ddf-93be-2898c56553d6" />



The API Gateway Invoke URL is integrated into the script.js file, allowing the frontend to communicate securely with the backend Lambda functions through the defined API endpoints. Both index.html and script.js are uploaded to an Amazon S3 bucket configured for static website hosting, with public access disabled for enhanced security. Instead of exposing the S3 URL directly, the site is served via Amazon CloudFront, which provides HTTPS encryption, global content distribution, and faster access through edge locations. This ensures that all user interactions with the web application occur securely and efficiently

<img width="1211" height="490" alt="image" src="https://github.com/user-attachments/assets/7e91a329-3e59-47a1-b3ce-45ba78263c52" />



<img width="1213" height="327" alt="image" src="https://github.com/user-attachments/assets/9ccf15bc-88ad-4de7-bda3-850245857b56" />




web hosting files(index.html and script.js) are added to S3 bucket- <img width="1326" height="494" alt="image" src="https://github.com/user-attachments/assets/f0146dbd-8bda-436e-9ba6-87b5fe9ad68e" />


