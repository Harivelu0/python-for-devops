from kubernetes import client,config
import argparse

config.load_kube_config()
v1=client.CoreV1Api()

def create_namespace(name):
    namespace=client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
    try:
        v1.create_namespace(namespace)
        print(f"Namespace '{name}' created successfully")
    except client.exceptions.ApiException as e:
        if e.status==409:
            print(f"Namespace '{name}' already exists")
        else:
            print(f"Error creating namespace '{name}': {e}")
            
def delete_namespace(name):
    try:
        v1.delete_namespace(name)
        print(f"Namespace '{name}' deleted successfully")
    except client.exceptions.ApiException as e:
        if e.status==404:
            print(f"Namespace '{name}' does not exist")
        else:
            print(f"Error deleting namespace '{name}': {e}")
            
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Manage Kubernetes namespaces")
    parser.add_argument("--action",required=True,choices=["create","delete"])
    parser.add_argument("--name",required=True,help="Namespace name")
    args=parser.parse_args()
    
    if args.action=="create":
        create_namespace(args.name)
    elif args.action=="delete":
        delete_namespace(args.name)
    else:
        print("Invalid action")