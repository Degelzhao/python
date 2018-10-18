#通过MIMEText()构造一个纯文本邮件
from email.mime.text import MIMEText
#参数1:邮件正文  参数2:邮件类型('plain'表示纯文本  参数3:编码格式
msg = MIMEText('Hello, my friend','plain','utf-8')

#发送邮件地址
from_addr = 'barryember@163.com'

#邮件授权码，非登陆密码
password = 'zxs199325yb'

#收件箱地址
to_addr = '810386053@qq.com'

#stmp服务器
smtp_server = 'smtp.163.com'

#发送邮件地址
msg['From'] = from_addr
#收件箱地址
msg['To'] = to_addr
#主题
msg['Subject'] = 'for testing'

import smtplib
#SMTP默认端口是25
server = smtplib.SMTP(smtp_server,25)
#打印出和SMTP服务器交互的所有信息
#server.set_debuglevel(1)
print(from_addr)
print(password)
#登陆SMTP服务器
server.login(from_addr,password)
#发邮件,传入一个list代表可以一次发给很多人，邮箱正文:as_string将MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()