#coding=utf-8
import sys
import time
import socket
from lib.Is_Result import is_result

data = time.strftime('%m-%d',time.localtime(time.time()))
is_result()
domain_file = data + "_url.txt"
print domain_file


ip_list=list()
def getIp(domain_file):
    f = open(domain_file, 'r')                   #以读方式打开文件
    for line in f.readlines():
        line = line.strip()
        print(line)
        try:
            myaddr = socket.getaddrinfo(line,'http')[0][4][0]
            ip_list.append(myaddr)
            ip_list.sort()
            open(data+'_ip_file.txt','w').write('%s'%'\n'.join(ip_list))
            # print line
            print myaddr
        except:
            pass




getIp(domain_file)