#!/usr/bin/env python3

# import the socket module. it lets us use the socket api to check if connection is possible to given ports on a specified ip address.
import socket

# import ipaddress module. it lets us use the ipaddress.ip_address(address) method.
# ipaddress.ip_address(address) tries to instantiate a valid ip address to test.
import ipaddress

# import re module. it lets us create regular expressions to make sure the input is correctly formatted.
import re

# regular expression. this regex pattern will allow us to filter the number of ports to scan.
# specify range from lowest to highest port number ( example: 1-65535 )
port_range_regex = re.compile("([0-9]+)-([0-9]+)")

# initializing the default port numbers.
port_min = 0
port_max = 65535

# if you can connect to it, a port is seen as open.
# no discrimination between filtered and closed ports, no response in both cases.

# user interface header
print("\n****************************************************************")
print("\n* Copyright of Ron Jean-Francois, 2023                         *")
print("\n* https://www.ronjeanfrancois.com                              *")
print("\n* https://www.youtube.com/@ronjf                               *")
print("\n****************************************************************")

# create a container array for the ports considered to be open.
open_ports = []

# ask user for the ip address to be scanned.
while True:
    ip_addr_entered = input("\nPlease enter the ip address you want to scan: ")
    
    # if an invalid ip address is entered, the try-except block will move to except and give that response.
    try:
        ip_address_obj = ipaddress.ip_address(ip_addr_entered)
        # only executes if ip address is valid.
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address!")

while True:
    # you can scan every port from 0 to 65535, however it is not advised to scan all ports, since this scanner does NOT use multithreading.
    print("Please enter the range of ports you want to scan in format: <number>-<number> (ex would be 20-100)")
    port_range = input("Enter the port range you want to scan: ")

    # perform data cleansing/input validation by removing extra white space.
    port_range_clean = port_range_regex.search(port_range.replace(" ",""))

    if port_range_clean:
        # filter the lower input for the port scanner range.
        port_min = int(port_range_clean.group(1))
        # filter the higher input for the port scanner range.
        port_max = int(port_range_clean.group(2))
        break

for port in range(port_min, port_max + 1):
    # create connection to socket of target machine.
    try:
        # create a socket object. socket.AF_INET lets us enter either a domain name or ip address and will then continue with the connection.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # set a timeout (in seconds) for the socket to try and connect to the server. the longer the duration, the better the results.
            s.settimeout(0.5)
            
            # connect to the ip address at the specified port using the socket object. it will cause an exception if it cant connect to this socket.
            s.connect((ip_addr_entered, port))
            # runs if connection to the port was successful and appends the value.
            open_ports.append(port)

    except:
        # if we wanted to do something with the closed ports we would use this section.
        pass

for port in open_ports:
    # we print the results with an f string to format the string with the variables.
    print(f"Port {port} is open on {ip_addr_entered}.")