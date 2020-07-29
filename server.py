from waitress import serve
import argparse, sys
import os
import signal
import subprocess


sys.path.insert(0,'.')


if __name__ == '__main__':
    from gatewayapp.wsgi import application
    serve(application, port='8080')

