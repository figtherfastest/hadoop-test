import pyhdfs


def ope_hdfs():
    fs = pyhdfs.HdfsClient(hosts='192.168.137.128,50070', user_name='fightfastest1')
    print(fs.get_home_directory())


if __name__ == '__main__':
    ope_hdfs()
