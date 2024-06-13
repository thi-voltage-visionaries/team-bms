import subprocess
import time

def start_script(script):
	process = subprocess.Popen(['python3', script])
	return process

first_script = '/home/test/Desktop/team-bms/bms_reader.py'
second_script = '/lcd/i2c_display.py'

first_process = start_script(first_script)
print(f"{first_script} gestartet mit PID {first_process.pid}")

time.sleep(10)

second_process = start_script(second_script)
print(f"{second_script} gestartet mit PID {second_process.pid}")
