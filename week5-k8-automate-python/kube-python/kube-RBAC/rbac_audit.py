from kubernetes import client, config
import argparse
config.load_kube_config()

rbac_api=client.RbacAuthorizationV1Api()
core_api=client.CoreV1Api()

def get_all_service_account(namespace):
    sAccount=core_api.list_namespaced_service_account(namespace=namespace)
    return [sAccount.metadata.name for sAccount in sAccount.items]
def get_role_bindings(namespace):
    return rbac_api.list_namespaced_role_binding(namespace=namespace)
def get_cluster_role_bindings():
    return rbac_api.list_cluster_role_binding()
def check_rbac(namespace):
    print(f"Auditing service accounts sin namespace: {namespace}")
    service_accounts=get_all_service_account(namespace)
    role_bindings=get_role_bindings(namespace)
    cluster_role_bindings=get_cluster_role_bindings()
    
    for service_account in service_accounts:
        found=False
        print(f"service account:{service_account}")
        for role_binding in role_bindings.items:
            for subject in role_binding.subjects:
                if subject.kind=="ServiceAccount" and subject.name==service_account:
                   print(f"Bound to rulee:{role_binding.role_ref.name}")
                   found=True
                   break
            if found:
                break
            
    for cluster_role_binding in cluster_role_bindings.items:
        if cluster_role_binding.subjects:
            for subjects in cluster_role_binding.subjects:

                if subjects.kind=="ServiceAccount" and subjects.name in service_accounts:
                    print(f"Bound to cluster role:{cluster_role_binding.role_ref.name}")
                    if cluster_role_binding.role_ref.name=="cluster-admin":
                        print("cluster has full access")
                    found=True
                break
        if found:
            break

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Audit k8s RBAC")
    parser.add_argument("--namespace",required=True,help="Namespace to audit")
    args=parser.parse_args()
    check_rbac(args.namespace)
                