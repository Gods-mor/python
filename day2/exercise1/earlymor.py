# 猜年龄小游戏，有三点需求
# 1.允许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y,就继续让其猜三次，以此往复，如果回答N或n,就退出程序
# 3.如果猜对了，就直接退出
age=18#设置年龄
tag=1

while tag:
    print('猜猜我的年龄')
    times=3

    #三次机会
    while times:

        #用户输入
        will=0
        guess=int(input())

        #对比结果
        if guess==age:
            print('猜对了')
            tag=0
            break
        elif guess<age:
            print('猜小了')
        else :
            print('猜大了')
        times-=1
        
        #结束语
    else :
        print('是否继续(回答Y或y继续/如果回答N或n退出)')
        while will==0:
            key=input()
            if key=='Y' or key=='y':
                will=1
            elif key=='N' or key=='n':
                will=1
                tag=0
                break
            else :
                print('输入格式不正确')
                print('请重新输入')


