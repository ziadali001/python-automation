import boto3

ec2_client_ohio = boto3.client('ec2', region_name="us-east-2")
ec2_resource_ohio = boto3.resource('ec2', region_name="us-east-2")

ec2_client_oregon = boto3.client('ec2', region_name="us-west-2")
ec2_resource_oregon = boto3.resource('ec2', region_name="us-west-2")


instance_ids_ohio = []
instance_ids_oregon = []

reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
for res in reservations_ohio:
    instances = res['Instances']
    for ins in instances:
        instance_ids_ohio.append(ins['InstanceId'])


response = ec2_resource_ohio.create_tags(
    Resources=instance_ids_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_oregon = ec2_client_oregon.describe_instances()['Reservations']
for res in reservations_oregon:
    instances = res['Instances']
    for ins in instances:
        instance_ids_oregon.append(ins['InstanceId'])


response = ec2_resource_oregon.create_tags(
    Resources=instance_ids_oregon,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
