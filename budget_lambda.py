import boto3

def stop_ec2_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Update region
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
    else:
        print("No running instances to stop.")

def lambda_handler(event, context):
    stop_ec2_instances()
    return {"status": "Paid services stopped."}
