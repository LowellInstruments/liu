import os
import random


def linux_app_write_pid_on_tmp(name):
    path = '/tmp/{}.pid'.format(name)
    pid = str(os.getpid())
    f = open(path, 'w')
    f.write(pid)
    f.close()


def get_fake_lat_n_lon():
    lat = random.random() * 20
    lon = random.random() * 20
    return int(lat), int(lon)


if __name__ == '__main__':
    linux_app_write_pid_on_tmp('prova')
