import os
#from banner import xe_header
import sys, traceback
import time

print('--------------Kama Kepar Script ---------------')
print('There was an error initializing your OS, so please choose your system...')
print('1.Set ip on Debian')
print('2.Set ip on Parrot')
print('3.Set ip on Termux (root needed)')
print('4.Set ip on Ubuntu GNU/LINUX')
print('5.Set ip on Linux Mint')
print('6.Set ip on Fedora Linux')
print('7.Set ip on Cent OS')
print('8.Set ip on Porteus KDE, Xfce, LXDE, others...')
ips = int(input('Choose your system> '))

print('\n')
print('\n')
print('So what ip you want to set?')
ip = str(input('Set ip> '))
print('\n')
print('So what ip you want to set?')
stat = str(input('static/dynamic(s/d) > '))
print('What netmask you want to set? (X.X.X.X)')
netm = str(input('netmask> '))
print('What gateway do you want set')
gate = str(input('gateway> '))
name = str(input('nameserver(standart:8.8.8.8)> '))
names = str(input('dns-nameservers std(8.8.8.8 8.8.4.4)> '))


print('Process started.')
time.sleep(1)
print('Process started..')
time.sleep(1)
print('Process started...')
time.sleep(1)
print('Initializing ip ', '-')
time.sleep(1)
print('Initializing ip ', '--')
time.sleep(1)
print('Initializing ip ', '---')
time.sleep(1)
print('Converting ip ', '-')
time.sleep(1)
print('Reconverting ip ', '--')
time.sleep(1)
print('Combining ip ', '---')

if (ips == 0):
    sys.exit("Script Exit...")

if (ips == 1):
    os.system('systemctl stop NetworkManager.service')
    os.system('systemctl disable NetworkManager.service')
    os.system('cd /etc/network')
    if (stat == 'd'):
        fo = open("interfaces", "a")
        strio = fo
        fo.close()
        fo = open("interfaces", "a")
        fo.write("allow-hotplug eth0 \n iface eth0 inet dhcp")
        fo.write("\n", "address ", ip, "\n" , "netmask ", netm, "\n", "gateway ", gate,'\n', "nameservers ", names)
        fo.close()
        os.system('cd /home/')
        pol = open("interfaces", "a")
        fo.write(strio)
        fo.close()
        os.system('cd /etc/')
        pol = open("resolv.conf", "a")
        fo.write("\nnameserver ",name)
        fo.close()
        os.system('service networking restart')

    if (stat == 's'):
        fo = open("interfaces", "a")
        strio = fo
        fo.close()
        fo = open("interfaces", "a")
        fo.write("allow-hotplug eth0 \n iface eth0 inet static")
        fo.write("\n", "address ", ip, "\n" , "netmask ", netm, "\n", "gateway ", gate,'\n', "nameservers ", names)
        fo.close()
        os.system('cd /home/')
        pol = open("interfaces", "a")
        fo.write(strio)
        fo.close()
        os.system('cd /etc/')
        pol = open("resolv.conf", "a")
        fo.write("\nnameserver ",name)
        fo.close()
        os.system('service networking restart')




if (ips == 2):
    os.system('')

if (ips == 3):
    os.system('')

if (ips == 4):
    os.system('')

if (ips == 5):
    os.system('')

if (ips == 6):
    os.system('')

if (ips == 7):
    os.system('')

if (ips == 8):
    os.system('')
