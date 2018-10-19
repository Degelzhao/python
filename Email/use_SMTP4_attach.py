from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart     #MIMEMultipart代表邮件本身
from email.mime.text import MIMEText               #MIMEText代表邮件正文
from email.mime.base import MIMEBase               #MIMEBase代表邮件附件
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)    #用来解析字符串中email的地址
    return formataddr((Header(name,'utf-8').encode(),addr))    #将email地址转为utf-8(防止中文乱码)

from_addr = 'barryember@163.com'
password = 'zxs199325yb'
to_addr = '810386053@qq.com'
smtp_server = 'smtp.163.com'

#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('赵伟<%s>' %from_addr)
msg['To'] = _format_addr('赵伟<%s>' %to_addr)
msg['Subject'] = Header('你的图片发了...','utf-8').encode()
#邮件正文
#msg.attach(MIMEText('给你发了一张好看图片','plain','utf-8'))     #将图片当作附件发送

#将图片直接镶嵌到邮件正文中，引入src = "cid:0",如果有多个附件作为图片嵌入了，可以给它们依次编号，然后引入不同的cid:x即可
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

#添加附件就是加上一个MIMEBase,从本地读取一张图片
with open(r'D:\games\porsche.png','rb') as f:
    # 创建MIMEBase对象，即附件内容
    mime = MIMEBase('image','png',filename = 'porsche.png')
    mime.add_header('Content-Disposition', 'attachment', filename='porsche.png')
    #添加必要的头文件
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    mime.set_payload(f.read())  #读进附件的内容
    encoders.encode_base64(mime)  #用base64编码
    msg.attach(mime)  #把附件添加到主体对象中

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#遇到的问题:
#1.附件的路径报错：with open('D:\games\porsche.png','rb') as f:
#原因:\字符默认为转义字符,但是我们不需要转义，只需表示出路径
#解决方法:在路径前面加'r'，表示不转义

#2.SMTP554错误:信封发件人和信头发件人不匹配
#需要调整程序发件人的名字和SMTP服务器上的一致


