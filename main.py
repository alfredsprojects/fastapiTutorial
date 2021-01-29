from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I am awesome"}


async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    burgers = number
    return burgers

@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    
    return burgers