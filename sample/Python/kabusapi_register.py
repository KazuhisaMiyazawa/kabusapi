import urllib.request
import json
import pprint

obj = { 'Symbols':
        [ 
            {'Symbol': '9433', 'Exchange': 1},
            {'Symbol': '6501', 'Exchange': 1},
            {'Symbol': '6501', 'Exchange': 3}
        ] }
json_data = json.dumps(obj).encode('utf8')

url = 'http://localhost:18080/kabusapi/register'
req = urllib.request.Request(url, json_data, method='PUT')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'e629f7e6073b40488d0d134dae4e60ac')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
