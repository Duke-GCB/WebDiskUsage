##  WebDiskUsage - Application for parsing df output and displaying it in a web page
##  Copyright (C) 2015 Darren Boss <Darren.Boss@duke.edu>
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2 of the License, or
##   (at your option) any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
##
##   You should have received a copy of the GNU General Public License along
##   with this program; if not, write to the Free Software Foundation, Inc.,
##   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
