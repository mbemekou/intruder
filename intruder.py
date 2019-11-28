#! /usr/bin/python
import requests
from Queue import Queue
import threading 
import os
import sys
from termcolor import colored
import argparse
import time
import re
import json
def banner():
	os.system("clear")
	
	print '''
			                               
			 ___       _                  _           
			|_ _|_ __ | |_ _ __ _   _  __| | ___ _ __ 
	 		 | || '_ \| __| '__| | | |/ _` |/ _ \ '__|
	 		 | || | | | |_| |  | |_| | (_| |  __/ |   
			|___|_| |_|\__|_|   \__,_|\__,_|\___|_|   
                                          

    '''
	l="\t\t\t\t\tBy Mbemekou Fred\n"
	u=""
	for b in l:
		u=u+b
		sys.stdout.write('\t\t\t\r'+u)
		sys.stdout.flush()
		time.sleep(0.01)

	print "\n\n"	
	time.sleep(0.3)
def request_parser(req):
	global head
	global is_head
	global is_body
	global body
	global cible
	global method
	global content

	body=''
	is_head=False
	is_body=False
	try:
		f=open(req)
	except Exception, e:
		print e
		sys.exit()
	requete=f.read()
	head=requete.split("\r\n\r\n")[0]
	method=head.split(" ")[0]
	if("^ATTACK^" in head):
		is_head=True
	
	body=requete.split("\r\n\r\n")[1]
	if("^ATTACK^" in body):
		is_body=True
	var=head.split("\r\n")
	h={}
	for header in var:
		if ":" in header:
			h[header.split(":")[0]]=header.split(":")[1].strip(' ')

	for key,value in h.items():
		if "^ATTACK^" in value:
			cible=key
	content=h["Content-Type"]









