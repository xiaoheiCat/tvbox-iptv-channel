import requests

url_list = ["BurningC4","https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
           "joevess","https://raw.githubusercontent.com/joevess/IPTV/main/sources/iptv_sources.m3u8"]

url = []
name = []
response = []

for i in range(len(url_list)):
    if i % 2 == 0:
        name.append(url_list[i])
    else:
        url.append(url_list[i])

for i in url:
    response.append(requests.get(i).text)

with open('tv-channels.txt', 'w') as f:
    for i in range(len(response)):
        lines = response[i].split('\n')
        # f.write("Channels by xiaoheicat,#genre#")
        f.write(f"\n{name[i]},#genre#")
        for line in lines:
            if line.startswith('#EXTINF'):
                cname = line.split(',')[1]
                next_line = lines[lines.index(line) + 1]
                curl = next_line.strip()
                f.write(f'\n{cname},{curl}')
