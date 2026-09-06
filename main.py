'''
Author       : Kaka
Date         : 2026-08-27 10:21:28
LastEditors  : Kaka
LastEditTime : 2026-09-03 19:02:43
Description  : 
'''

from fastapi import FastAPI
from fastapi.responses import FileResponse
from functools import lru_cache
import time
import asyncio
app = FastAPI()

@lru_cache(maxsize=1)
def lru_caches():
    time.sleep(10)
    return 'tttt'


@app.get('/')
async def index():
    name = lru_caches()
    return {f"你好{name}"}

@app.get('/{name}')
async def index(name):
    time.sleep(10)
    return {f"你好{name}"}


@app.get('/quick/{name}')
async def qucik(name):
    return {f"你好{name}"}