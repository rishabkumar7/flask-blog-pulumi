"""An AWS Python Pulumi program"""

import pulumi
import json
from pulumi_aws import dynamodb, ec2, iam

# Create an AWS DynamoDB table
dynamodb_table = dynamodb.Table('BlogPosts',
    attributes=[dynamodb.TableAttributeArgs(
        name='post_id',
        type='S',
    )],
    hash_key='post_id',
    read_capacity=1,
    write_capacity=1,
    tags={
        "Name": "BlogPosts",
    },
)

ubuntu_ami = ec2.get_ami(filters=[
        {"name": "name", "values": ["ubuntu/images/hvm-ssd/ubuntu-*-20.04-amd64-server-*"]},
        {"name": "virtualization-type", "values": ["hvm"]},
    ],
    owners=["099720109477"],
    most_recent=True,
)

# Create an IAM role for the EC2 instance to access DynamoDB
ec2_role = iam.Role("ec2Role",
    assume_role_policy=pulumi.Output.from_input({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com",
            },
        }],
    }).apply(lambda policy: json.dumps(policy)),
)

# Attach the Amazon DynamoDB Full Access policy to the role
attach_policy = iam.RolePolicyAttachment("attachPolicy",
    policy_arn="arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
    role=ec2_role.name,
)
# Create an IAM instance profile to attach the role to an instance
instance_profile = iam.InstanceProfile("instanceProfile", role=ec2_role.name)

ec2_instance = ec2.Instance("webserver",
    instance_type="t2.micro",
    ami=ubuntu_ami.id,
    iam_instance_profile=instance_profile.arn,
    user_data="""#!/bin/bash
    # Install dependencies
    sudo apt-get update
    sudo apt-get install -y python3-pip python3-venv
    # Clone your repository
    git clone https://github.com/rishabkumar7/flask-blog-pulumi
    # Replace below with the path to your app, if different
    cd flask-blog-pulumi
    # Set up your application
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    # Start your application with the DynamoDB table name as an environment variable
    export DYNAMODB_TABLE_NAME=$(curl http://169.254.169.254/latest/user-data/)
    flask run --host=0.0.0.0 --port=80
    """,
    # Pass the DynamoDB table name as user data to the EC2 instance
    user_data_replace_on_change=True,
)
# Pass the DynamoDB table name as the EC2 user data for the Flask application to use
