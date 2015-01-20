from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

def partition_usage(filesystem):
    df = subprocess.Popen(["df", filesystem], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    lines = output.split('\n')
    fs, size, used, available, percent, mountpoint = lines[1].split()
    #output_dict = dict(item.split() for item in output.split("\n"))
    #device, size, userid, available, percent, mountpoint = \
    #        output.split("\n")[1].split()
    #return output_dict
    return dict(name=fs, total=size, used=used, free=available, percent=percent)

@app.route('/')
def hello_world():
    usage = partition_usage('/media/itlab')
    print usage
    usage_list = []
    usage_list.append(usage)
    return render_template('usage.html', mounts=usage_list)

if __name__ == '__main__':
    app.debug = True
    app.run()
