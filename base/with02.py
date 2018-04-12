# -*- coding:utf-8 -*-


# try:
#     f = open('C:/Users/tinker/Desktop/123.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


with open('C:/Users/tinker/Desktop/123.txt', 'r') as f:  # open最后的r是utf-8编码
    # rb是二进制文件，比如图片视频
    # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')读取gbk编码
    # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')忽略错误UnicodeDecodeError
    # print(f.read())
    for line in f.readlines():
        # print(line.strip('l'))
        print(line.strip())  # 把末尾的'/n'删掉
        #  read,readline(),readlines(),read(size)四种方法，readlines要去除空白行


with open('C:/Users/tinker/Desktop/123.txt', 'a') as f:
    f.write('\nhello')
# 'w'是写入，但是会覆盖，'a'相当于append，在文件后面继续写
