import log_mokuai as l
#a=l.log()
import os
import sys
import time
def mulu():
    paths = sys.path
    cur_path=paths[1]#获取的是文件的根目录
    # 当前文件的父路径
    #cur_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    #cur_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    #print(cur_path )
    filename=cur_path+'/log'
    a=filename
    create_time1 = time.localtime(time.time())
    create_time = time.strftime("%Y-%m-%d", create_time1)
    log_mulu=create_time+'text.txt'
    isexist=os.path.exists(a)
    if not isexist:
        os.makedirs(a)
    else:
        pass
    os.chdir(a)#改变当前工作路径
                                         #print(os.getcwd())
    f=open(log_mulu,'a')
    if f:
      f.write("")
      #f.close()
    else:
       pass
    a=filename+'/'+log_mulu
   # print(os.getcwd())
    return ('%s'%a)
    #print((filename+'/'+'text.txt'))
if __name__ == '__main__':
    print(mulu())
#os.mkdir(a)
#os.path.join(filename,a)
#os.mkdir(filename)
#print(filename)
#a.info(msg='我收神')
# import os　

