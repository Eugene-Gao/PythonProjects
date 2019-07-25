#coding = utf-8
import json

def resolveJson(path):
    file = open(path, "rb")
    fileJson = json.load(file)
    print(type(fileJson))

    for key, value in fileJson.items():
        print(key, value)

    print(fileJson["url"])


    '''
    return (field, futures, type, name, time)
    '''

def output():
    result = resolveJson(path)
    '''
    print(result)
    for x in result:
        for y in x:
            print(y)
    '''


path = r"D:\Work\Project\PythonProjects\BaseMethods\jsonFile.json"
output()