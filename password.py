i = 2
password = 'a123456'
while i < 3 and i >= 0 :
	pwd = input('請輸入密碼: ')
	if pwd != password:
		print('密碼錯誤，還有', i, '次機會')
		i = i - 1
	else:
		print('登入成功!')
		break