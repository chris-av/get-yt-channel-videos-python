# GetYouTube

I wanted to simply get a list of every video published by a specific YouTube channel. 

## Instructions

You need only to import the `GetYouTube` function from the `main.py` file. This function can take any username or channel ID. However, you depending on how large the channel is, you may need an API key from YouTube / Google. 

Define your key in a `secret.py` file like so: 

```python
KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # replace string with actual key
```

The `test.py` file shows how to run the function.

## Notes

The optional `GetYouTube(...,output=True)` flag produces a JSON file (see `sample.json`) that contains all the information associated with a YouTube video, which includes vdieo ID, channel ID and published dates. Therefore, the resulting output can be potentially large depending on how many videos a YouTube channel has published.

I decided get preserve the original output to give the end user the ultimate decision as to whether to keep the output as is, or to modify it per their requirements.

The structure of this code is inspired by [this](https://youtu.be/IK5UUrPglTM) video. However, it appears that the methodology in the video is [necessary](https://stackoverflow.com/questions/26831919/get-all-playlist-ids-from-channel-id-youtube-api-v3) due to the nature of how YouTube structures its API. 