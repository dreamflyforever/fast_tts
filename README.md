# 最快tts音频响应解决方案
> 使用azure的tts作为缓存，hash表映射方式获取音频，终端响应时间20ms。

## tts的demo地址
```
https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/#overview
```

# 项目目的和声明
- 本项目的目是提供一种快速tts响应的方案，使用azure tts缓存到服务器，使用hash表方式实现o1时间复杂度的方式。
- 本项目仅用于学习交流禁止用于商业用途

### usage
开启服务器python tts_server.py  
使用客户端测试python tts_client.py

### license
NO MIT by Jim
