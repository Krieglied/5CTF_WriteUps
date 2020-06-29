"""
    Solution generated that will take the initial compressed file, and processed items
    until the text file is left
    
    Program used for the Inziption and Inziption-Bonus challenges
"""

import subprocess, os, hashlib, signal
count = 1
while True:
    arr = os.listdir()
    currentFile = ''
    for item in arr:
        if '.py' not in item:
            if '.txt' not in item:
                currentFile = item
    if currentFile is '':
        break
    fileType = currentFile.split('.')[2]
    oper = currentFile.split('.')[1]
    password = currentFile.split('.')[0]
    if oper is 'A':
        password = password
    elif oper is 'B':
        password = password[::-1]
    elif oper is 'C':
        password = hashlib.md5(password.encode()).hexdigest()
    elif oper is 'D':
        password = hashlib.sha1(password.encode()).hexdigest()
    else:
        password = '\'\''


    print('{} 7z e -t{} -p{} {}'.format(count, fileType, password, currentFile))
    cmd = ['7z', 'e', '-t{}'.format(fileType),'-p{}'.format(password), currentFile]
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    sp.wait()
    os.remove(currentFile)
    count += 1
