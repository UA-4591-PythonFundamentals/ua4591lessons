import json

data = '''
{
    "name": "Temperature Sensor",
    "15": 22.5,
    "20": 23.0
}'''
parsed_data = json.loads(data)
print(type(parsed_data))  # <class 'dict'>
print(parsed_data)
with open('lessons/lesson14/input.json') as f:
    file_data = json.load(f)
    print(file_data)

parsed_data['city'] = parsed_data['name'] + ' Location'
dumps = json.dumps(parsed_data, indent=4)
print(type(dumps))  # <class 'str'>
print(dumps)
with open('lessons/lesson14/output.json', 'w') as f:
    json.dump(parsed_data, f, indent=2)