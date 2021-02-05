from fastapi import  FastAPI, Request
import uvicorn

app = FastAPI()

@app.get('/') #requests.get(f'{api_url}').json()
async def index():
    return {"message": "Hello World"} #{'message': 'Hello World'}

@app.get('/cal') #requests.get(f'{api_url}/cal?a=5&b=4').json()
async def cal_get(a: int = 0, b: int = 10):
    return {'result': a + b} #{'result': 9}

@app.post('/cal') #requests.post(f'{api_url}/cal', json={'a':5,'b':4}).json()
async def cal_post(request: Request):
    content = await request.json()
    a = content['a']
    b = content['b']
    return {'content': content, 'result': a + b} #{'content': {'a': 5, 'b': 4}, 'result': 9}

#uvicorn.run(app)