from aip import AipOcr

BAIDU_APP_ID='14490756'
BAIDU_API_KEY = 'Z7ZhXtleolXMRYYGZ59CGvRl'
BAIDU_SECRET_KEY = 'zbHgDUGmRnBfn6XOBmpS5fnr9yKer8C6'

client=  AipOcr(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
options = {}
options["recognize_granularity"] = "big"
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["vertexes_location"] = "true"
options["probability"] = "true"

def getimagestream(path):
    with open(path, 'rb') as f:
        return f.read()

def getcharactor(path):
    obj = client.general(getimagestream(path))
    if obj.get('error_code'):
        return obj
    res = []
    for r in obj['words_result']:
        res.append(r['words'])
    return res



if __name__ == '__main__':
    r = getcharactor('5.png')
    print(r)