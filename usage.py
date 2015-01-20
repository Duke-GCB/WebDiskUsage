from flask import Flask
import os
import subprocess

app = Flask(__name__)

def partition_usage(n):
    df = subprocess.Popen(["df", n], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    #device, size, userid, available, percent, mountpoint = \
    #        output.split("\n")[1].split()
    return output 

@app.route('/')
def hello_world():
    return partition_usage('/media/itlab')
    #return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
