import ansible_runner

def run_ansible():
    r=ansible_runner.run(private_data_dir=".",inventory="inventory.ini",playbook="playbook.yml")
    print(f"{r.status}")
    for e in r.events:
        if e.get("event")=="runner_on_ok":
            print(e.get("task_name"))
            
            
if __name__== "__main__":
    run_ansible()            