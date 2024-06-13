import subprocess
import time

# function to start script
def start_script(script):
	process = subprocess.Popen(['python3', script])
	return process

# path to bms_reader.py
first_script = '/home/test/Desktop/team-bms/bms_reader.py'
# path to i2c_display.py
second_script = '/lcd/i2c_display.py'

# start first script
first_process = start_script(first_script)
print(f"{first_script} gestartet mit PID {first_process.pid}")

# wait ten seconds
time.sleep(10)

# start second script
second_process = start_script(second_script)
print(f"{second_script} gestartet mit PID {second_process.pid}")
