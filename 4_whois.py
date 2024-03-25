import socket

domain=input("Inser your link here: ")

def mywhois(domain: str):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("whois.iana.org",43))
    s.send(f"{domain}\r\n".encode())
    response=s.recv(4096).decode()
    s.close()
    return response

print(mywhois(domain))

#write in file method 1
with open("whois.txt","w") as f:
    output=mywhois(domain)
    f.write(output)

#write in file method 2

f=open("whois.txt","w")
f.write(mywhois(domain))
f.close()

#append to file
#f.read()
domain=input("Inser your link here for append: ")

f=open("whois.txt","a")
f.write(mywhois(domain))
f.close()


import validators
import whois

dm=input("Inser your domain here: ")

def domain_lookup(dm):
    if validators.domain(dm):
    #try:
        dm_info = whois.whois(dm)
        #write in file method 2
        f=open("whois_module.txt","w")
        f.write(str(dm_info))
        f.close()
        return dm_info
    # except:
        #  return f"{dm} is not a valid domain!"
    else:     
        return "Enter a valid domain"

print(domain_lookup(dm))