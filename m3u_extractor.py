import requests
from m3u_parser import M3uParser

response = requests.get('https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u')
parser = M3uParser()
parser.parse_m3u(response.text)

with open('tv-channels.txt', 'w') as f:
  f.write("xiaoheicat's Channel,#genre#")
  for item in parser.playlists:
    f.write(f'\n{{{item.name}}}:{{item.url}}')
