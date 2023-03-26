from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import CommandArg
from pathlib import Path

__zx_plugin_name__="摩斯密码"

cd=Path(__file__).parent
dict_path=str(cd/'morse_dict.txt')

morse=on_command("摩斯", aliases={"莫斯", "摩尔斯", "morse"}, priority=5, block=True)

@morse.handle()
async def _(arg: Message=CommandArg()):
    args=arg.extract_plain_text().strip().split()
    text=' '.join(args[1:])
    if text=='':
        await morse.finish("请输入内容并且记得空格！", at_sender=True)
    try:
        if args[0]=='加密':
            await morse.finish(f"原文：{text}\n\n密文：{text_encode(text)}", at_sender=True)
        elif args[0]=='解密':
            await morse.finish(f"密文：{text}\n\n原文：{text_decode(text)}", at_sender=True)
        elif args[0]=='更新':
            reload()
            await morse.finish("更新完成！", at_sender=True)
    except KeyError:
        await morse.finish("加解密出错！密文错误或未收录！", at_sender=True)

acdict={}
cadict={}
def reload():
    global acdict
    global cadict
    global dict_path
    acdict={}
    cadict={}
    for line in open(dict_path).readlines():
        alpha, code=line.split()
        acdict[alpha]=code
        cadict[code]=alpha
reload()

def word_encode(word):
    encoded=[]
    for a in list(word):
        encoded.append(acdict[a])
    return '/'.join(encoded)

def text_encode(text):
    encoded=[]
    for word in text.upper().split():
        encoded.append(word_encode(word))
    return ' '.join(encoded)

def word_decode(encoded):
    word=''
    for c in encoded.split('/'):
        if c=='':
            continue
        word+=cadict[c]
    return word

def correct_bracket(text):
    result=''
    bracket_count=0
    for c in text:
        if c!='(':
            result+=c
            continue
        bracket_count+=1
        if bracket_count%2==0:
            result+=')'
        else:
            result+='('
    return result

def text_decode(encoded):
    text=[]
    for e in encoded.split():
        text.append(word_decode(e))
    return correct_bracket(' '.join(text))

