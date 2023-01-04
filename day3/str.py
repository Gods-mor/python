#capitalize 大写第一个字母，小写其他字母
a='hello,world'
print(a.capitalize())
#title
print(a.title())
#打印Hello , world
#strip 跳过前后空格 lstrip删除左空格，rstrip删除右空格
a='  hello,world  '
print(a.strip())
print(a.lstrip())
print(a.rstrip())
#id() 变量地址
b=a
print('%d'%id(a))
print('%d'%id(b))
a='Hello,world'
print('a:%d'%id(a))
print('b:%d'%id(b))
print('a:'+a)
print('b:'+b)
#find() 找到元素下标
print(a.find('o'))#4第一个o的下标
print(a.find('x'))#-1未找到
#index
print(a.index('o'))#4第一个o的下标
'''
print(a.index('x'))报错
'''
#replace
print(a.replace('Hello', 'hELLO'))
print(a.replace('hello', 'HELLO', 1))
print(a.replace('l', 'L', 2))
#split
print(a.split('o'))
print(a.split('o',1))
