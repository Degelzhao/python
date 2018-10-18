from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)                                 #解析邮件地址，name为邮件人，addr为邮件地址
    return formataddr((Header(name,'utf-8').encode(),addr))   #格式化邮件地址

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('Hello, Degel...','plain','utf-8')
msg['From'] = _format_addr('赵伟 <%s>' % from_addr)
msg['To'] = _format_addr('赵伟 <%s>' % to_addr)
msg['Subject'] = Header('SMTP测试', 'utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()