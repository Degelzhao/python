from email.parser import Parser            # 解析模块
from email.header import decode_header     # 用于获取头文件的编码信息
from email.utils import parseaddr         # 用于格式化邮件信息

import poplib

# 准备登陆POP3服务器的相关信息
email = 'barryember@163.com'
password = 'zxs199325yb'
pop3_server = 'pop.163.com'

# 针对邮件相关信息，比如Subject, name等，进行解码


def decode_str(s):
    # decode_header()返回一个list

    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)          # 如果文本中存在编码信息，则进行相应的解码
    return value

# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示


def guess_charset(msg):
    charset = msg.get_charset()                # 用get_charset()方法获取编码
    if charset is None:                        # 如果获取不到，则在原始文本中寻找
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')    # 找'charset='这个字符串
        if pos >= 0:                           # 如果有，则获取该字符串后面的编码信息
            charset = content_type[pos + 8:].strip()
    return charset

# 递归打印出Message的层次结构


def print_info(msg, indent=0):                 # indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':          # 解码主题信息
                    value = decode_str(value)
                else:                          # 解码发件人和收件人信息
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))      # '  ' *indent可以打印出2*indent个空格
    # 将组合邮件对象分离
    if (msg.is_multipart()):
        parts = msg.get_payload()              # 拿取msg的子对象
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()  # 获取邮件对象格式
        if content_type == 'text/plain' or content_type == 'text/html':  # 如果为文本邮件，则直接打印
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)       # 检测编码
            if charset:
                content = content.decode(charset)   # 解码
            print('%sText: %s' % ('  ' * indent, content + '...'))  # 打印内容
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))   # 否则为附件，获取附件信息

# 连接POP3服务器


server = poplib.POP3(pop3_server)


print(server.getwelcome().decode('utf-8'))       # 打印POP3服务器欢迎信息

# 进行身份验证
server.user(email)
server.pass_(password)

# 返回邮箱的相关信息
print('Messages: %s. Size: %s' % server.stat())   # stat()返回邮件数目和占用空间
resp, mails, octets = server.list()              # list()返回所有邮件的编号
print(mails)                                     # 打印所有邮件编号和相应大小

# 获取一封邮件
index = len(mails)                               # index为邮件总数目
resp, lines, octets = server.retr(index)         # 获取最新一封邮件的信息，lines存储了邮件的原始文本的每一行
msg_content = b'\r\n'.join(lines).decode('utf-8')  # 获得整个邮件的原始文本

# 稍后解析出邮件
msg = Parser().parsestr(msg_content)
print_info(msg)
server.quit()


# 小结
# Python用POP3收取电子邮件分两步:
# 1.使用poplib下载邮件原始文本
# 2.使用email把原始文本解析为Message对象，然后将内容展示给用户
