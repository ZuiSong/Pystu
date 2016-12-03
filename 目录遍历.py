import os
# os.mkdir('file') 创建文件夹
# os.mkdir('file/abc')在file下创建abc目录
# os.makedirs('file2/abc')  创建目录树，
# os.rmdir('file/abc') 删除目录abc
# os.rmdir('file') 删除目录file
# os.removedirs("file2/abc")删除目录树
# os.listdir(".") 列出当前目录下的文件、文件夹
# os.getcwd() 获取但前路径
# os.chdir('/')  切换目录到根目录


def visitfiletree(path, layer):
    os.chdir(path)
    cwd = os.getcwd()
    filenames = os.listdir()
    # print(filenames)
    for filename in filenames:

        for i in range(layer):
            print('', end='  ')

        print(filename)
        if os.path.isdir(cwd + '/' + filename):
            visitfiletree(cwd + '/' + filename, layer + 1)


if __name__ == '__main__':
    path = 'D:/Personal/Desktop/'
    visitfiletree(path, 0)
