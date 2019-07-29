def create_num(all_num):
    a,b=0,1
    current_num=0
    while current_num<all_num:
        yield a #如果一个函数中有yield语句，那么这个就不在是函数，而是生成器模板
        a,b=b,a+b
        current_num+=1
    return "ok...."
obj2=create_num(50)
while True:
    try:
        ret=next(obj2)#next唤醒
        print(ret)
    except Exception as ret:
        print(ret.value)
        break