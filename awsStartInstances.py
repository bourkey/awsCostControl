# import reqs
import boto3

# Set Approriate Region
region = 'ap-southeast-2'

# Lamba Handler
def lambda_handler(event, context):
    ec2client = boto3.client('ec2', region_name=region)
    ec2 = boto3.resource('ec2', region_name=region)
    ec2RunningInstancesIDs = []
    instances = ec2.instances.filter(
        # Filter Instances based On Tag, Check Current State
        Filters=[{'Name': 'tag:startup', 'Values': ['true']}, {'Name': 'instance-state-name', 'Values': ['stopped']}])
    if not instances:
        exit(1)
    for instance in instances:
        ec2RunningInstancesIDs.append(instance.id)
    ec2client.start_instances(InstanceIds=ec2RunningInstancesIDs)

