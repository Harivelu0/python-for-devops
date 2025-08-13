import boto3
import argparse

ec2 = boto3.client('ec2', region_name='us-east-1')

def manage_instance(action, instance_ids):
    for instance_id in instance_ids:
       if action == "start":
           ec2.start_instances(InstanceIds=[instance_id])
           print(f"Started instance {instance_id}")

       elif action == "stop":
           ec2.stop_instances(InstanceIds=[instance_id])
           print(f"Stopped instance {instance_id}")

       elif action == "terminate":
           confirm = input(f"Are you sure you want to TERMINATE instance {instance_id}? (yes/no): ").strip().lower()
           if confirm == "yes":
               ec2.terminate_instances(InstanceIds=[instance_id])
               print(f"Terminated instance {instance_id}")
           else:
               print("Termination cancelled.")

       else:
           print("Invalid action. Use start, stop, or terminate.")

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Manage EC2 instances")
    parser.add_argument("--action",type=str,required=True,help="Action to perform (start, stop, terminate)")
    parser.add_argument("--instance-ids",type=str,nargs="+",help="EC2 isntance id")
    args=parser.parse_args()
    print("args received")
    manage_instance(args.action.lower(),args.instance_ids)
    