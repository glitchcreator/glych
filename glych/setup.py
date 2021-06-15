from re import sub
import subprocess
import pyfiglet
print('installing scapy...')
subprocess.call('pip3 install scapy', shell=True)
print('installing socket...')
subprocess.call('pip3 install sockets',shell=True)
print('installing colorama...')
subprocess.call('pip3 install colorama', shell=True)
print('installing datetime...')
subprocess.call('pip3 install datetime', shell=True)

