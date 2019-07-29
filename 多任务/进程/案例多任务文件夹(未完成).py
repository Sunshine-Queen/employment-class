import os
import multiprocessing

def copy_file(file_name):
    "完成文件的复制"
    print("=====模拟复制文件：%s"%file_name)
def main():
    #1.获取用户要copy的文件夹的名字
    old_folder_name=input("请输入要copy文件夹的名字：")
    #2.创建一个新的文件夹
    try:
        os.mkdir(old_folder_name+"[附件]")
    except:
        pass
    #3.获取文件夹的所有待copy的文件名字 listdir()
    file_names=os.listdir(old_folder_name)
    print(file_names)
    #4.创建进程池
    po=multiprocessing.Pool(5)
    #5.向进程池中copy文件任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(file_name,))

    #复制原文件夹的文件，到新文件夹中的文件去

if __name__ == '__main__':
        main()