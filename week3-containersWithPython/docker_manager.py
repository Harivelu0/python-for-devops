import subprocess
import argparse

def manage_container(action, container):
    try:
        if action not in ["start", "stop", "restart", "rm"]:
            print("❌ Invalid action.")
            return

        result = subprocess.run(["docker", action, container], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Successfully ran: docker {action} {container}")
        else:
            print("💥 Error:", result.stderr.strip())

    except Exception as e:
        print("❌ Exception:", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docker container manager using subprocess")
    parser.add_argument("--action", type=str, required=True, help="Action: start, stop, restart, rm")
    parser.add_argument("--container", type=str, required=True, help="Container name or ID")
    args = parser.parse_args()

    manage_container(args.action, args.container)
