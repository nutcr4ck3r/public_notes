from os.path import isfile
from os import remove
from requests import get
import json


def output_2_file(fileName):
    with open(fileName, mode='a') as w:
        print('No. %s' % i, file=w)
        print('Zip code: %s' % x['zipcode'], file=w)
        print('Address: %s%s%s' % (x['address1'], x['address2'], x['address3']), file=w)
        print('Ruby: %s%s%s' % (x['kana1'], x['kana2'], x['kana3']), file=w)


baseUrl = 'https://zipcloud.ibsnet.co.jp/api/search'
zipCode = input('Please input ZIP code for search: ')
limitNo = 20
parData = {'zipcode' : zipCode, 'limit' : limitNo}
resFile = 'result.txt'

response = get(baseUrl, params=parData)

jsons = json.loads(response.text)

print('Response status: %s' % jsons['status'])

if jsons['status'] != 200:
    print('[!] Error has occured!')
    print('[!] %s' % jsons['message'])
elif jsons['message'] == None:
    print('[!] ZIP code is not found!')
else:
    if isfile(resFile):
        remove(resFile)
    
    i = 1
    for x in jsons['results']:
        print('No. %s' % i)
        print('Zip code: %s' % x['zipcode'])
        print('Address: %s%s%s' % (x['address1'], x['address2'], x['address3']))
        print('Ruby: %s%s%s' % (x['kana1'], x['kana2'], x['kana3']))
        output_2_file(resFile)
        i += 1