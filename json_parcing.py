import json

string_to_format = '''
{
  "messages": [
    {
      "message": "This is the first message",
      "timestamp": "2021-06-04 16:40:53"
    },
    {
      "message": "And this is a second message",
      "timestamp": "2021-06-04 16:41:01"
    }
  ]
}
'''

json_obj = json.loads(string_to_format)

catch_json = json_obj["messages"]

print(catch_json[1])
