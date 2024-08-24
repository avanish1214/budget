import os
import subprocess


programs_to_run=["python /Users/avanish/Desktop/my_budg/server_internals.py", "python /Users/avanish/Desktop/my_budg/server_security.py","python /Users/avanish/Desktop/my_budg/mail_server.py", "python /Users/avanish/Desktop/my_budg/server_test.py"]

def run_programs(programs):
    processes = []
    for program in programs:
        try:
            # Start the program
            process = subprocess.Popen([program])
            processes.append(process)
            print(f"Started {program} with PID {process.pid}")
        except Exception as e:
            print(f"Failed to start {program}: {e}")
    
    return processes

if __name__ =="__main__":
    processes=run_programs(programs_to_run)
    