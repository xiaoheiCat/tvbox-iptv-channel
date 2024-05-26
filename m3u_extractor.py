import requests

response = requests.get('https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u')

lines = response.text.split('\n')

with open('tv-channels.txt', 'w') as f:
    f.write("xiaoheicat's Channel,#genre#")
    for line in lines:
        if line.startswith('#EXTINF'):
            name = line.split(',')[1]
            next_line = lines[lines.index(line) + 1]
            url = next_line.strip()
            f.write(f'\n{name}:{url}')
