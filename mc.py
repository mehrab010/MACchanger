import optparse
import re
import netifaces
import subprocess
import os
import time
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface" , dest= "interface", help="plase get a MAC addres white -i or --interface")
    parser.add_option("-m","--mac", dest= "new_MAC", help= "plasse get a interface white -m or --mac")
    (options,args) = parser.parse_args()
    if not options.interface:
        parser.error("false i")
    if not options.new_MAC:
        parser.error("false m")
    if options.interface not in get_interface():
        parser.error("get i True")
    if not re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w",options.new_MAC):
        parser.error("get m True")
    return options
def get_interface():
    return netifaces.interfaces()
    
def change_MAC(inter,MAC):
    print("[+] MAC is changing")
    subprocess.run(["sudo" , "ifconfig" , inter , "down"],shell=True)
    subprocess.run(["sudo" , "ifconfig" , inter, "hw" , "ether" , MAC])
    subprocess.run(["sudo" , "ifconfig" , inter , "up"],shell=True)
    os.system("clear")
    wait(options.new_MAC)
def wait(new_MAC):
    print("[?] waiting for changing .")
    time.sleep(0.5)
    os.system("clear")
    print("[?] waiting for changing ..")
    time.sleep(0.7)
    os.system("clear")
    print("[?] waiting for changing ...")
    time.sleep(0.9)
    os.system("clear")
    print("[?] waiting for changing ....")
    time.sleep(1.1)
    os.system("clear")
    print("[?] waiting for changing ....")
    time.sleep(1.5)
    os.system("clear")
    print("[?] waiting for changing .....")
    time.sleep(0.5)
    print("\n"+"\n")
    print("[+] FINISHED")
    print("[+] Your Mac address changed to "+new_MAC)
options = get_args()


change_MAC(options.interface,options.new_MAC)
        
