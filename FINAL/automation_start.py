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
# pid = process identifier number, means which process is running
first_process = start_script(first_script)
print(f"{first_script} gestartet mit PID {first_process.pid}")

# wait ten seconds
time.sleep(10)

# start second script
second_process = start_script(second_script)
print(f"{second_script} gestartet mit PID {second_process.pid}")

# DO FOLLOWING STEPS TO START SCRIPT IN TERMINAL
# 1. create new service file -->
# sudo nano /etc/systemd/system/starter.service

# 2. write this information in service file -->
# [Unit]
# Description=starter for two python scripts
# After=network.target
# [Service]
# ExecStart=/usr/bin/python3 /home/test/Desktop/team-bms/automation_start.py
# WorkingDirectory=/home/test/Desktop/team-bms
# StandardOutput=inherit
# StandardError=inherit
# Restart=always
# User=test
# [Install]
# WantedBy=multi-user.target

# 3. activate and start systemd service -->
# sudo systemctl daemon-reload
# sudo systemctl enable starter.service
# sudo systemctl start starter.service

# 4. check systemd service -->
# sudo systemctl status starter.service

# 5. quit systemd service -->
# sudo systemctl stop starter.service
