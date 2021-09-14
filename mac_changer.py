import subprocess
import optparse






def get_args():
	parser=optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface",help="Interface for which mac address have to change")
	parser.add_option("-m","--mac",dest="new_mac",help="Enter new mac address")
	return parser.parse_args()
	

		

def change_mac(interface,new_mac):
	print "[+] Changing Mac Address to ->", new_mac
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])
	
(options,arguments)=get_args()
change_mac(options.interface,options.new_mac)


