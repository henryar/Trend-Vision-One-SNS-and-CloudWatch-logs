# Trend-Vision-One-SNS-and-CloudWatch-logs
Trend Vision One SNS and CloudWatch logs

#Can Cloud One Workload Security forward the Syslog event directly to either AWS Cloudwatch or AWS S3?
Currently, this is not supported. Cloud One Workload Security has no ability to forward Syslog events directly to Amazon S3 and Cloudwatch.
https://success.trendmicro.com/en-US/solution/KA-0010725#Funct_SIEM_07

Nevertheless, Cloud One Workload Security can support forwarding events to Amazon SNS.
https://cloudone.trendmicro.com/docs/workload-security/event-sns/

You can use a Lambda function in one AWS account to subscribe to an Amazon Simple Notification Service (Amazon SNS) topic. When you publish messages to your Amazon SNS topic, your Lambda function reads the contents of the message and outputs it to Amazon CloudWatch Logs

![image](https://github.com/user-attachments/assets/8b4f8d46-4376-45d3-b156-04d243e14f5c)


![image](https://github.com/user-attachments/assets/1955e4ce-0c38-4e9b-a837-705d54a6c37e)
