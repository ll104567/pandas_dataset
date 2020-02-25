import requests_html
import re

s = requests_html.HTMLSession()
a = s.get('https://zhuanlan.zhihu.com/p/76905282')
f = open('step1-5.txt','w')
x = re.findall('步骤[^"]*',a.text)
for i in x[:len(x)//2]:
    f.write(i+'\n')


a = s.get('https://zhuanlan.zhihu.com/p/76929640')
f = open('step6-10.txt','w')
x = re.findall('步骤[^"]*',a.text)
for i in x[:len(x)//2]:
    f.write(i+'\n')

print('Raw Data:{}\t{}'.format('step1-5.txt','step6-10.txt'))
