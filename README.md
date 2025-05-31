# AWS PySpark CI/CD Example

This project demonstrates a real-world mini CI/CD pipeline for a PySpark ETL job, automated with GitHub Actions and ready for AWS Glue or S3 integration.

## Project Structure

```
aws-pyspark-ci-cd/
├── scripts/
│   └── job.py                <- Your PySpark job
├── requirements.txt          <- Optional dependencies
├── README.md                 <- Project explanation
└── .github/
    └── workflows/
        └── deploy.yml        <- GitHub Actions CI/CD
```

## Features
- **PySpark** ETL job
- **AWS Glue/S3** ready
- **GitHub Actions** for CI/CD
- Real ETL flow automation

## Usage
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the job: `python scripts/job.py`

## CI/CD
- On push, GitHub Actions will run the ETL job and (optionally) deploy to AWS. # Update trigger
# Update trigger
