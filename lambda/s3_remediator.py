import boto3

def modify_instance_attribute():
    ec2 = boto3.client('ec2')

    # Specify your instance ID and security group information
    instance_id = 'your-instance-id'
    security_group_id = 'your-security-group-id'

    params = {
        'DryRun': False,
        'InstanceId': instance_id,
        'Groups': [security_group_id],
    }

    try:
        ec2.modify_instance_attribute(**params)
        print(f"Insecure SSL protocols disabled for instance: {instance_id}")
    except Exception as error:
        print(f"Error disabling SSL protocols: {str(error)}")

if __name__ == "__main__":
    modify_instance_attribute()
