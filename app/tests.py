from django.test import TestCase
import requests

# r = requests.get("http://127.0.0.1/Api/Jingcai/playerviewjingcai/player_default/",
#                  headers =  {'Content-Type': 'application/json','Authorization':
#                      'TOKEN eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6InBsYXllcl9kZWZhdWx0IiwiZXhwIjoxNTQ3OTUwMzM0LCJlbWFpbCI6InBsYXllckBwbGF5ZXIuY29tIiwib3JpZ19pYXQiOjE1NDc4NjM5MzQsImlzcyI6Imh0dHA6Ly9mYXNmZGFzLmJhaWN1In0.19RzqyBJ-SCmxCyn3adR5iYtXKckyWJYfSdhuyzF8Rs'},
# )
r = requests.post("http://127.0.0.1/Api/User/code/",
                  data = '{"A":"a"}',
                  headers =  {'Content-Type': 'application/json',
                              'Authorization':"TOKEN eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InRvcGFnZW50X2RlZmF1bHQiLCJleHAiOjE1NDc5NTM2MjIsImVtYWlsIjoidG9wYWdlbnRAdG9wYWdlbnQuY29tIiwib3JpZ19pYXQiOjE1NDc4NjcyMjIsImlzcyI6Imh0dHA6Ly9mYXNmZGFzLmJhaWN1In0.qKIJjS_PekMh1KYrXbpiccivu8SKM3mhPdC-WWcTU5E"
},
            )
print(r.text)
print(r.status_code)


