# zhenxun-plugin-morse
morse code encryption &amp; decryption  
真寻机器人的摩斯密码加解密插件

## 文件说明
- `morse/`  
插件文件夹，放到`plugins`目录中即可。
- `morse/__init__.py`  
插件主文件。
- `morse/morse_dict.txt`  
摩斯密码对应字典，一行一个，空格分割，可修改、补充。

## 使用方法
- 加密  
`摩斯加密 <明文>`
- 解密  
`摩斯解密 <密文>`

## 加解密规则  
空格不变；加密时以单词为基本，每个字符转换为对应的摩斯密码，以斜杠`/`分割；解密时反之。  
例：`'apple pie'` --加密-> `'.-/.--./.--./.-../. .--./../.'` --解密-> `'APPLE PIE'`
