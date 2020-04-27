import os
import shutil

answerFile = 'a.csv'
sampleDir = 's/'

answer = {}

with open(answerFile, 'rb') as f:
    lines = f.readlines()
    
    for line in lines:
        name = line.split(',')[0]
        label = line.split(',')[1].rstrip('\r\n')
        answer[name] = label

os.mkdir(sampleDir + '1')
os.mkdir(sampleDir + '0')

samples = os.listdir(sampleDir)
for sample in samples:
    samplePath = sampleDir + sample
    if sample in answer.keys():
        if answer[sample] == '1':
            shutil.move(samplePath, '1/' + sample)
        elif answer[sample] == '0':
            shutil.move(samplePath, '0/' + sample)
        else:
            print('Wrong label')

print('Job finished')
