import subprocess
import optparse
import re



def get_args():
	parser=optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface",help="Interface for which mac address have to change")
	parser.add_option("-m","--mac",dest="new_mac",help="Enter new mac address")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] please specify an interface, use --help for more info")
	elif not options.new_mac:
		parser.error("[-] Please specify a new mac address , use --help for more info")
	
	return options
	

		

def change_mac(interface,new_mac):
	print "[+] Changing Mac Address to ->", new_mac
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])
	


def get_current_mac(interface):
	ifconfig_result=subprocess.check_output(["ifconfig",interface])	
	current_mac=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result)
	
	if current_mac:
		return current_mac.group(0)
	else:
		print"[-] Could not find mac address"

options=get_args()
current_mac= get_current_mac(options.interface)

change_mac(options.interface,options.new_mac)

current_mac= get_current_mac(options.interface)
if current_mac == options.new_mac:
	print"[+] Mac address changed to " ,current_mac
else:
	print"[-] Could not change Mac address to " ,current_mac

