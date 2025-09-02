from python_terraform import Terraform
import argparse

def run_terraform(action):
    tf=Terraform(working_dir='./')
    
    if action=="init":
        print("Running :terraform init")
        return tf.init()
    elif action=="plan":
        print("Running :terraform plan")
        return tf.plan()
    elif action=="apply":
        print("Running :terraform apply")
        return tf.apply(skip_plan=True,auto_approve=True)
    elif action=="destroy":
        print("Running :terraform destroy")
        return tf.destroy(skip_plan=True,auto_approve=True)
    else:
        return "Invalid action"
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Run terraform actions")
    parser.add_argument("--action", required=True, choices=["apply","plan","init","destroy"])
    args=parser.parse_args()
    
    output=run_terraform(args.action)
    print(output)
                                                        