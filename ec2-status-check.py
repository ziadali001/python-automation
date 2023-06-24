import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-1")
ec2_resource = boto3.resource('ec2', region_name="us-west-1")


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} instance status {ins_status} system status {sys_status}")
    print("#############################\n")


schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()


# reservations = ec2_client.describe_instances()
# for reservations in reservations['Reservations']:
#     instances = reservations['Instances']
#     for instance in instances:
#         print(f"instance {instance['InstanceId']} is {instance['State']['Name']}")
