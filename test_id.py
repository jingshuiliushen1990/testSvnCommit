import hashlib
import json


def id_iterator(prefix: str):
    for i in range(1000):
        yield prefix + f'{i:03}X'
        for j in range(20):
            yield prefix + f'{i:03}{j:01}'


def test_id(id: str, idSha: str):
    for i in id_iterator(id[0:14]):
        if (hashlib.sha256(i.encode('utf-8')).hexdigest() ==  idSha):
            return i


with open('settlePersonJson') as f:
    data = json.load(f)
    for m in data['rows'][0:10]:
        print(test_id(m['idCard'], m['idCardSHA']))