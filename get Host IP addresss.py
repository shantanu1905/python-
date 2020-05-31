import socket
print("wank to get ipaddress (y/n)?");
check = input();
if check == "n":
    exit();
else:
    print("\n Your IP address is : ",end="");
    print(socket.gethostbyname(socket.gethostname()));
