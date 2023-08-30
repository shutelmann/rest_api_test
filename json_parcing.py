import json

string_to_format = '{"answer": "shutelmann"}'
json_obj = json.loads(string_to_format)

key = "answer"

if key in json_obj:
    print(json_obj[key])
else:
    print(f"Ключа с названием {key} не в JSON файле.")
