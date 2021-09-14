import subprocess
import optparse






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
	print ("[+] Changing Mac Address to ->", new_mac)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])
	
options=get_args()
change_mac(options.interface,options.new_mac)


