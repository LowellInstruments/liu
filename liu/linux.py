import os
import random
import subprocess as sp


def linux_app_write_pid_to_tmp(name):
    if not name.endswith('.pid'):
        name += '.pid'
    if not name.startswith('/tmp/'):
        name = '/tmp/' + name
    path = name
    pid = str(os.getpid())
    f = open(path, 'w')
    f.write(pid)
    f.close()


def linux_is_process_running(name) -> bool:
    cmd = 'ps -aux | grep {} | grep -v grep'.format(name)
    rv = sp.run(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    return rv.returncode == 0


if __name__ == '__main__':
    linux_app_write_pid_to_tmp('prova')
