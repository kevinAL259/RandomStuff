import ftplib
import threading
import signal

terminate_threads = False

def User_Login(ip, User, password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(User, password)
        ftp.quit()
        print('user: {}:{}'.format(User, password))

        terminate_threads = True
    except ftplib.all_errors as e:
        if terminate_threads:
            return
        pass

def iniciar_sesiones_concurrentes():
    ## Not finished