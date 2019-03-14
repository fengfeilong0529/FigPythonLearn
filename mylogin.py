username = input('请输入用户名：')
userpwd = input('请输入用户密码：')

print(username)
print(userpwd)

print('---------开始登陆---------')

# inputUsername = input('请输入登陆账户：')
# inputUserpwd = input('请输入登陆密码：')

flag1 = 0  # 密码输入错误次数统计
flag2 = 0  # 登陆成功标记
successFlag = False

while True:
    inputUsername = input('请输入登陆账户：')
    if username == inputUsername:
        while flag1 < 3:
            inputUserpwd = input('请输入登陆密码：')
            if inputUserpwd == userpwd:
                print('登陆成功！！！')
                flag2 = 1
                break
            else:
                flag1 = flag1 + 1
                if flag1 <= 2:
                    print("密码错误，请重新输入")
        else:
            print('已输入错误3次，请重新登陆')
            flag1 = 0
        if flag2 == 1:
            break
    else:
        print('用户名错误，请重新输入用户名：')
