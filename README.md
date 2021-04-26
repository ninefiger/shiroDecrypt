# shiroDecrypt
> “值守”前开会被问了一个问题，遇到shiro反序列化告警怎么确定是攻击，有几个老哥说直接base64解密看一下就行，我可能不太相信。。。

​		使用常用key解密rememberMe的payload，解密内容中会有部分dnslog、ysoserial等字样，正常数据可能是类似于用户身份信息的可识别内容。

```bash
python3 shiroAesTools.py -d "rememberMe内容"
```

<img src="https://raw.githubusercontent.com/ninefighter/shiroDecrypt/master/example.png">









