# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:00:39 2018

@author: rwang
"""

def get_email_data(filename,index,path_out):
    fp = open(filename, "r")
    msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码
    
    subject = msg.get("subject") # 取信件头里的subject,　也就是主题
    h = email.header.Header(subject)
    subject=make_header(decode_header(str(h)))
    date=msg.get('Date')
#    date = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
    from_user=email.utils.parseaddr(msg.get("from"))[1]
#    to_user=email.utils.parseaddr(msg.get("to"))[1]
    tos = msg.get_all('to', [])
    ccs = msg.get_all('cc', [])
    resent_tos = msg.get_all('resent-to', [])
    resent_ccs = msg.get_all('resent-cc', [])
    all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)
    all_list=[rec[1] for rec in all_recipients]
    email_data=[]
    for to_user in all_list:   
        data=[str(index),from_user,to_user,str(subject),str(date),filename]
        email_data.append('\t'.join(data))
    email_data='\n'.join(email_data)   
    
#    email_data=[str(index),from_user,to_user,str(subject),date]
#    email_data='\t'.join(email_data)
    f_content=open(path_out+'/'+str(index)+'_'+str(subject)+'_content.txt', 'w',encoding='utf-8')
    f_content_all=open(path_out+'/'+'all_content.txt', 'a',encoding='utf-8')
    output=''
    for par in msg.walk():
        if not par.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
            name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
            content_Type = par.get_content_type()  
            charset=par.get_content_charset(); 
            if name:#有附件
                # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                h = email.header.Header(name)
                fname=make_header(decode_header(str(h)))
                print('附件名:', fname)
                data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中

                try:
                    f = open(path_out+'/'+str(index)+'_'+str(fname), 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                except:
                    print('附件名有非法字符，自动换一个')
                    f = open(path_out+'/'+str(index)+'_aaaa', 'wb')
                f.write(data)
                f.close()
            else:     
                if content_Type in ['text/plain'] or content_Type in ['text/html']:              
                    if charset:
                        content = par.get_payload(decode=True).decode(charset)
                        if len(content)>0:
                            f_content.write(content+'\n')
                        if content_Type in ['text/plain']:
                            p=re.compile('\s+')
                            output=re.sub(p,'',content)
#                            output="".join(output.split())
#                            output=content.replace('\t','').replace('\n','').replace(' ','')
                            if len(output)>0:
                                f_content_all.write(str(index)+' '+output)
                                f_content_all.write('\n')
                    else:
                        content = par.get_payload(decode=True)
                        print('sAttachment: %s' % (content_Type))
                 
    f_content.close()
    f_content_all.close()
    fp.close()
    
    return email_data

#%%
import os
import email
from email.header import decode_header, make_header
from email.utils import getaddresses
import time
from os import walk
import re
from datetime import datetime

path_in=r'C:\code\email'
filename=os.path.join(path_in,"example.eml")
path_out=r'C:\code\email\output'

os.chdir(path_in)
if os.path.exists(path_out+'/'+'all_content.txt'):
    os.remove(path_out+'/'+'all_content.txt')

start=time.time()
if  not os.path.exists(path_out):
    os.makedirs(path_out)

file = open(path_out+'/email_all_table.txt', 'w',encoding='utf-8')

if os.path.isfile(filename):
    email_data=get_email_data(filename,1,path_out)
    file.write(email_data)
    file.write('\n')
file.close()        
stop=time.time()
print('用时：%f秒'%(stop-start))

