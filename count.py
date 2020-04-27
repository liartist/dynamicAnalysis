# extract API count

import os
import json
import time
from json.decoder import JSONDecodeError

ALL_REPORTS_DIR = 'reports/'
RESULT_DIR = 'count/'

print('API count extraction')
print()

for reportNum in os.listdir(ALL_REPORTS_DIR): # 1 2 3 ....
    reportFile = ALL_REPORTS_DIR + reportNum
    print(reportFile)
    APICount = {}

    if os.path.isfile(reportFile):
        if os.stat(reportFile).st_size > 2000000000:
            print('\t[ERROR] file size over 2.0 GB')
            print()
            continue

        with open(reportFile, 'r') as f:
            try:
                jsonData = json.load(f)

            except JSONDecodeError:
                print('\t[ERROR] json decode')
                print()

            try:
                for APIList in jsonData['behavior']['apistats'].values():
                    for api, count in APIList.items():
                        if api not in APICount.keys():
                            APICount[api] = 0
                            
                        APICount[api] += count
            
            except KeyError:
                print('\t[ERROR] apistats not found')
                print()
                continue
            
    if not os.path.isdir(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    
    resultFile = RESULT_DIR + reportNum
    resultFile = resultFile.replace('json', 'csv')

    with open(resultFile, 'w') as f:
        for api, count in APICount.items():
            f.write(str(api) + ',' + str(count) + '\n')

print()
print('API count extracted')
