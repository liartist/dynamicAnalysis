# extract all report.json files

import sys
import os
import shutil

ALL_REPORTS_DIR = '/home/ssl/.cuckoo/storage/analyses/'
SINGLE_REPORT_FILE = 'reports/report.json'
RESULT_DIR = 'reports/'

print('report.json mover')
print('this procedure will move (not copy) all report.json files.')
print()
ask = str(input('will you proceed? (y/n) '))
if ask != 'y':
    print('procedure canceled')
    sys.exit()

if not os.path.isdir(RESULT_DIR):
    os.mkdir(RESULT_DIR)

print('moving file')
print()

for reportNum in os.listdir(ALL_REPORTS_DIR): # 1 2 3 ....
    reportFile = ALL_REPORTS_DIR + reportNum + '/' + SINGLE_REPORT_FILE
    print(reportFile)

    if os.path.isfile(reportFile):
        destination = RESULT_DIR + str(reportNum) + '.json'
        shutil.move(reportFile, destination)

print()
print('report.json moved')
