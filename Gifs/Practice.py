import os
from googleapiclient.discovery import build

pass_key = 'AIzaSyDh1JOuFCe19hrcIj1KVjo2aeGhGrGQngA'
youtube = build('youtube', 'v3', developerKey=pass_key)

request  = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()
print(response)