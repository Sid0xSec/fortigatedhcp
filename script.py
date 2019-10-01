
from netmiko import Netmiko
from getpass import getpass

FWFG1FL01 = {
	"host": "",
    "username": "",
    "password": '',
    "device_type": "fortinet",
}

net_connect = Netmiko(**FWFG1FL01)

mac = input ("Please Enter the Mac-Address?\n")
desc = input ("Please enter comment\n")
desc_com = ('"{}"'.format(desc))

command_chk = ['config system dhcp server', 'edit 3', 'config reserved-address', 'get ', 'end']
output_1 = net_connect.send_config_set(command_chk) 

chk = [int(i) for i in output_1.split() if i.isdigit()]
chk_1 = str(chk[-1])
chk_2 = int(chk_1) + 1
chk_3 = str(chk_2)
#print ("Your ID is ",chk_2) 

#print()
#print(net_connect.find_prompt())
command = ['config system dhcp server', 'edit 3', 'config reserved-address', "edit " + chk_3, "set mac " + mac, 'set action assign', 'set description ' + desc_com]
output = net_connect.send_config_set(command)
net_connect.disconnect()
print('its completed')
#print()



