from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import datetime


class UploadItem(BaseModel):
    animate: list
    mode: str

mode = '來回播放'
status = 0
animateList = []
t = datetime.datetime.now()



app = FastAPI(
    title='Embedded System project'
)

@app.get('/')
async def main():
    return "test ok"

@app.post('/upload')
async def upload(item: UploadItem):
    
    global mode, animateList, t, status
    
    mode = item.mode
    animateList = item.animate
    t = datetime.datetime.now()
    
    status = 200
    
    return {'status': 'success'}

@app.get('/check')
async def check():
    global status
    return status


@app.get('/appData')
async def appData():
    global mode, animateList, t, status
    status = 0
    return {'mode': mode, 'animate': animateList, 'date': str(t)[:10], 'time': str(t)[12:-7]}



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
