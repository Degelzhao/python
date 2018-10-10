'regular expression practice'

__author__ = 'Degel zhao'

import re

#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

def is_valid_email(addr):
	if re.match(r'(^\w*\.?\w*)@(\w*).(com)$',addr):
		return True

	else:
		return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


#提取出带名字的Email地址：
def name_of_email(addr):
	result = re.match(r'<?(((\w*\s+\w*)|\w*))>?(\s+)?(\w*)?@(\w*).(\w*)$',addr)
	return result.group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
     
        
            
            
        
            