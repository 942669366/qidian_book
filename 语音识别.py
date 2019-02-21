from aip import AipSpeech
app_id = "15544234"
api_key = "GWjmFRoTNT3azlTXNblqAzM9"
secret_key = "XZXUb08jPAftrojw6cchEf518eeLkUQ9"
client = AipSpeech(app_id,api_key,secret_key)#将所需要的参数放入AipSpeech里面，形成一个对象
#第一个参数是文本信息，第二个参数是语音  #"zh"表示中文，引文为"en",1代表使用的平台为PC
texts = ["周夫拥"]
texts[0].replace("”","")
result = client.synthesis(texts,"zh",1,{
    "vol":5,#音量
    "spd":4,#语速
    "pit":9,#语调
    "per":4,# 0:女，1:男，3:逍遥音，4:小萝莉 等等

})
with open("auido5.mp3","wb") as f:
    f.write(result)