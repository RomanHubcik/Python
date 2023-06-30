#/usr/bin/env python
import os
import time
import subprocess
import xml.etree.ElementTree as ET


tree = ET.parse('esi.xml')

print("\n")
#1. Check: On clean and fresh installation, no processes should be evaluated higher than eval 5, except files from %programfiles%\windowsapps\
#   Reason: Most system files must be evaluated 1, but for Windows store apps 5-6 is allowed. Higher eval may indicate error in collecting processes/modules
proccount = 0
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Running Processes'):
		continue
	for process in section:						
		if not (process.tag == 'NODE' and process.attrib['NAME'] == 'Process'):
			continue			
		if process.attrib['EVAL'] > '5':
			proccount += 1
			print("1. Error: The process", process.attrib['VALUE'], "has EVAL>5.")


#2. Check: Process evaluated higher than 1 has more than 1 module
#   Reason: This may indicate that full process path wasn't extracted, process denied access to handle or other error
processcnt = 0
modulecnt = 0
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Running Processes'):
		continue
	for process in section:						
		if not (process.tag == 'NODE' and process.attrib['NAME'] == 'Process' and process.attrib['EVAL'] > '1'):
			continue
		processcnt += 1
		for module in process:
			modulecnt += 1
		if processcnt > 0 and modulecnt < 1:
			print("2. Error: The process",process.attrib['VALUE'],"with EVAL=",process.attrib['EVAL'],"has",modulecnt,"modules.")
			

#3. Check: There is process services.exe, evaluated 1, signed by Microsoft
#   Reason: Detection of processes works, check of digital signature works
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Running Processes'):
		continue
	for process in section:						
		if not (process.tag == 'NODE' and process.attrib['NAME'] == 'Process' and process.attrib['VALUE'] == 'services.exe'):
			continue
		if process.attrib['EVAL'] == '1':
			serviceseval = True
		else:
			serviceseval = False
			print("3. Error: The process services.exe has EVAL <> 1.")


#4. Check: There are more than 1 process svchost.exe in TCP or UDP connection
#   Reason: Network connection enumeration works
svchostcount = 0
tcpcount = 0
udpcount = 0

#TCP count
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Network Connections'):
		continue		
	for subsection in section:						
		if not (subsection.tag == 'NODE' and subsection.attrib['VALUE'] == 'TCP Connections'):
			continue	
		for node in subsection:
			if node.attrib['NAME'] == 'svchost.exe':
				tcpcount += 1

#UDP count
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Network Connections'):
		continue		
	for subsection in section:						
		if not (subsection.tag == 'NODE' and subsection.attrib['VALUE'] == 'UDP Connections'):
			continue	
		for node in subsection:
			if node.attrib['NAME'] == 'svchost.exe':
				udpcount += 1			

svchostcount = udpcount + tcpcount

if svchostcount < 1:
	print("4. Error: Network connection enumeration failed.")


#5. Check: There are at least 20 drivers and no one should have eval > 1
#Reason: Registry enumeration works, digital signature check works also for .sys files
drvcount = 0
#evalcount = 0
root = tree.getroot() 
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Drivers'):
		continue
	for node in section:
		if node.attrib['EVAL'] == '1':
			#evalcount += 1
			drvcount += 1 
			print("5. Error: There is less than 20 drivers with EVAL = 1")


#6. Check: System Scheduler Tasks contains at least 40 tasks
#   Reason: XML parser works, scheme of scheduled tasks doesn't change
#### Done in Robot Framework ####


#7. Check: System Information > Installed Software contains some software (at least ESET Security)
#   Reason: Registry enumeration works and registry scheme for installed software doesn't change over time
occur = 0
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'System Information'):
		continue		
	for subsection in section:						
		if not (subsection.tag == 'NODE' and subsection.attrib['VALUE'] == 'Installed Software'):
			continue	
		for node in subsection:						
			if "ESET" in node.attrib['VALUE']:
				occur += 1
		if occur == 0:
			print("7. Error: There is no ESET product installed.")		


#8. Check: Hidden Selfdiag section contains node SDV0008 with value 1 and SDV0009-SDV0011 with value 0
#   Reason: Detection of LiveGrid works and LG service response without error
selfdiagcount = 0
root = tree.getroot()
for section in root:
	if not (section.tag == 'NODE' and section.attrib['VALUE'] == 'Selfdiag'):
		continue
	for node in section:						
		if (node.attrib['NAME'] == 'SDV0008' and node.attrib['VALUE'] != '1'):
			selfdiagcount +=1
			print("8. Error: The value of SDV0008 is", node.attrib['VALUE'], "--> Should be 1.")
			
		if (node.attrib['NAME'] == 'SDV0009' and node.attrib['VALUE'] != '0'):
			selfdiagcount +=1
			print("8. Error: The value of SDV0009 is", node.attrib['VALUE'],"--> Should be 0.")

		if (node.attrib['NAME'] == 'SDV0010' and node.attrib['VALUE'] != '0'):
			selfdiagcount +=1
			print("8. Error: The value of SDV0010 is", node.attrib['VALUE'],"--> Should be 0.")

		if (node.attrib['NAME'] == 'SDV0011' and node.attrib['VALUE'] != '0'):
			selfdiagcount +=1
			print("8. Error: The value of SDV0011 is", node.attrib['VALUE'],"--> Should be 0.")
	

#9. Check: About section contains at least 10 modules (or 15 lines)
#   Reason: Collecting of product modules must work with all our products, on all systems and architecture
#### Done in Robot Framework ####


#10. Check: Log generaton takes less than 15 minutes
#  Reason: This should be enough even for weak hardware and full OS. Otherwise something may hang
#### Done in Robot Framework ####

