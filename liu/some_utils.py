import os


def linux_app_write_pid_on_tmp(name):
    path = '/tmp/{}.pid'.format(name)
    pid = str(os.getpid())
    f = open(path, 'w')
    f.write(pid)
    f.close()


if __name__ == '__main__':
    linux_app_write_pid_on_tmp('prova')
