from multiprocessing import Process
import os


# print('Process %s start' % os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent process is %s' % (os.getpid(), os.getpid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(), pid))


def run_proc(name):
    print('Run new process %s  %s' % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process start')
    p.start()  # 进程启动
    p.join()  # 等待子进程结束后再继续往下运行  进程间的同步
    print('Child process end')
