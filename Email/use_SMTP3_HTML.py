#通过MIMEText构造一个纯文本文件
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)   #用来解析字符串中email的地址
    return formataddr((Header(name,'utf-8').encode(),addr))    #将email地址转为utf-8(防止中文乱码)

from_addr = 'barryember@163.com'
password = 'zxs199325yb'
to_addr = '810386053@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('<html><body><h1>Hello, my friend...</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('赵伟<%s>'% from_addr)
msg['To'] = _format_addr('赵伟<%s>'% to_addr)
msg['Subject'] = Header('SMTP测试1','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)     #邮箱默认端口25
server.login(from_addr,password)          #登陆
server.sendmail(from_addr,[to_addr],msg.as_string())    #发送
server.quit()   #退出

