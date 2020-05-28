
import boto3
#Connecting to EC2
ec2 = boto3.resource('ec2')
#Creating two instances
ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=2)
#shows instances in running state
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
lists = []
lists2 = []
#list for all the running instance ids
for instance in instances:
    lists.append(instance.id)
#list for instance ids to be stopped
lists2.append(lists[0])
#Stopping one instance
ec2.instances.filter(InstanceIds=lists2).stop()
instances1 = ec2.instances.filter()
for inst in instances1:
    print(inst.id, inst.instance_type, inst.state, inst.public_ip_address)
