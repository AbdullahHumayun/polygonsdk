from typing import List

class Author:
    def __init__(self, data: dict):
        self.id = data['id']
        self.username = data['username']
        self.global_name = data.get('global_name')
        self.avatar = data['avatar']
        self.discriminator = data['discriminator']
        self.public_flags = data['public_flags']
        self.avatar_decoration = data['avatar_decoration']

class Attachment:
    def __init__(self, data: dict):
        self.id = data['id']
        self.filename = data['filename']
        self.content_type = data['content_type']
        self.size = data['size']
        self.url = data['url']
        self.proxy_url = data['proxy_url']
        self.width = data['width']
        self.height = data['height']

class Embed:
    def __init__(self, data: dict):
        self.type = data['type']
        self.url = data['url']
        self.provider = data['provider']
        self.thumbnail = data['thumbnail']
        self.video = data['video']

class Message:
    def __init__(self, messages: dict):
        self.id = [i['id'] for i in messages]
        self.type = [i['type'] for i in messages]
        self.content = [i['content'] if i['content'] is not None else "N/A" for i in messages]
        self.channel = [i['channel_id'] if i['channel_id'] is not None else "N/A" for i in messages]
        self.author = [i['author'] if i['author'] is not None else "N/A" for i in messages]
        self.authorid = [i['id'] if i['id'] is not None else "N/A" for i in self.author]
        self.username = [i['username'] if i['username'] is not None else "N/A" for i in self.author]
        self.embeds = [i['embeds'] for i in messages]
        
        self.fields = [i[0]['fields'] for i in self.embeds]
        self.field_name = [i[0]['name'] for i in self.fields]
        self.field_value = [i[0]['value'] for i in self.fields]
        self.mentions = [i['mentions'] if i['mentions'] is not None else "N/A" for i in messages]
        self.pinned = [i['pinned'] if i['pinned'] is not None else "N/A" for i in messages]
        self.timestamp = [i['timestamp'] if i['timestamp'] is not None else "N/A" for i in messages]

        