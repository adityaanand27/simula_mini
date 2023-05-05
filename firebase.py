import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import time
import asyncio
from async_firebase import AsyncFirebaseClient

cred = credentials.Certificate('firebaseJSON.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://miniprojectdatabase-12f1b-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

async def send_data(data):
    ref.update({
        'Car_Count_Simulation': data,
    })
    print('hello')

async def aw(data):
    await send_data(data)
    
    