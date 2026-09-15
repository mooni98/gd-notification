# Game Day Notification

A Python-based AWS Lambda project that retrieves Premier League match data from football-data.org and sends match updates through Amazon SNS (Simple Notification Service).

## What this project does

The Lambda function:

- Retrieves Premier League match data from football-data.org
- Formats upcoming matches into a simple message
- Publishes the message to an Amazon SNS topic
- Uses environment variables for sensitive configuration such as the API key and SNS topic ARN

## Tech stack

- Python
- AWS Lambda
- Amazon SNS
- football-data.org API
- python-dotenv
- boto3

## How it works

```text
AWS Lambda
   ↓
football-data.org API
   ↓
Match data
   ↓
Amazon SNS
   ↓
Notification
```

## Environment variables

The project uses environment variables instead of hard-coded secrets.

Create a local `.env` file with:

```text
SPORTS_API_KEY=your_api_key_here
SNS_TOPIC_ARN=your_sns_topic_arn_here
```

The `.env` file should not be committed to GitHub.

## Project files

```text
gd-notification/
├── lambda_function.py
├── .gitignore
├── .env
└── README.md
```

## Run locally

Install the required packages:

```bash
pip install boto3 python-dotenv
```

Then run:

```bash
python lambda_function.py
```

## AWS deployment

This project was originally deployed using:

- AWS Lambda
- Amazon SNS
- IAM permissions for Lambda to publish to SNS

The AWS resources were later removed, so the cloud deployment is not currently active.

## Security

Sensitive values such as the football-data.org API key and SNS topic ARN are stored in environment variables instead of directly in the source code.
