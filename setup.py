import check_depends, os, subprocess, socket

cwd = os.getcwd()
f=open("/etc/systemd/system/pionpioff.service","w+")
f.write('[Unit] \nDescription=Pi On Pi Off Webserver\nAfter=network.target\n\n[Service]\nType=simple\nUser=pi\nWorkingDirectory=%s\nExecStart="/usr/bin/python3 %s/Main.Py" \nRestart=on-failure # or always, on-abort, etc\n[Install]\nWantedBy=multi-user.target' %(cwd, cwd))

f.close()
command = "sudo systemctl daemon-reload"
subprocess.Popen(command, shell=True, executable='/bin/bash').wait()

command2 = "systemctl start pionpioff.service"
subprocess.Popen(command2, shell=True, executable='/bin/bash').wait()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

print("Thanks For Installing, You should now be able to access the website on http://127.0.0.1 or http://:%s" %(ip))