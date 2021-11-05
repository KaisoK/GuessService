import socks
import socket
import subprocess

x = open("/home/kaisok/Documentos/Python/Onion/Lista", "r", encoding="latin-1")
url = x.readlines()
x.close()
subprocess.run("clear")

for i in url:
    nombre = i.strip("\n")
    i = i.split(" ")[1].strip("\n")
    
    try:
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
        s = socks.socksocket()
        s.connect(('{}'.format(i), 8000))
        a = s.recv(1024).decode()

        if "SSH" in a:
            print("\n#######################")
            print("\n" + nombre)
            print("\nEs SSH")
            print("\n#######################")

        elif "FTP" in a:
            print("\n#######################")
            print("\n" + nombre)
            print("\nEs FTP")
            print("\n#######################")

        else:
            print("\n#######################")
            print("\n" + nombre)
            print("Otro servicio")
            print("\n#######################")
        s.close()
    
    except:
        print("\n#######################")
        print("\n{}\n\nHost inaccesible".format(nombre))
        print("\n#######################")
