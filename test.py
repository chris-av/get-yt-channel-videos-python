import requests
import pprint
import dateutil.parser
import time
import json
from main import getYouTube

# import your key key (or create variable in this file)
from secret import KEY

# some test channels
hoodvlogs = 'TheHoodRussian'    # one of my favorite channels, has relatively few videos (good for a quick test)
wshh = 'WorldStarHipHopTV'      # this channel has a large amount of videos, proceed with caution if you want to render output!

data = getYouTube(hoodvlogs, KEY, output=True)
