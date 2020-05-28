import boto3
import threading
import smtplib
import datetime
session = boto3.Session(aws_access_key_id='',
                        aws_secret_access_key='')
client = boto3.client('cloudwatch')


#function for first instance
def first():
    value = 0
    threshold = 3
    while value < threshold:
        response = client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': 'i-01dc9b319c878a8b0'
                },
            ],
            StartTime="2019-02-01T03:46:00Z",
            EndTime=datetime.datetime.now(),
            Period=1800,
            Statistics=['Average'],
            Unit='Percent'
        )
        for item in response["Datapoints"]:
            for items in item:
                if items == "Average":
                    value = item[items]
                    print(value)
    ec2 = boto3.resource('ec2')
    #terminating instances when average exceeds threshold
    ec2.instances.filter(InstanceIds=['i-01dc9b319c878a8b0']).terminate()
    #creating an instance
    ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=1)
    #sending alert mail to my mail-id
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ashok.nirupa20@gmail.com', '')
    message = "Alert: Average crossed the threshold, stopped the instance and spun up an identical one"
    server.sendmail('ashok.nirupa20@gmail.com', 'nirupa.asokan@colorado.edu', message)


#function for second instance
def second():
    value = 0
    threshold = 3
    while value < threshold:
        response = client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': 'i-03bbd2719bce9155c'
                },
            ],
            StartTime="2019-02-01T03:40:00Z",
            EndTime=datetime.datetime.now(),
            Period=1800,
            Statistics=['Average'],
            Unit='Percent'
        )
        for item in response["Datapoints"]:
            for items in item:
                if items == "Average":
                    value = item[items]
                    print(value)
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=['i-03bbd2719bce9155c']).terminate()
    ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=1)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ashok.nirupa20@gmail.com', '')
    message = "Alert: Average crossed the threshold, terminate the instance and spun up an identical one"
    server.sendmail('ashok.nirupa20@gmail.com', 'nirupa.asokan@colorado.edu', message)


#multithread to monitor both instances simultaneously
t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)
t1.start()
t2.start()
t1.join()
t2.join()
