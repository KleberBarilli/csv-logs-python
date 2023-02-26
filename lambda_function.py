import json
import urllib.request


def lambda_handler(event, context):
    res = urllib.request.urlopen(urllib.request.Request(
        url='https://swapi.dev/api/people/',
        headers={'Accept': 'application/json'},
        method='GET'))

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.loads(res.read())
    }
