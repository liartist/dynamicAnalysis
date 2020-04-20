# extract API sequence

import os
import json
import time
from json.decoder import JSONDecodeError

ALL_REPORTS_DIR = 'report/'
SINGLE_REPORT_FILE = 'reports/report.json'
RESULT_DIR = 'sequence/'

print('API sequence extraction')
print()

for reportNum in os.listdir(ALL_REPORTS_DIR): # 1 2 3 ....
    reportFile = ALL_REPORTS_DIR + reportNum + '/' + SINGLE_REPORT_FILE
    print(reportFile)
    APISequence = {}

    if os.path.isfile(reportFile):
        with open(reportFile, 'rb') as f:
            try:
                jsonData = json.load(f)

            except JSONDecodeError:
                print('\t[ERROR] json decode')
                print()

            try:
                for process in jsonData['behavior']['processes']:
                    for call in process['calls']:
                        api = call['api']
                        time = call['time']

                        if time not in APISequence.keys():
                            APISequence[time] = []
                        
                        APISequence[time].append(api)
            
            except KeyError:
                print('[ERROR] processes-calls not found')
                print()
                continue
            
    if not os.path.isdir(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    
    resultFile = RESULT_DIR + reportNum + '.txt'
    
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