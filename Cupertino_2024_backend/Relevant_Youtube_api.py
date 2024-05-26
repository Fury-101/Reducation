import requests
import re

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    video_links = [f"https://www.youtube.com/embed/{video_id}" for video_id in video_ids]
    if(len(video_links) == 0):
        return 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    return video_links[0]

'''
# Example usage
query = "Python tutorial"
video_links = list(set(search_youtube(query)))

for link in video_links:
    print(link)
'''