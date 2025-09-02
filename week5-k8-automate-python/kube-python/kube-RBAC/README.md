
#  Kubernetes RBAC Auditor with Python (Week 5 - Task 2)

This project uses the **Kubernetes Python SDK** to audit **Service Accounts and their Role/ClusterRole bindings** inside a namespace.

## 📦 What it Does
- Lists all ServiceAccounts in a given namespace.  
- Checks RoleBindings for each ServiceAccount.  
- Checks ClusterRoleBindings for ServiceAccounts.  
- Warns if a ServiceAccount has **cluster-admin** privileges.  

## 🛠️ Requirements
- Python 3.8+  
- Kubernetes cluster access via `~/.kube/config`  
- Install dependencies:  

```bash
pip install kubernetes argparse
````

## ▶️ Usage

```bash
# Audit a namespace
python rbac_audit.py --namespace default
```

### Example Output

```
Auditing service accounts in namespace: default
service account: default
Bound to cluster role: cluster-admin
cluster has full access
```


