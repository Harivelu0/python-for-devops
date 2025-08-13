import subprocess
import argparse

def get_pods(namespace):
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace],
            capture_output=True,
            text=True,
            check=True
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if "No resources found" in stdout or "No resources found" in stderr:
            print(f" No pods found in namespace '{namespace}'.")
        else:
            print(f"Pods in namespace '{namespace}':\n")
            lines = stdout.splitlines()
            if not lines:
                print(" No pod data received.")
                return

            header = lines[0]
            rows = lines[1:]
            print(header)
            print("-" * len(header))
            for row in rows:
                print(row)

    except subprocess.CalledProcessError as e:
        print("Error running kubectl:", e.stderr.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Kubernetes pods in the given namespace")
    parser.add_argument("--namespace", type=str, required=True, help="Namespace name required")
    args = parser.parse_args()

    get_pods(args.namespace)
