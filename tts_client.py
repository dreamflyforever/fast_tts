# -*- coding:utf-8 -*-

import sys
import websocket
import time
count = 0
ws = websocket.WebSocket()
ws.connect("ws://0.0.0.0:8766", max_size = 10752000)

'''
content_file= open("/home/jim/workspace/aiengine/tts-tools/batch_tts/content.txt")
lines = content_file.readlines()
for line in lines:
    filename = f'{count}.wav'
    print(filename)
    print(line)
    ws.send(line)
    with open(filename, 'wb') as f:
        while (True):
            audio = ws.recv_frame()
            if len(audio.data) == 2 and audio.data == b'\x03\xe8':
                print('exit')
                break
            print(type(audio.data), len(audio.data))
            #print(audio.data)
            print('-------------------------------')
            f.write(audio.data)
    count = count + 1
ws.close()
'''

ws.send('对不起啦！我这就闭嘴哦！什么时候让我张嘴跟我说声呀！')
filename = 'test.wav'
with open(filename, 'wb') as f:
    while (True):
        audio = ws.recv_frame()
        if len(audio.data) == 2 and audio.data == b'\x03\xe8':
            print('exit')
            break
        print(type(audio.data), len(audio.data))
        #print(audio.data)
        print('-------------------------------')
        f.write(audio.data)
ws.close()
