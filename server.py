from waitress import serve
import argparse, sys
import os
import signal
import subprocess

parser=argparse.ArgumentParser()
parser.add_argument('--service', help='Enter service to start / stop')
args=parser.parse_args()
sys.path.insert(0,'.')

def killPort(portnumber):
    command = "netstat -ano | findstr "+portnumber
    c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = c.communicate()
    pid = int(stdout.decode().strip().split(' ')[-1])
    os.kill(pid, signal.SIGTERM)

if __name__ == '__main__':
    from gatewayapp.wsgi import application
    if(args.sub == 'dev'):
        if (args.service == 'stop'):
            killPort("8001")
        else:
            serve(application, port='8080')