def requesthandler(donnee):

	global data
	global req
	global get
	global head
	global body
	
	

	if(get):
		r=requests.get(donnee,allow_redirects=False)
		lines=r.content.count("\n")
		chars=len(r.content)
		words=len(re.findall("\S+",r.content))
		code=r.status_code
		sys.stdout.write("\r"+donnee+"                                                                        \r")
		sys.stdout.flush()
		sys.stdout.write("                                                                                  \r")
		if((code != hidecode)&(words!=hideword)&(chars!=hidecharacter)&(lines!=hideline)):
			if(200 <= code <300):
				print(colored(code,'green')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			elif(300 <= code < 400):
				print(colored(code,'blue')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			elif(400 <= code < 500):
				print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			else:
				print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")

	elif(len(data)):
		d=donnee.split("&")
		payload={}
		a=""
		b=""
		for i in d:
			a=i.split("=")[0]
			b=i.split("=")[1]
			payload[a]=b


		r=requests.post(url,data=payload,allow_redirects=False)
		lines=r.content.count("\n")
		chars=len(r.content)
		words=len(re.findall("\S+",r.content))
		code=r.status_code
		sys.stdout.write("\r"+donnee+"                                                                        \r")
		sys.stdout.flush()
		sys.stdout.write("                                                                                  \r")

		if((code != hidecode)&(words!=hideword)&(chars!=hidecharacter)&(lines!=hideline)):
			if(200 <= code <300):
				print(colored(code,'green')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			elif(300 <= code < 400):
				print(colored(code,'blue')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			elif(400 <= code < 500):
				print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
			else:
				print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee)+"\t\t")
	elif(len(req)):
		global content

		if(is_body):
			global method

			
			payload={}
			headers={}
			a=""
			b=""
			if("application/x-www-form-urlencoded" in content):
				d=donnee.strip("\r\n").split("&")
				for i in d:
					a=i.split("=")[0]
					b=i.split("=")[1]
					payload[a]=b
					h=head.split("\r\n")
				for j in h:
					if(":" in j):
						headers[j.split(":")[0]]=j.split(":")[1].strip(" ")
				if(method=="POST"):
					r=requests.post(url,data=payload, headers=headers ,allow_redirects=False)
				elif(method=="GET"):
					r=requests.get(url, headers=headers ,allow_redirects=False)
				elif(method=="PUT"):
					r=requests.put(url,data=payload, headers=headers ,allow_redirects=False)
				elif(method=="PATCH"):
					r=requests.patch(url,data=payload, headers=headers ,allow_redirects=False)
			elif(("application/json" in content) or ("text/plain" in content)):
				payload=json.loads(donnee)
				h=head.split("\r\n")
				for j in h:
					if(":" in j):
						headers[j.split(":")[0]]=j.split(":")[1].strip(" ")

				if(method=="POST"):
					r=requests.post(url,json=payload, headers=headers ,allow_redirects=False)
			
				elif(method=="PUT"):
					r=requests.put(url,json=payload, headers=headers ,allow_redirects=False)
				elif(method=="PATCH"):
					r=requests.patch(url,json=payload, headers=headers ,allow_redirects=False)
			lines=r.content.count("\n")
			chars=len(r.content)
			words=len(re.findall("\S+",r.content))
			code=r.status_code
			sys.stdout.write("\r"+donnee.strip("\r\n")+"\t\t                                                                        \r")
			sys.stdout.flush()
			sys.stdout.write("                                                                                  \r")

			if((code != hidecode)&(words!=hideword)&(chars!=hidecharacter)&(lines!=hideline)):
				if(200 <= code <300):
					print(colored(code,'green')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee.strip("\r\n"))+"\t\t")
				elif(300 <= code < 400):
					print(colored(code,'blue')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee.strip("\r\n"))+"\t\t")
				elif(400 <= code < 500):
					print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee.strip("\r\n"))+"\t\t")
				else:
					print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(donnee.strip("\r\n"))+"\t\t")
		elif(is_head):
			global cible
			d=body.strip("\r\n").split("&")
			payload={}
			headers={}
			a=""
			b=""
			for i in d:
				a=i.split("=")[0]
				b=i.split("=")[1]
				payload[a]=b
			h=donnee.split("\r\n")
			for j in h:
				if(":" in j):
					headers[j.split(":")[0]]=j.split(":")[1].strip(" ")

			r=requests.post(url,data=payload,headers=headers,allow_redirects=False)
			lines=r.content.count("\n")
			chars=len(r.content)
			words=len(re.findall("\S+",r.content))
			code=r.status_code
			sys.stdout.write("\r"+headers[cible]+"                                                                        \r")
			sys.stdout.flush()
			sys.stdout.write("                                                                                  \r")

			if((code != hidecode)&(words!=hideword)&(chars!=hidecharacter)&(lines!=hideline)):
				if(200 <= code <300):
					print(colored(code,'green')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(headers[cible])+"\t\t")
				elif(300 <= code < 400):
					print(colored(code,'blue')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(headers[cible])+"\t\t")
				elif(400 <= code < 500):
					print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(headers[cible])+"\t\t")
				else:
					print(colored(code,'red')+"\t|\t"+str(chars)+"\t|\t"+str(words)+"\t|\t"+str(lines)+"\t|\t{}".format(headers[cible])+"\t\t")





def worker():
	
	while True:
		#print"waiting for worker"
		donnee=q.get()
		#print "worker {} got".format(port)
		if(donnee==None):
			q.task_done()
			break
		requesthandler(donnee)
		q.task_done()


