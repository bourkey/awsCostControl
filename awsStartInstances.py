import boto3

region = 'ap-southeast-2'

def lambda_handler(event, context):
    ec2client = boto3.client('ec2', region_name=region)
    ec2 = boto3.resource('ec2', region_name=region)
    ec2RunningInstancesIDs = []
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:startup', 'Values': ['true']}, {'Name': 'instance-state-name', 'Values': ['stopped']}])
    if not instances:
        exit(1)
    for instance in instances:
        ec2RunningInstancesIDs.append(instance.id)
    ec2client.start_instances(InstanceIds=ec2RunningInstancesIDs)

    