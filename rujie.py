import paramiko
# switch’e SSH ile bağlan
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.1", port=22, username="username", password="password")

# VLAN oluştur
vlan_id = "10"
vlan_name = "VLAN10"
stdin, stdout, stderr = ssh.exec_command("system-view")
stdin.write("vlan batch 10\nvlan name 10 VLAN10\n")

# port’u VLAN’a ekle
port = "GigabitEthernet0/0/1"
stdin.write("interface " + port + "\nport link-type access\nport default vlan " + vlan_id + "\nquit\n")
ssh.close()