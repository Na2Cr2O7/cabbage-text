with open('index.html', 'r',encoding='utf8') as f:
    html = f.read()

import base64
import os
from PIL import Image
def resize(fileName):
    img = Image.open(fileName)
    img.resize((200,200))
    img.save('temp.png')

html0=html
def convertImageToBase64(fileName):
    with open(fileName, 'rb') as f:
        return base64.b64encode(f.read())
    
left=html.find('id: "')
while left>0:
    right=html.find('",',left+4)
    fileName=html[left+5:right]
    print(fileName)
    if os.path.exists(f'./image/{fileName}.png'):
        resize(f'./image/{fileName}.png')
        base64_=convertImageToBase64(f'./temp.png').decode('utf8')

        html0=html0.replace(fileName,f'data:image/png;base64,{base64_}')
    html=html[left+5+len(fileName):]
    
    left=html.find('id: "')
with open('indexSingle.html', 'w', encoding='utf8') as f:
    f.write(html0)