def threadhandler():
	global threads
	global list_threads
	global url
	global words
	global q
	global cible
	global get
	global data
	global req
	global is_head
	global is_body
	if(get):
		print("-------------------------------------------------------------------------------------------------------------------------------")
		print("|code"+"\t|\t"+"chars"+"\t|\t"+"words"+"\t|\t"+"lines"+"\t|\t"+"url"+"\t\t")
		print("-------------------------------------------------------------------------------------------------------------------------------")
	elif(len(data)):
		print("-------------------------------------------------------------------------------------------------------------------------------")
		print("|code"+"\t|\t"+"chars"+"\t|\t"+"words"+"\t|\t"+"lines"+"\t|\t"+"payload"+"\t\t")
		print("-------------------------------------------------------------------------------------------------------------------------------")
	elif(len(req)):
		if(is_head):
			print("-------------------------------------------------------------------------------------------------------------------------------")
			print("|code"+"\t|\t"+"chars"+"\t|\t"+"words"+"\t|\t"+"lines"+"\t|\t{}".format(cible)+"\t\t")
			print("-------------------------------------------------------------------------------------------------------------------------------")
		elif(is_body):
			print("-------------------------------------------------------------------------------------------------------------------------------")
			print("|code"+"\t|\t"+"chars"+"\t|\t"+"words"+"\t|\t"+"lines"+"\t|\t"+"payload"+"\t\t")
			print("-------------------------------------------------------------------------------------------------------------------------------")
				



	for i in range(threads):
		t=threading.Thread(target=worker)
		t.daemon=True
		t.start()
				#print"thead{} started".format(i)
		list_threads.append(t)
	for word in words:
		word=word.strip("\n")
		if(len(data)):
			
			q.put(data.replace("^ATTACK^",word))
		elif(len(req)):
			if(is_body and not(is_head)):
				
				q.put(body.replace("^ATTACK^",word))	
			elif(is_head and not(is_body)):
				
				q.put(head.replace("^ATTACK^",word))
				
			elif(not(is_head) and not(is_body)):
				print("please supply the targeted parameter with the keyword '^ATTACK^'")
				sys.exit(0)
		else:
			word=word+extension
			q.put(url.replace("^ATTACK^",word))



	q.join()

	for i in range(len(list_threads)):
		q.put(None)

	for t in list_threads:
		t.join()


def start(argv):
	global threads
	global url
	global words
	global hidecode
	global hideword
	global hidecharacter
	global hideline
	global data
	global extension
	global req
	global get
	get=False
	banner()
	parser=argparse.ArgumentParser(usage='''
./Intruder.py [-h] -u <target url> -w <wordlist> [-t] <number of threads>
example:
./Intruder.py -u http://127.0.0.1/^ATTACK^ -w /usr/share/wordlist/rockyou.txt -t 50
./Intruder.py -u http://127.0.0.1/login.php?username=admin&password=^ATTACK^ -w rockyou.txt -t 50

		''')
	parser.add_argument("-u",dest="url",required=True,type=str,help="The target url")
	parser.add_argument("--data",dest="data",type=str,help="data parameter for post request",default="")
	parser.add_argument("-w",dest="wordlist",required=True,type=str,help="The wordlist")
	parser.add_argument("-r",dest="req",type=str,help="The burpsuite request",default="")
	parser.add_argument("-t",dest="threads",type=int,help="Number of threads",default=20)
	parser.add_argument("--hc",dest="hidecode",type=int,help="Hide responses with status code",default=404)
	parser.add_argument("--hw",dest="hideword",type=int,help="Hide responses with number of words",default=0)
	parser.add_argument("--hh",dest="hidecharacter",type=int,help="Hide responses with number of characters",default=0)
	parser.add_argument("--hl",dest="hideline",type=int,help="Hide responses with number of lines ",default=0)
	parser.add_argument("-x",dest="extension",type=str,help="add an extension to the wordlist",default="")
	args=parser.parse_args()
	url=args.url
	wordlist=args.wordlist
	threads=args.threads
	hidecode=args.hidecode
	hideword=args.hideword
	hidecharacter=args.hidecharacter
	hideline=args.hideline
	data=args.data
	req=args.req
	if(not len(req) and not len(data)):
		get=True
	if len(req):
		request_parser(req)
	if args.extension=="":
		extension=args.extension
	else:
		extension="."+args.extension

	
	
	try:
		f=open(wordlist)
		words=f.readlines()

	except Exception, e:
		print e
		sys.exit()
	threadhandler()

list_threads=[]	
q=Queue()
start(sys.argv)


 
