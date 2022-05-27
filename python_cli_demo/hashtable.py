import json


global dic
dic = {}

def load(table):
    f = open(table, 'r', encoding="utf-8")
    dic1 = json.loads(f.read())
    dic.update(dic1)
    f.close()
    #print(dic)

def check(key):
    #print(dic)
    return dic.get(key)

def add(key, value):
    dic[key] = value
    js=json.dumps(dic, ensure_ascii=False)
    f = open(r'table.json', 'w+', encoding="utf-8")
    f.write(js)
    f.close()

def delete(key):
    dic.pop(key)


if __name__ == "__main__":
    load(r'table.json')
    add('你好', '1.wav')
    #add('好', '2.wav')
    #add('你', '3.wav')
    value = check('聊这么久，我都饿没电啦，要不要一起进店看看呀')
    print(value)
