import paramiko
from conf import config

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def read_test_log():
    ssh.connect(config.test_server_ip,username = config.test_server_username,password=config.test_server_password)
    #关闭MQ
    cmd = 'cat '+config.test_temp_log
    stdin,stdout,stderr = ssh.exec_command(cmd)
    return stdout.read()


if __name__ == '__main__':
    read_test_log()