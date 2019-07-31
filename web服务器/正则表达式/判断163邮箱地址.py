import re

def main():
    email = input("请输入一个邮箱地址：")
    #如果在正则表达式中需要用到某些普通的字符，比如.比如?等，仅仅需要在他们前面添加一个反斜杠进行转义
    ret = re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$",email)
    if ret:
        print("%s符合要求..."%email)
    else:
        print("%s不符合要求..."%email)

if __name__ == '__main__':
    main()