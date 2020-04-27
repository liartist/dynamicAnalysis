# extract API sequence

import os
import json
import time
from json.decoder import JSONDecodeError

ALL_REPORTS_DIR = 'reports/'
RESULT_DIR = 'sequence/'

print('API sequence extraction')
print()

for reportNum in os.listdir(ALL_REPORTS_DIR): # 1 2 3 ....
    reportFile = ALL_REPORTS_DIR + reportNum
    print(reportFile)
    APISequence = {}

    if os.path.isfile(reportFile):
        if os.stat(reportFile).st_size > 2000000000:
            print('\t[ERROR] file size over 2.0 GB')
            print()
            continue

        with open(reportFile, 'rb') as f:
            try:
                jsonData = json.load(f)

            except JSONDecodeError:
                print('\t[ERROR] json decode')
                print()
                continue

            try:
                for process in jsonData['behavior']['processes']:
                    for call in process['calls']:
                        api = call['api']
                        time = call['time']

                        if time not in APISequence.keys():
                            APISequence[time] = []
                        
                        APISequence[time].append(api)
            
            except KeyError:
                print('\t[ERROR] processes-calls not found')
                print()
                continue
            
    if not os.path.isdir(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    
    resultFile = RESULT_DIR + reportNum
    resultFile = resultFile.replace('json', 'txt')
    
    if bool(APISequence):
        with open(resultFile, 'w') as f:
            for time, apis in APISequence.items():
                for api in apis:
                    f.write(str(api) + '\n')
    else:
        print('\t[ERROR] API calls not found')
        print()

print()
print('API sequence extracted')
