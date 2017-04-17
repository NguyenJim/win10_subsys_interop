#!/usr/bin/env python3
'''
Author:     Jimmy Nguyen
Description:    Generate a directory of linux commands to allow
                CMD to "pretend" to be linux.
                Really, what is happening is I'm taking advantage of
                the 'bash -c' command and omitting it via putting
                the commands in various .bat files.

Ver: 0.1
'''

import os
import struct
import re
import subprocess as sp

def main():
    # create the directory if not already made 
    new_dir = r'C:\bash_commands'
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        print(new_dir + "\ already exists")
    # cd to directory
    os.chdir(new_dir)
  
    # creat .bat files of linux commands to be "imported"
    cmds = '''
    ls mv rm cp clear
    whois ssh
    sl vim 
           '''
    cmds = re.findall(r'\w+', cmds) # parse data into list

    #generate .bat files
    for cmd in cmds:
        outfile = open(cmd + '.bat', 'w')
        outfile.write("@bash -c '" + cmd + " %*'")
        outfile.close()

    
    # TODO: Find out why PATH won't update
    # # modify system path to enable command execution anywhere
    # path = sp.check_output(['path'], shell=True)
    # path = str(path, 'utf-8')
    # new_path = r'C:\bash_commands'
    # if new_path not in path.split(';'):
    #     path = path.strip()
    #     path += ';' + new_path
    #     sp.call('path ' + path, shell=True)
    #     print(new_path + ' appended to PATH')
    # else:
    #     print(new_path + ' already in PATH')
    

main()
