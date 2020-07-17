# msg='上课啦，认真听讲！！！'
# # encode and decode
# #gbk中文 gb2312 简体中文 utf-8 unicode
# result=msg.encode('utf-8')
# print(result)
# 	#解码
# result_1=result.decode('utf-8')#一般在网络应用
# print(result_1)

# #startswith and endswith
# #startswith 是判断用什么开头 and endswith判断用什么结尾返回值都是布尔类型
# # filename='笔记.doc'
# # result_2=filename.startswith('txt')
# # print(result_2)
# # path=input('请选择文件')
# # filename_1=path[path.rfind('\\')+1:]
# # print(filename_1)
# #  list_1=[]
# while True:
# 	usename=input('请输入用户名')
# 	usepassword=input('请输入用户密码')
# 	useremail=input('请输入用户邮箱')
# 	if len(usename)>20 or len(useremail)>20 or len(usepassword)>20:
# 		print('输入不正确')
# 	else:
# 		print("{}\t{}\t{}".format(usename,usepassword,useremail))
# # 		break		
# brands=['hp','dell','email','thinkpad','lenovo','mac','神州','华为']
# # print(brands)
# # brands[-1]='HASSEE'
# # print(brands)
# # # for brand in brands:
# # # 	if '华为' in brand 
# # 	# 此处要结合下标
# # for i in range(len(brands)):
# # 	if'华为'in brands[i]:
# # 		print(i)
# # 		brands[i]='huawei'
# # print(brands)
# W=input('请输入一个要删除的单词')
# i=0
# l=len(brands)
# # while i<l:
# # 	for word in brands:
# # 			if W in word:
# # 				del brands[i]
# # 				l-=1
# # 				i+=1
# while i<l:
# 	if W in brands[i]:
# 		del brands[i]
# 		l-=1
# 		continue
# 	i+=1
# print(brands)
# girl=[]
# while True:
# 	name=input('请输入你心目中女孩子的名字')
# 	if name =='quiet':
# 		break
# 	girl.append(name)

# print(girl)
# girl.insert(1,'李永泰')
# print(girl)
# import random
# list_1=[]
# for x in range(10):
# 	ran=random.randint(1,50)
# 	list_1.append(ran)
# print(list_1)
# new_list_1=sorted(list_1)
# print(new_list_1)
# a=[3,4,5,6,7,8,9,11,13,15,17]
# print(a[8:-9:-1])
# #  
# brand ={}
# brand['name']='huawei'
# print(brand)
print('-'*30)
datebase=[]
while True:
	usename=input('请输入用户名')
	usepassword=input('请输入用户密码')
	reusename=input('请再次确认密码')
	email=input('请输入用户邮箱')
	phone=input('请输入电话号码')
	user={}
	user['usename']=usename
	if usepassword==reusename:
		user['password']=usepassword
	else:
		print('密码不一致')
		continue
	user['email']=email
	user['phone']=phone
	datebase.append(user)
	print(datebase)
	