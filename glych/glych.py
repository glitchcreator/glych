from re import sub
import pyfiglet
import socket
import subprocess
import sys
import termcolor
import colorama
from colorama import Fore
from datetime import datetime
from classes import colour
import smtplib
import smtplib, ssl
import os

banner=pyfiglet.figlet_format('glych')
print(banner)
tool=input('tool( -h for help): ') 


if tool=='port_scanner':
    port_banner=pyfiglet.figlet_format('port scanner')
    # Clear the screen
    subprocess.call('clear',shell=True)
    print(port_banner)
    # Ask for input
    remoteServer    = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    # Print a nice banner with information on which host we are about to scan
    print ("-" * 60)
    print ("Please wait, scanning remote host"), remoteServerIP
    print ("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1,1025):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print (colour.CGREEN+"[+]Port {}: 	 Open".format(port))
            
            else:
                print(colour.CRED+'[-]port {}:     close'.format(port))
            sock.close()
    except KeyboardInterrupt:
        print ("exiting...//")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print ('Scanning Completed in: '), total
    




elif tool == '-h':
    subprocess.call('clear', shell=True)
    help_banner=pyfiglet.figlet_format('need help?')
    print(help_banner)
    print('port_scanner == port scanner')


elif tool=='ping':
    subprocess.call('clear', shell=True)
    banner_ping=pyfiglet.figlet_format('ping')
    print(banner_ping)
    ip_for_ping=input('[+]what ip do you want to ping: ')
    subprocess.call('ping '+ ip_for_ping,shell=True) 
    if KeyboardInterrupt:
        print('okay bye!!')



else:
    print(colour.CRED+'[-]invalid arg')



if KeyboardInterrupt:
    leave_banner=pyfiglet.figlet_format('cya!!')
    print(leave_banner)
    print(colour.CBEIGE2+'glad to work with you')

