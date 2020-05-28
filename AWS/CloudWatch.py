import boto3
session = boto3.Session(aws_access_key_id='',
                        aws_secret_access_key='')
client = boto3.client('cloudwatch')
print("Instance ID : i-055c2fe14984f322f")


def func(a, b):
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName=a,
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-055c2fe14984f322f'
            },
        ],
        StartTime="2019-02-02T06:00:00Z",
        EndTime="2019-02-02T06:30:00Z",
        Period=1800,
        Statistics=['Average'],
        Unit=b
)
    for item in response["Datapoints"]:
        for items in item:
            if items == "Average":
                print(a, ":", item[items], b)


func('CPUUtilization', 'Percent')
func('StatusCheckFailed', 'Count')
func('NetworkIn', 'Bytes')
func('NetworkOut', 'Bytes')
