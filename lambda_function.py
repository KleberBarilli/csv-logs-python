import json
import urllib.request
from io import StringIO
import pandas as pd

def main():

    res = urllib.request.urlopen(urllib.request.Request(
        url='https://swapi.dev/api/people/',
        headers={'Accept': 'application/json'},
        method='GET'))
    res_json = json.loads(res.read().decode())

    df = pd.DataFrame(res_json['results'])

    df.to_csv('df.csv', index=False)

main()
