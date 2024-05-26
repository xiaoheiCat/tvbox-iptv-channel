import urllib.request

def parse_m3u(m3u_content):
    # 分割字符串获取每一行
    lines = m3u_content.split('\n')
    # 初始化播放列表数组
    playlists = []
    # 遍历每一行来解析
    for line in lines:
        # 如果这行是以#EXTINF开始，说明它会包含一个频道信息
        if line.startswith('#EXTINF:'):
            # 获取逗号分割的信息，通常第一部分是频道信息，第二部分是频道名称
            parts = line.split(',', 1)
            if len(parts) > 1:
                # 初始化频道信息字典
                channel_info = {'name': parts[1].strip()}
                # 将频道信息字典添加到播放列表数组中
                playlists.append(channel_info)
        # 如果这行不是以#开头，说明它可能是一个URL信息
        elif not line.startswith('#') and line.strip():
            # 如果播放列表数组不为空，给最后一个频道信息字典添加URL
            if playlists and 'name' in playlists[-1]:
                playlists[-1]['url'] = line.strip()
    return playlists

# 获取m3u文件内容
url = 'https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u'
response = urllib.request.urlopen(url)
m3u_content = response.read().decode('utf-8')

# 解析m3u内容
playlists = parse_m3u(m3u_content)

# 将解析后的内容写入文件
with open('tv-channels.txt', 'w') as f:
    f.write("xiaoheicat's Channel,#genre#")
    for item in playlists:
        f.write(f"\n{{{item['name']}}}:{{item.get('url', '')}}")
