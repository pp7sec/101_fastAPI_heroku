# 101_fastAPI_heroku

This is basic fastAPI code for upload to heroku

## Usage

```python
import requests

api_url = 'YOUR API URL'

#get json
requests.get(f'{api_url}').json()
>> {'message': 'Hello World'}

#query parameters
requests.get(f'{api_url}/cal?a=5&b=4').json()
>> {'result': 9}

#request body
requests.post(f'{api_url}/cal', json={'a':5,'b':4}).json()
>> {'content': {'a': 5, 'b': 4}, 'result': 9}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
