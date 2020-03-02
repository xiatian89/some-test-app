import os
import sys


#计算当前目录下文件数
def filecount(cur_dir):
    return sum([len(files) for dirpath, dirnames, files in os.walk(cur_dir)])


#打印当前目录下的文件树形结构
def display_file(cur_dir, type_id=0):
    for dirpath, dirnames, files in os.walk(cur_dir):
        #print(os.path.split(dirpath))
        file_count = filecount(dirpath)
        level = dirpath.replace(cur_dir, '').count(os.sep)
        indent = '  |' * level + '|-----'
        print("{0}{1} 文件数:{2}".format(indent,
                                      os.path.split(dirpath)[1], file_count))
        for file in files:
            indent = '  |' * (level + 1) + '|-----'
            print("{}{}".format(indent, file))


#添加前缀
def add_pre_mark(cur_dir):
    pre = input("请输入需要添加的前缀：")
    mark = "{}".format(pre)
    for dirpath, dirnames, files in os.walk(cur_dir):
        os.chdir(dirpath)
        for filename in files:
            os.renames(filename, mark + filename)


#删除前缀
def del_pre_mark(cur_dir):
    pre = input("请输入需要删除的前缀：")
    mark = "{}".format(pre)
    for dirpath, dirnames, files in os.walk(cur_dir):
        os.chdir(dirpath)
        for filename in files:
            if mark == filename[:len(mark)]:1111
                os.rename(filename, filename[len(mark):])
    pass


#文件名加后缀
def add_post_mark(cur_dir):
    post = input("请输入需要添加的后缀：")
    mark = "{}".format(post)
    for dirpath, dirnames, files in os.walk(cur_dir):
        os.chdir(dirpath)
        for filename in files:
            filename_tmp = filename.split(".")
            filename_tmp[-2] += mark
            filename_New = ".".join(filename_tmp)
            os.rename(filename, filename_New)
    pass


#删除后缀名
def del_post_mark(cur_dir):
    post = input("请输入需要删除的后缀：")
    mark = "{}".format(post)
    for dirpath, dirnames, files in os.walk(cur_dir):
        os.chdir(dirpath)
        for filename in files:
            filename_tmp = filename.split(".")
            if mark == filename_tmp[-2][-len(mark):]:
                filename_tmp[-2] = filename_tmp[-2][:-len(mark)]
                filename_New = ".".join(filename_tmp)
                os.rename(filename, filename_New)
    pass


#修改文件扩展名
def rename_file_exten(cur_dir):
    exten_Old = "{}".format(input("请输入需要修改的扩展名："))
    exten_New = "{}".format(input("请输入修改后的扩展名："))
    files = os.listdir(cur_dir)
    os.chdir(cur_dir)
    for filename in files:
        if not os.path.isdir(filename):
            filename_tmp = filename.split(".")
            if exten_Old == filename_tmp[-1]:
                filename_tmp[-1] = exten_New
                filename_New = ".".join(filename_tmp)
                os.rename(filename, filename_New)
    pass


#文件名中字段替换
def rename_file(cur_dir, KeyWord_Old, KeyWord_New=''):
    for dirpath, dirnames, files in os.walk(cur_dir):
        os.chdir(cur_dir)
        for filename in files:
            filename = os.path.join(dirpath, filename)
            if KeyWord_Old in filename:
                FileName_New = filename.replace(KeyWord_Old, KeyWord_New)
                os.rename(filename, FileName_New)


def main():
    while True:
        print("{0} {1} {0}".format('*' * 20, "欢迎使用"))
        print("1.添加或删除文件前缀")
        print("2.添加或删除文件后缀")
        print("3.添加或删除文件名")
        print("4.修改文件扩展名")
        print("5.当前目录文件列表")
        print("6.退出")
        print("*" * 50)
        while True:
            try:
                type_root = int(input("请输入编号："))
                if type_root in range(1, 7):
                    break
            except:
                pass
        if 6 == type_root:
            break
        while True:
            cur_dir = "{}".format(input('请输入路径：'))
            if os.path.isdir(cur_dir):
                break
        if 1 == type_root:
            while True:
                print("1.添加文件前缀")
                print("2.删除文件前缀")
                print("3.退出")
                while True:
                    try:
                        type_id = int(input("请输入编号："))
                        if type_id in range(1, 4):
                            break
                    except:
                        pass
                if 1 == type_id:
                    add_pre_mark(cur_dir)
                if 2 == type_id:
                    del_pre_mark(cur_dir)
                if 3 == type_id:
                    break
        if 2 == type_root:
            while True:
                print("1.添加文件后缀")
                print("2.删除文件后缀")
                print("3.退出")
                while True:
                    try:
                        type_id = int(input("请输入编号："))
                        if type_id in range(1, 4):
                            break
                    except:
                        pass
                if 1 == type_id:
                    add_post_mark(cur_dir)
                if 2 == type_id:
                    del_post_mark(cur_dir)
                if 3 == type_id:
                    break
        if 3 == type_root:
            while True:
                print("1.修改文件名")
                print("2.删除文件名")
                print("3.退出")
                while True:
                    try:
                        type_id = int(input("请输入编号："))
                        if type_id in range(1, 4):
                            break
                    except:
                        pass
                if 1 == type_id:
                    KeyWord_Old = "{}".format(input("请输入需要被替换的字段："))
                    KeyWord_New = "{}".format(input("请输入替换的字段："))
                    rename_file(cur_dir, KeyWord_Old, KeyWord_New)
                if 2 == type_id:
                    KeyWord_Old = "{}".format(input("请输入需要被替换的字段："))
                    rename_file(cur_dir, KeyWord_Old)
                if 3 == type_id:
                    break
        if 4 == type_root:
            rename_file_exten(cur_dir)
        if 5 == type_root:
            display_file(cur_dir)
    print("欢迎使用！！！！")


if __name__ == "__main__":
    main()

#	renamefile(cur_dir)
#	rename_file("C:\\Users\\xiahuan\\Desktop\\111",'经研所')
#	add_pre_mark("C:\\Users\\xiahuan\\Desktop\\111")
#	del_pre_mark("C:\\Users\\xiahuan\\Desktop\\111")
#	add_post_mark("C:\\Users\\xiahuan\\Desktop\\111")
#	del_post_mark("C:\\Users\\xiahuan\\Desktop\\python\\党建工作\\2014\\支委会记录")
#	rename_file_exten("C:\\Users\\xiahuan\\Desktop\\111\\党课")
#display_file("C:\\Users\\xiahuan\\Desktop\\党建工作",1)
