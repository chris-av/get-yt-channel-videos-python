import requests
import pprint
import dateutil.parser
import time
import json

pp = pprint.PrettyPrinter(indent=4)


def getYouTube(id, mykey, output=False):
  videos = []
  nextPageToken = ''


  # FIRST: query the channel and get the id for the uploads playlist
  baseURL = 'https://www.googleapis.com/youtube/v3/channels'
  responseCHANNEL = requests.get(baseURL, params={
    "part": "snippet,contentDetails,id",
    "forUsername": id,
    "key": mykey,
    "maxResults": 50
  })

  
  dataCHANNEL = responseCHANNEL.json()
  
  try:
    uploadsid = dataCHANNEL['items'][0]['contentDetails']['relatedPlaylists']['uploads']
  except:
    try: 
      responseCHANNEL = requests.get(baseURL, params={
        "part": "snippet,contentDetails,id",
        "id": id,
        "key": mykey,
        "maxResults": 50
      })

      uploadsid = dataCHANNEL['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    except:
      uploadsid = None
      print("user account not found! Please verify that you have the correct YouTube username or user id")
      return None


  
  # be kind to YouTube API, give the api a few seconds rest
  time.sleep(3)

  # SECOND: Now query the uploads playlist to get ALL the videos
  baseURL = 'https://www.googleapis.com/youtube/v3/playlistItems'
  response = requests.get(baseURL, params={
    "part": "snippet,contentDetails,id",
    "playlistId": uploadsid,
    "key": mykey,
    "maxResults": 50
  })

  
  if response.status_code == 200:
    print("channel {} found!, downloading videos now...".format(id))
    responseJSON = response.json()
    nextPageToken = dict(responseJSON).get('nextPageToken')
    if not nextPageToken:
      print("no next page token found!")

  
  for item in responseJSON['items']:
    videos.append(item)

  while nextPageToken:
    time.sleep(3)
    print("searching next page with token {}...".format(nextPageToken))
    response = requests.get(baseURL, params={
      "part": "snippet,contentDetails,id",
      "playlistId": uploadsid,
      "key": mykey,
      "maxResults": 50,
      "pageToken": nextPageToken
    })
    responseJSON = response.json()
    nextPageToken = dict(responseJSON).get('nextPageToken')
    for item in responseJSON['items']:
      videos.append(item)

  print("download complete!")

  if output:

    print("\n")
    print("writing output to file...")
    
    videos_dict = {}

    for i in videos:
      videos_dict[i['contentDetails']['videoId']] = i

    with open('output.json', 'w') as file:
      json.dump(videos_dict, file, indent=4)
      file.close()
    
    print("output complete!")
    print('')

  return videos

