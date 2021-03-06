import base64

def cc(input):
    arrayOfInt = [i for i in range(256)]
    i,j = 0,0
    while i<256:
        j = ( j + arrayOfInt[i] + input[i%len(input)] + 256) % 256

        temp = arrayOfInt[i]
        arrayOfInt[i] = arrayOfInt[j]
        arrayOfInt[j] = temp

        i += 1
    return arrayOfInt

def b(input,key):

    output = [0 for i in range(len(input))]
    b,c = 0, 0
    for i in range(len(input)):
        b = (b+1)%256

        c = (c + key[b])%256

        temp = key[b]
        key[b] = key[c]
        key[c] = temp

        #print(key)
        output[i] = key[(key[b] + key[c]) % 256] ^ input[i]
  
    return output

#input = 'tbspebytbakmOTc4YTM2NjM3ZDE5YjcyOGU3NTE1MDgxMjIxODc5'
#output = 'open_teamviewer'

def decode(input):
    kkey = [ord(i) for i in input[:12]]
    ens = bytes.fromhex(''.join(map(chr,base64.b64decode(input[12:]))))

    key = cc(kkey)
    output = b(ens,key)
    #print(output)
    print(''.join(map(chr,output)))


input = [
"biwqfdpxmjmhNWQxYw==",
"ocztviniusfwZTJlNg==",
"qovfawdxmwyvMWI3MQ==",
"qflalydmkrakMWVmMA==",
"plrwhhonatzhZjM2MQ==",
"fewvxyxgiwijNmE0Zg==",
"bulwqlgehmwfN2I1ZA==",
"dtnkpyingnmqOTJkYw==",
"wgdtmpimpgfrYTQ2MA==",
"mvioidqlhlbfODNkZQ==",
"mlsxxjwuzqvmNzM1ZQ==",
"wzabjwavceteZDQ4Zg==",
"wgiawamphayhN2EwNQ==",
"ydbeyjopkkmwZTk3OA==",
"lmadngjpwetzYzdjMg==",
"nrvzzbuotkoeNWQ1NA==",
"kqvyafbjrqvtNWFmYQ==",
"kkwxxkdnhkzbYTZjMw==",
"pmzddmlwftqtMTFlYQ==",
"cqshyljackoaZTY5NQ==",
"pdgqvgzfxrpnMzdlZg==",
"blxigajdqbvvYzNkMA==",
"eramjsqpyareZTczNA==",
"nnjkmocibtyoYmQ4OQ==",
"zqqtnzrixnuhYjUzNQ==",
"zibttsnesnwnYjkxZQ==",

"ggfxhwxuavhuMTM2ZTJiZWE2YTE1NmQ0MDFjNDFjZWFhY2Y2YTUzMzA2YjQyOTE5ODEwNDMwNzQ3OTQ0NzgxNjBjZjlhMDk=",
"kkzlwetvufwxZDQ1ZmYwOGI1NTI3MDJjYzgzZGQwODk3MTg5YmZhMDIyMjEyYjg4MThiMDg5MTdmNmFjN2Q1MTE5ZTcxYWI4OGViZDE=",
"xldzqebrakrgOTNkNzBhODhkNjkyMzJhZTExYTk2ZWEyZmFiYTk1ZTViY2UyMDNjYmFhMDc0ODliZTRlODcyOWI2OWIyM2JlNjMzMGNhNg==",
"aoavrpciqxwoZjkyMTlhNzY1ZDk2ZDdiNjBmNzc4ZWE2ZjI1NzBmZjYxMzQ4YTNhNmM0YmRhMDQzY2I0NTNkYjA5ZGZmMWE0M2NkZDQ3OGQwZGY4YTFi",
"aqulmefvgxziZGEyYmNmMDZjMDgxYzY1OTgzZGE2NzQzZDMyNzE2YjI5Mw==",
"pdrwmachckatMGEwZjg5MGJiNjE4NjI4ZjU3Y2Y5NDg2OWY=",
"ijyfygpsvhmfYmM0NDk1NzlmNWNkM2U0OTFi",

"fbmrcudeuwwzMDhiMg==",
"lrhpvcjljtojNDljMw==",
"wrebmwesooavNGIyNw==",
"haglfwanbyzhYWMzOQ==",
"beoigbxpbxxsMGRiNw==",
"jcwjpvuznjtbMDVmNTkzMGE3Ng==",
"onjhxgyoadaoYWE3MGM0YmY=",
"qkdnxromxnkcZmJjMWQ0NWQzZTBkYWI3YmI0MjE3MGMwOTY5ZWZm",
"ypfbmkppwifwYzJmNDIxYmU1NzE2NDk4MjFhMmM1YQ==",
"vrbllaqanncpOTc2OGNiYmM3ZmMwNzM3YjA4MjMzOGVhMzRiMmFjZGNlZA==",
"lbesojlktlouZmEzZDk0",
"kcbmthghurgxODM5YzY1MDcwMGYwNDE2ODUxZTFiOGIwMDdkZGM1NzU0OTIyMDI5ZDk4ZTAwZTMyNDAzNTUyZWQzNWJkYTI0Njk5MTAxNDg4ZDgwMjRl",
"gzuxmhnkomtoMzU4MWY2MDBjZWQ4YmNiZWVlYTE3MjcwNTFmOTEzOTdhOGUyYWZhNDBhMjFmM2M3NTU4Mzg2NDhiNTExOThiNjZjZTI1MA==",
"zkonehshofbcZDZiYjkzYTkzNDU0NWFjYWNkNTUzZTcwMTA4ODFkMGU4OTE5YmI1OTVhMWY0Y2ZkMDIzZTVlM2Y0Yjg2ZWNmMmVmNWZiMTBjYjMwNDBlOTFiOA==",
"nbhhfrcrhnccZjZkNTlkZWU5NmE3MmIzY2U4N2YwYmQ0NGY3ZGNlMzFhYTUxNjRmNDMzMWQyNmU2NjM2MWI3",
"gzuxmhnkomtoMzU4MWY2MDBjZWQ4YmNiZWVlYTE3MjcwNTFmOTEzOTdhOGUyYWZhNDBhMjFmM2M3NTU4Mzg2NDhiNTExOThiNjZjZTI1MA==",
"ektnaipmomnnMDU4ODg2OTZiZTZiY2I5MzM4NzAzNDhjOWMxNDhmOTZiMTU3NThhNjBiZWMwODg1OTI1MTMyNzU3YTRjYjFjMw==",
"vprbbnueaqwoZDI=",
"wcmhpupsvlrhMTg2ZGU2ZTlmMDdjODgzYzdjYzVkODczZGU3MmM5MjIwZTBmOTgxNjhiNzU4NDNjN2VkNzE5ZjM4M2IzZGVjY2VmYzQ3ZmZi",
"lkicxwfrjjpnOTk4MmE3Njc1NWVkNGNmNjAzNDhkYmU2NjZjYmVmMmZkMTU0MGUyMjE4OWYyMWMyZTA1YWQyZWVhNzU3ODJiNDBmZDVhYQ==",
"hcfqieosccjnNGY5N2Q5ZGUyZDExOTNiZGFiNDM3OTdmNjliYTBjMzdlODljZTNhYmNhMzNkMjZmODNmNjEyNTM0YWNmNmI=",
"zbrksbkrrpuhZTc2OTkzZGM2YTAzZDhmMGRiYmUwMzdhZWQ4YjYxZjNjMDAwODgyOTJjMGNkZTM4MGVlMWQxOWY0NGE4ZDFhOA==",
"rujhfooqunomODg3NTkxZWFjYmFiMGVlM2M0ZTZlNmVlNjE2MDFkNzE5MGJlZmQxODM3ZGUyNTlmMGNkNTRlYWRhZjNkNTljNQ==",
"ktxvfflzxqlbNWY5M2I5NDFiNDc3MTkzYWJiNTBmZWMyMjc5YWYyMjZhOGJkZWRlNWI4YjE1YmZmNTEzYTQxZGI1YTcwMjU=",
"imjviasalebrYmJmYjQyMjQ5YzFmMDQ2NGM0M2RmYTUzM2MzZjI5M2VhMWNmMDgyZTIzMTIzNTIzYTUxNTRiNDRmNzc1M2YxNjhjNTJlZmMyYjRhODM0NGU=",
"ovepgxybhybeYTU1NzgxM2EyNDk4MzQzODJhOTg5ZWIwN2E2ZWY1ZDA4ZjA4NmFkZDIxNGJiZmI2YjBiOTAwNGYwY2Y5YjY0NTk2MWFmYzliZGMwNDgx",
"ajqfyncnppcoYzcyNGRmZmYxMWRmYjMyZjYyOTQ1YzY0MWUyNjQ1ZTYwMzJiZDAyMzEwZTAzM2RlODc1OWNjZTIwMTljNDQ5NDA2OWZiZQ==",
"nkvpztpqndypMDgyNGM4YWFkMjc2MjYzMjk0ZDA5ZDAyNjliNmMxZWVjMDZlZjUwZTg4MGQzMTUyNDdiNDUxMDc1ZDhkYzhmOGMyMTVmNGFiN2EyMzAzNjk4MjNiMmU3ZjU3YzJhMw==",
"npafvfqphfanZTRhMGU0M2U1M2NkMzU5ZmY4MGY5YzZmN2U5OTMyZGEyMTc1YzE2ZGVkY2Q3OGRkZDNhZGM4ZTI4Nzk5YTZkY2Y1ZjU=",
"oxgqcpnnslsdZGEwNw==",
"fjimpnpcmjcnOGQ3Mw==",
"wbyprcpodlqxZTkzMA==",
"giwrupwjwianYzEwYg==",
"vlflgwnilbsjZmU5Yg==",
"agkkuchieicdYmYxMw==",
"yxylohohqpebZTYxMg==",
"pigcqqefxvvyZjlkYg==",
"liclbaznhoeeNTQxNw==",
"kgvygfmyzxlgNDIyZA==",
"qishvlmfxtthMmYwMw==",
"cicohgqawewiODJmYw==",
"lqijmumhjnmpMWFhOA==",
"igjetjtzjmnyMzVjNA==",
"odfxguxclgiiYTc3NA==",
"efcetbkmfwuiNDMwNA==",
"hxtzwkobypwoNWFmYg==",
"qenrkqsjzeptYzljYw==",
"trbrcuyphorrMDNmYw==",
"swbhtaiztjsaZGRkMA==",
"mcmmdnebsdlfODU0YQ==",
"xudzemevavoyZGY3ZQ==",
"lozkczadhbueNzExOQ==",
"ymmrneswqkhhZDRkYw==",
"qurgblyifugvMGFhYw==",
"sqjrerefeaxpYmY=",
"djukaaekqfioMWI2N2JiYTliMTZiMTQ5NzU4ZGNhYTc4MDg4NA==",
"abraqwmfmmiuMWU3MDFlNDY4NDAzOGYxOTdkZmMxZDI0ZDc3ZjRlMjc2OGFk",
"ebqnxxxagwniMzAyODM2YTdjNmJkNmJjMGNjNzhjODJhNDcwNGViODg=",
"kaipunszcrxuOWQ3NTEwNDNmOTU0NTlmNDdmNTE3YTAzZmQ1Mg==",
"mfdgjmwvurdvMzIzYzNmMTI4NjM1OTA3NWJlMWY5MGM3ZDRiMjdk",
"enklzevxbzuoYTg0ODNlZDBjYTVhZjUwYTZhNTY0ZjgxOTNiMDgxZDA3Ng==",
"zhsuhbnwsrsyOTljNWIyNmZhYWE2OWIzZDQzNzhhNzAxYmZiN2U1",
"hfmusqcznpnsYWI0ZmNiOTk2YmI4YWJmYjBiYmZkOGQ3OTcyZDFmZGM3NQ==",
"purndjyzaftsYTNjOTI4ZmRkMWQ5NWU3MmM0MTlhNjAxOTUwY2E3Y2Y4MmQ4NjM3MzVjYzc1Zg==",
"rtxbtpaefeqaZTdkZDIzODllNzdhMTExMWE1MjQzOTY2ZmViMTEzNWQxMmQzNjcwZg==",
"spegxwdrljqgNWE3YjViYWJmZGUwMzU4YTlmNmM1NzRmNjc2ZTYzZmFmNzY1",
"avbnvseswhfbY2JiMjA2MzAzODI0ZjBhYzI4ZGZjYjMzYzYyMGNkNDRkYQ==",
"sdfcbhamoffoZTJhNTg3ZjUyMTU2YTg4Yzc1NDI1Y2E4Y2Q2YjQ4YzU4MGY3YTk0OA==",
"wlwstpyloutiYWI4ZTQwNTIxNzhjYjcyZDM3Nzc2ZTdhZTEwYTNlMDg3MzliNTViYzU2MGUyMDZiMzFmMWQ3MGQ=",
"xmjqgslbdbvkODUwYTEyZTkyZGRlYzExZTMyY2EwNTQ5MmYzOA==",
"erruvrkzuethNjgwYWNlODc5ZTAwMmRhNTliOTRkMDhmYmFiMDZmZGEzNDM2",
"ulbxwtrwnaszZjIzMTcwNTM0YjgyZDFmMWM1YjNlYzJhZmE2Zjk3OWU=",
"bqzvhimowkqnZWE0Y2RiMWMyOGM4MzI2MzQ5OTQzZTBmZTI3MzQxZGJkM2Q0NzVlYmRmYTMxOGIwZTQ=",
"qzxdlazsymwtNjVkYThjMWI3MmE4OTUwZGM3ZTg2OTY0ZmQwNTYwOTQ0ODcyMTllNGFiOGU0OWZmYTg5MTYwMWU=",
"bnxkxsndeosbMmZmZGI2YTIxZGVlNDgyMDJmODVmYmMyOTQ4ZDY5NWVmOTcyZDk3NzljYTdmYjM1NGVmYzQy",
"aydyobpikxofZTE4ZDJjZGY5MzFmNGI3MGY0N2NmYTg2NjkyZTFhYzRmOGNkZTFkM2M5MWJhNmJkM2QwZGJiOGY2MTdiZjljM2E1MjZlNDZj",
"jlpqdxsvghhuODJiMzY3YzJlMmYxMWNkZDFhY2UzMzUzZGNjNWZjMDU0ZDQzODc=",
"trxfpueawwlnYjAwMzc2MGVmOTY3Y2RmMWFiODhjZjgyOTUyYmFmYjMzYQ==",
"fbczlysoviynYjVmZGI5OGVjNTg4NmRmODI5NDBiNWU3OTZiMGE1MWNmNmIy",
"peuclyujqpodNDVmYmMzNDRlYjY2MjZlMzMwYzRjZDhjMjVmZTRkNzYwOA==",
"ayncehsgumaoOTM1YzI3ZDk2ZDI2MDA3YjA5OTc0YmNjYmJjYzcwOGY=",
"byzdyokgoxnuYWY5NzFjMzNhZTlmYjUxNGM1Yzc1MjBhMzc1Mw==",
"xudenaebkrfkMDFhMGVkYzE1ODc0OGFjMDZjZmQyY2E5YTJhNA==",
"buhrfubunjfvYTNhYTZjMGY2NGYwMGYzNDcxNzZlMDM4ODdiZmFkMzU2YTI5",
"ytbdfvhqameqNzQ4MTYzMTk3NWE5NjA5YzY5YjdkMTJhZWEwYzMzZjQxZmVm",
"bxautkauhexaMjJlNjVkNGIzOTU1MGRmZDdmNDM3NjU1ZWYzYzI0ZGZlMTJj",
"spbldkeyngwsN2FkMTU4ZWI0ZDEyMzg1YmUxYTQ1ZDBkNzFmMTUyZGU=",
"rjliorlpqwecNjY2YWYzZWU2NDU4NmI5MjIxZDgzYjBhZTk0MGFhYjgzNTdhNzUxOGIxOWIzNDUwMWI1ZDY2MDk3ZTQxMGE1ZDAxOGFlMDVhMzhmMg==",
"hdicvsdfoxsiYWJmMWQ3M2I5ZTA1OThkN2UwOTM2YjJhODVlMzYyOTg1OWU2YzkyNWU5NWE3MA==",
"hbeivhdqkuxwN2VhMGVkZDQ4NGRiNWUxNjIzODk1ZTIzZTRmMjczNGJmYTZiZjI3NTY0Mzg3OQ==",
"gxwhphghitwnYjU=",
"sqjrerefeaxpYmY=",
"dmejyiaompqeYjVlMmVhYzZmY2IyNDNkYzdiZGMwYmZhOTMyNTZiOTYzYjVkZDg5MzlhMzM4MmVkNTBlODUxMWQzOWE4MWE1OTQzNDAzOGM1YWEyOTExODg=",
"wulqtrcyzjafNTQwY2U2NGI2MDA3YmIwNzUxOTE4MjhlYjgyMTA5MmU0MjY5MjIyYTcxNTkxNDBmZmYwZGQ2NzBkZTNjNDY0MTliZTFmYmEyNmI4MzJiOTNmNmU0OTExNWFlYjFhNjAwNjM1MmRlODNlYzZiNDg=",
"fsrvpzsvwbqlZTViNjY3OThmNjEwOGViZjJhNzgyN2IwMzk0ZjM0YzgwMDgwNjBhZTM0MzdmOWNmMzE2YjMzODc3ZmUxMTliOGY0ZDI2NDhjZGJiNzgy",
"pkfizadzixepOTc3YTY2MTM1MzBmNzJjNTQ5ZGVkNDdiY2Y1MDY1M2M4MDcxZTcwNDM5ZGM3MzhjY2M5ZjdlZDVhYTk5NmE3Y2U0NjZiOGY4ZjgwOA==",
"pvqpieikprsvODZjNDZmZGM2YmIxYTQwNDU5ODY1Y2ViZGZmYzBmMjUzNjJiZDhiNTRiYzYxNDBmNDA2ZTE1YzZhNWM3ZTBhNmMxMGEwN2U0ODM3ODE1NjZjNTJlN2NmMTE4MmM=",
"vnrsjigdxqzqMjU0NTQ3MmFjMGVlOWMwZjRjZjFjYzM4ZmYyMjAyMWFhZWE5NDU1MjkwYjhiNDc1ZDAxODM2MWNhZDY2N2RiMzY5NzJkOGRkMTE2ZjI4NWJlNg==",
"khbnmwtqhyjoZGY2ZTNlNTRmZTUwMzBkNTg5NmZjMDEzNDFlNmIyNjVmZjY3Y2UxYTEwY2U5ZmNmY2FmNmRlNjk1YTM5ZGRjNzBhOWQzZGYwMjI4ZTEzOGQ0Mzg3Y2Y2ZjExYmY3MzU4MjY=",
"lbpvisvxifzdZmY1MWIyZGRmMGM5MzViZjU4MzgwYjZmMWU4MjJmZGY4OWNjY2M1MTMwMTJmODZjNGFkYTQwYTI4N2ZiNjM4YzIxNmZkMDhiNjY5ZjNl",
"pufwbvrxfsycZWI2YjBlNWE5NmE0YTJhMTU4ZmM5NzlhYzRlZDZiN2VmYzBlMDI5NmU4OGNjMTJmZWFkYjhiYjg2ZDgxNDJkY2Q1OTIxZWIwNWI3ZjE2YTU2NmRkOTY3NmYyNzEwODQ4ZTMxZDg2ODJkY2ZmZjZiMTQxODMwYjg5YjNlNmExMWQ5NQ==",
"pgrlejdbrzklNjA0YWUwYjQ1ZjA1Mjk0M2E1MjRhYTkxMjRhNmUyMDU3M2VhMjgyNDgzMWMxMmRiZDEyMWM3NDA1ZTZlYjFiNzc1MTgwMmI1MjhjMzc1NGQxNGZiZDY4OThkMTEwZWMyMWEwOGJh",
"fbvkcwlijsdaMjcwOTQwNTA5ZmQ2ODgzN2VhN2YzMDVmNWFhZGYwNmNhOWVmYjRhOTgxYzE4OGRjMGY4NmIxZWNlYTI0MWNiNWQ2YjEyNTcwMDk2MzhhM2YzM2I5Y2E=",
"lumhwoweytpgN2RhN2ZkMTU2ZjUxOTc1ZmI3ZmE4ODE5YWJkY2ZiM2I4YjA5OTRkNDU1ZGZiZGZhMDRjYTRlNzVhMTAyYWM0ZWU5ZDhiNzRhMTQxMTIxNjMyMTliMzA4Yw==",
"vwtmmvwiaxjrNjY2NjViMjZjMGE0NGE1Njk5ZTUxYTA1MzMxOWNmY2JlZWUxNmM5NDA0NDBhNmRiZGY3OGYxNTMyZWU4ODlhNGIxOWRjZGNlMDY1MDdlZWY3ZjQ1MmNmMWEzZDU0Y2FiMTQyNWI0OGE0MGZlYWNiMWZmZTZiN2JiY2ZhYjM3ZTMyODhkNDVjZjQyZTRjYzk0ZmQ0YzY3YWFhMzE5YmU=",
"gwvrcrexhrdrNjAxNDdmNWMwZDdmMTlkNTVkNTAwODVkNGE0YzZlODY4ZDQ0ZGU1ZTc1Y2UxNTMxOWY5YWE4Yzc1OWFmMjQ4N2MyZWIwZTZlOTMwZWM2MzI1NGNmZWIwYjk1MDMzZDgwNjAwZjhlZmJjZmU2MjU5YjdkZjU3NTdkNGEyZjY4ZDI2Nzhj",
"bvixcfhuswtyZTU2OTRkNjViMjdhZWI5OTFkN2M4ZGEzNWJiN2U5MGJhZDQxNDI3ZDIyMDk2MWMwNDAwZGFhYzgwNGYwOTYxZGRjOWFkNjM0MDVhODY3MDA=",
"svcqizbtshvyNmZkODcxMGFlNzYyNzQyZmFhOGM2OGQwN2M5YTg3OWEzMDVkYTIzMTIyOTlmMTI4NzI0YzVmOTMxNDk0YzFlNTc4M2NhMTg3ZmI4OTJhNmQ=",
"lokjhcqiwnmbYjkxNjUzNzU0MjRmZDRmMDY5OTkyNGVkOTZiNDI4OTMzMTI5ODJlZmYwNzRkYzIxZTY2NmZhZjU1Yzg1ODBhZGZkNDE4NTQxMDZhODc4ZjRiZjVkNTM=",
"krsnvdgiqomnMzJlZWQwMDE3YmNiM2YyOGI5Y2JhOGI0OThkZjkyNjUxYTdlZDQzNTIwNWZiZDlhOGJiZDFkMDAxMzYyYWE0ZDIyNDFiY2JhZGFiZGFlNjIyNWRlOTdjOQ==",
"diuczudqyccxZGIyNDhmNWFjZjVjYmJiNzhhOTdmMTUwYjVmODZiNGYzOGQyODg1NDIxNzgwMzFhZmZmZGIyODhkNTZlZmE2ZTBjMmZlNWUzNDk1Mjk3ZDRkYTVjMjVhMjU5YjRjY2I0ODhiYTYxMjJmYzc2ODQxZDU1YzlhMmVjMDZmNjc4YzFiN2ViM2RkNzU1YmZjOGNlNzk2Y2ZkMzkxODJhZmRmYg==",
"cmtbcnhdjsblMWE0ZTdhMTE1ZTQyMDMwYjg1NGFiNGQ2MDU3ZjhiNjU4MTMwNjE3Yzc1YTRiNjRiOGNkZGU0NDA1OTNmNGE2MzAwODdiMzMxZjBmMTJhODA0MzI2NTYwZDYwMzkxMTg2ZDYyNWVhNGU5ZjFhMmM0ZWU3ZDUwMmZl",
"gjxcdwfamnjuNjdjYWFmMWYxYmY5OTgwNTkyNmZhYzJhZTljMWM0YzUyOTkyZWQyNDNmNTE2YzAwZTYxYjIwMjhlM2IwMjEyMWI5MzY2YTEzZGVlMTlkNTgwODNmZDYyY2YzYjkwZmIwOTI5NDdmZjg3YmI5ZTNiZDMxZDNkMTMyNGQyNTZkYjE0NDM1NWEyNDc0NTFiZjA3M2Q1M2Q5NTM0MDhlNDNlNmE1MzkxY2UwNTQ4MmIwZWNjZDZiNDk2YzI5YWM=",
"pewkxxipsboqMDMyMTI5Mjg3MDMzZGFjYzE3Njc4N2U5NTFiMmU3YmUzYmRiYjIyM2NmZjY5ZTAwOTA2NzAxOGIwMjcyNDczNTY2ZTFhMDBiNWZjZGYwZGIwNDgzNjY2M2QzZGQ2MmQ0NmI4N2NjYzE2Mzg3Mjg1MQ==",
"zsavalmipbbqMWQwMzU1Y2E3ZjQ0ODI0M2VkYjE0MzYxYzc0M2UwZGUxYjBiMjUwM2QyNjk2Y2ZhZWFiZWFlZDg1MWE5YWYxNWZiYTcxM2ZmZjJiYjc2ZDEzM2QwMWNkNjYxMGZkMjVkMGY=",
"jonrlsoxqmjfNzNkYjQ2OWMxZTBlMmFmNzZiMDg3NTZkNDFiZmViN2EzMjgwZGZiYTU4ZWE0ZjU4YmE1ZTI4YzQ1MzU0NmRlYzk0ZWUzZDY4ZGIzNzdiMDUyN2Y0ZjY4YjA2Y2M4Y2Q2MDA5MzU0MjA1OTY0YzdjNDhm",
"trefwoshejggMjVmYTI2NTM1NjFkMDkwOWUyMzhhYjc5OTc5OTNhYjFlZTRmYTZiM2JhMTIxZDg1NGM0ZTQ3N2FjYTJjYWQyZWFlODQzZGM5Mzg5YmM1ZWE5MzQ3ZDdlNzRmNDlkMWVmMzRlOGJmYWI0ZA==",
"kvgpilltxeenNjkyOTk2NzBlOTgxMzg0MjRkZDBmMTZjZjUwOTVlMzhjN2RkOWJjMDE0NzM5YWI3MDMzNjIyYjk4M2I3MTE1NWRmMjIzYzUxMGRhOWZjYjY5Yjk5YjE=",
"hkkckiqakgwrNWQ2Y2JkZmFhNzdjZTE3NGZjOGE3OWRmYzllY2JhYjVhYzU1ZTI2YTVjMDdkOWMzZmU2NzJiM2JjOWQwYjZjNzZjNDE4ZGIyNTMxMzQ1Mzg=",
"dcpflkidauqeMzg0NDk1YmQwNTE4OTUxNDNlZDgyYjdmZDEwZjFlNWI2YTVhMzY4ZDYyNWUyMWVjYmVjOTQ0Y2Q5MDk3M2MzMjM4YWExZThlNTNjMTU4Yjg1MDZjNjhlMmY5NGE1ZTBjMDk2NQ==",
"clktsqbfpekdZDk1NTkwNTlhMjliMGEwY2MyYmI5N2U3MjQ2YzYzNjRmNDVmZmY1ZGI1ZWZmMGU5NWJkZGQ0MmE3NTE1NGJmN2ZiMGYzNTM0N2Q3MmI0YmFiYzZmM2NlMmExZmRhNzcxMGU3OGFlOWE4M2JkZGU5ZjdmMDJkNzE1MzM4MQ==",
"zgctlyzvkbgfZDJmNWE4YzkwNjI2MTM2YmRiMWY2OGI2NDUyZTBkMzdjMTY1NDkyYmQxNzk4MWE2MmNhYWVkYWZlOTg5OWJhNmMzMDU4Njg1NGQ5ZmE3MTU=",
"nbgplexmvdnzNjg0NTQ3N2VjYmI4YzMyZmZlYjBkOGY0ZThiMGIwY2I4YjM0NDgxMzNmYzE5ZDE5OGYzMDcxNGRhZDc0ZmUxMTdiOGRiMDZkMTk2ZDRkYzVhMTE2ZGI=",
"tvhelfuaolcpZmIxZWNjYjMzZDBjMjE1NGNmNDdmZWE4MGE5ZDA0Yzg3MzkwYzgxOTJiNmNkNDQzMTQyZDYyNWE3NDhiOTg5NGFhMjk1YzBmNGQ3YWM3MDM0ZGRiYzY=",
"oliqlklqrhhzY2NlMDVmYjlmZWRkYzY3NmU1MzFkMmZkMGUzNjA4YWFjMGU4ZTBiYmRlYWYwYWEzMzI4N2UwY2MyYWU5NzBiNDVkZTQ3NTE1MjAzNGNhMTM5MWMxMTU4YjcyMmFjNWU5Y2QyNDc3NWRmOWMxNDcyYWE3ZmE3M2FhOGZkNDJlZTg5MTMyMjk0ZDMxYTdjZTk4MjEzOWFlMTAwZmViMjliYzdiNzU0OTZlMzYwN2M1YWZjODc5OTA4MTIwMGEwZDlkZTQ3NTlmNDM5OWZlN2Y5NQ==",
"tlwlmjlnokgmM2M2MmFiMTE0OGQ3N2E4Njg3NzU0YjU5NmM5M2U2MmRiYzNlOWE1NDAxYjEwN2MzMTg2YzdjZmIzMTc5ZDlkNjhmMDgzZDU2NWVjNmJhZWUzMw==",
"cmkrnctsycelMGZkOTc0MTZiMDkwM2NkYTkxYzY4OWNkODhlYjFlNTRiOGFlOTFiY2ViMzY2MzY0ZWIyZjA4ZmY3NjAyZTA0NmVjM2EzYjA4NzlhNmU3MjkwYzk1MTAzYjZmMzlhNWMxZGJkOGY4",
"gxwhphghitwnYjU=",
"sqjrerefeaxpYmY=",
"julpdsxxwyvaM2Q1ZWE2ZGFiZmQ5MmE4MTFiNDE5YTdlYjQ2ODg2YWJlNjUzMWI1ZWQxOWM4MmU0Nzc4Y2RkYTRkYjQ4MWQ=",
"hmruhzeiqewaNGJiYzVkNTIxOGUzYTQxNGQ4Yzk0MmI3MWU3MjFkNGM3MDBmNThlYjk1ZmUxZDYxNGM5MmM5Mjc2MWFmMjBjY2Y1YTUxZTkwMmUzMGFlNGVmNTZh",
"gsitrjojunkxN2ZhZmJhNDYxMGNmMGE4ZmZiNDk1YWE2ZTE1Yjc3ZWM4ZGJmMTVjMzFlZjc3YWIzOTYzZjI0ODFjZjQzODU0Nzlm",
"wgikvubzgsriZGYxOTcyMzUzMGQxMjIyZDE5ODEwODY5MzI3ZGNlODU5OWMwYWYyMzlkYmNhNQ==",
"eekkjycconsnNzA1M2FhMWU3ZWZlM2IwZjM2MWVhNTQ1YTRjZTAzYTFiZTdjMmE4ODljYWIxYTk2OWJmYjc2Yzg3MzcyZjU2NWU3NWE2MTk0Y2E=",
"lpbjxvozwjvdNTJlZWUzYzY5NWE3ZWFmMDM3ZGMyMGQwZWNhZjE5OTMxODQ0MzVjMjdmNGRlMjU3ZTM0MWM2YWY3YTI4M2M3MmI1YjUzYw==",
"qlkhsrcvigdmMDI4YjkyZDk0MTRlN2YwYWJhNTQ2MWIyZGExOWE0YTJiYmMxZTQ2MmE4YjhiYWU5ZmE4ZmZiOWRkMjZhYjI5YzI0ZWM4MjU0",
"zrujaqvpsentYTBlYmY3NWMwODZkZmE4Mzk4OTgzZmVjOGE3NjAwMWIwOWY2Nzg3NmZhMTJkNWIzNmZlMWU4NzE4ODRhYTc0ZWVlM2ZkMzlh",
"svrilwvsrmswZGUxYzNhMDQ3Y2VlNzYwZjdiN2QzNGUyNDI2ZjI5ZWM1MDk5Nzg4ZDk3MWM0OTg4NjVkMzYzYjcyZDZlZjAwOGM2ZGVmZTI2OGQ3ZGMyMWZmMmVkZGQyY2JlMDNkYw==",
"kbmwcrgslvseNTY5NTNmYjhlMmNhZmM5ZDhlNWE4ZDA1Zjg4MzczNDhlYTEzYTFhYTZlYjA0ZjFhYTE2ODk0ZDQwYzY5ZjVjZWY1NjM2YTMxZTRkOGFlYzk2YjU2M2JmZDJlOTFkNTc0ZTA0ZjQxZDE=",
"grtmqxzdwvyaNGE5NmYzMjliNmVmNjMzNzVjMmE3Yjc3YjIxYjdlZTE3ZDg5NTQ0M2FhYjRmY2M1MWZiZDg4OGE2YWIxZWE1ZjQyMWJjMzdiNDkxMTJi",
"oaknswhuspdtMGNlN2Y4M2MzMTUyNzcyMzlmZTU3NzhmNTM5MjMwMWQ0ZDJkNjZiMDc0NTAyNzEwNGQxMGMzNzJjYjMzNmEyZmM0ZWRkZjhj",
"dspbkgardynuMzY2NzAyNmY1ZGJiYTBiZTQ3ZWVmMDhjYjI1YTU2ZDRlMDRlMmQwZTViMGM1YmIwOWI1YjFjNzRkNDY4ZWQwNjEyYTkwMjU4",
"xobqanczmvssNWE0MTQ5OGRjZGE3OGM1NjMzMTU3YWYzMTE1MjNlMTBmMDRlNDhkZTgzNjZmNzJiNzI5NjU1MGQyMDQzNDQ2MGUwNmY0YmYxOTYzNjY5ZThhYzAxNDVhNjIyMmNkY2JmMjYyN2JiNTg0YmVhYzhiMmE3NDQyOGI0MjlhNjZjMzhmOWE5YmY4MDRjZGY1Mw==",
"oczodqzepdmmNzlhOTg2NDFlODU4M2Y5NjVkNGU1MDMyNWYxM2FiMjBjNmNmZmIwODJjZTVjNzgwZDY4YTZhZDIyNGZjYzc=",
"vjcayptxmarvNGZmOWUxNGY4Mjg5MTI0ZGJiM2IyMDA1ODI4NjU3ZjdjZDg4NDRmYzNiNzMwNDgyZTkzNjM1ZDZhODcyOWY4NjA1YzBhNTIxYWJmZjgyMzE=",
"xwuhdyjgogekZDA1NzgxOWFjZWI5MjgzY2I2ZGQ5ZmJjMjliMzVkYTI1MjkwODczZWJiYjM2NDg2NjQyYTBiMDVkNDc3N2VkNWNkZTE2Y2QxYzI=",
"zmpsylnxpwgwOGYwMTY1YTc1YjNkNjY3MjI4ZjBiZDdhYTdkMGZjMzViOTRkZWRkNjcwYzU4ZmI2YWZjZWIwZWM4ZmQ5NDc1OWE0ZTI=",
"sxuqdothfchjNjBmMmE3N2Q5NTlkODAzNTg4NDg1YjgzMDEzNzcyYjQ3NmIyZWQxYWYzODllYmVkMGJlMzc2NjM1NGI4MGQxNzZmYmExNTQ2YmY1MDVjYTEwNmVkODY3MjJmNjRlZmI4ODRmMDRjYmUyNDI0YmY3ZWI3NWYzNjA3NzIxY2I2ZTk1Y2E5YTA5YmM1NmMzMDIyMmUyYzNhOTJiNDk3",
"kmfhjuqglrhpNTEwNDc5Y2RlMDRlZmYxZWZiM2VhYTBlNGJjZjEyY2Q3YzM3MmIxY2E2MmU4OGFlZGJiOTQzZGViYmY0NzE2NWI5OGUwYzZhYjFhMDJjMDNmZjVkYjQ=",
"osigewwdazgzNmU5NGE2N2FkNDhlMzlkZTE3MDc4NGE3MmQ2ODFmYjMzNTdmZDA0MmE0ODU5MWNlZGI5OWM1YmQwZmI4NDdhMjU5MTc0ODI0YjIzZTVmNTk3ODQ5OGJiNzZkMDI4MWQ3MDZmMDcxNjIyOGU3ZTVkMjM1YzBjYWJlYjVhNzhiNTljYmNkYTZjZDBhM2Q2ZmVjYTJjZjU3MGEwMmFmZWJmMDVkN2Q2NzFkM2JkZjFmZDRhMjA5NDkzYTMyNjllM2M2ZGRmZg==",
"etsovzuwrfvpNjJkMzQ4YzEzYjJmZTVmOTRlMTE3Y2ZjYTJhYjM1YjRhZTE3ZjA0NGYyMDNmM2YzYjkxYTA3NTE4NzlmYzdkNTY2MGJjMmQ1Yzg3Y2NhMTQ0MQ==",
"ngxaavexcccdODg4Yjk5ZjYyODZmMTFkZjBkMTkyMjRjNmVmZDYwZThjYTVkMGQyN2VkZmM5NWIzNDlmNjRhNWIzZWEyNWFjYmFjY2U2NGQ5",
"sriprgebmhhrYzNhZmUzYTliMjA5NDhhMjU3ZDZmMGU1YmU3NGRlN2RkMjRhZjU2ZDAwOTM0NzZjNDY1MTQwZTgzMmMwMmI3ZWVjYjQwN2YxODQ4ZmE3N2RhMjc2ODM3MzQ5ZTRkMTIyYmQ=",
"uwdizynapzezNWQwYzYxMDNhODY0MTE2MzFhMDk3ZDgwMTRjMDAwNDY4ZTc5NmJmZTc3N2IwNjNkM2M3OWM2N2M4OTc5OTMzYjljZTVhZWU3ZjYyOTkxNGNhZjU1MGEyYjFhNmVjOWMy",
"yvhombiqrtqpYWEzY2ZlMjYwZGQ2M2I4ODFjNTRmNGQ0MDA0ZTVlMDJjNTM2ZDgzODJhNTNhNTA4Y2Q3ZGViOTUzM2IzYzIyMDVmOWM4Y2QwOTg=",
"xlvaohlrcjewZmM4MzVkODQxYmU3YTU3Yjg0NTUwNjM5YzkyM2EwYWI2ZWU1YjE1MTliMWRkZGJmNjc0NmQ4OThlZGE3Y2YzYzI1",
"jbggsgguabgxZGJlOWUyNjVkNjNjOTRlYjhiMmNiNTk3NWViYzExZTc1ZDk1ZmMyNmE3MzFhMGFhZDE3MTdjOTAzZjdkYTFhZGYxZmFiY2VhYmZmNDA1ZGE3NzhmODEwMA==",
"kzucvtsmcgoxMDgzYmIxMGQzYjBjZjY0NjhkY2NhZTdmZDFkMjBkN2Y3MTU0MTU2ZmIzZmY2OGU0MDUxMmQ3NjAyNTkzNTY4NDU4NjJjYmU5YjllNGNmZmViNzNmZGRhOGUyNTE0YzA0ZTA1M2M3ODcxMzljMWQxNWMyNzVmZmFiNjFkMzIzZGY5MGMxY2I=",
"gyuqnhbzxcaeYmQwNzFiZWU5N2Q1ZTA0ODA3NDg0NGQwMTA1ZDdlZjQzMDNlYzExYmM4OWVhYmE0NGVkZDIzNDFkODgyZDg=",
"rgabxwtahoqzOTBjNDRiM2ExNjM1ODBlMzliOGI5ZTMyNzI1OTJiZjJjYjM0MmE3NDNjMTQ1Y2YyNWM0Yjk4ZThhOGFkMTA5YmNjZjNhZThlZGRjNWU0YWE1Zg==",
"dvkpqvfgohfuNGVlN2FmMzY1ZGZmMWQzYzhhZDFlMDQyMWU4MzY0NTdhMGIyNjQwYjBlMjViODlkMTY0MDc4MDllNmVjN2I5MmE0ZmIxMzg4Yjg1MmY0OGI=",
"tttykuqkxacrYjY4Y2ZmZDg2NTQyMTc3ZThkOGJkY2MwZWViMTUwMjc3NWVlZjczZGIyMzljODI2YzBkMTc3YWY2NzljY2Q1NTYxZjYzZDNjYWE4NTI3MDAzMTEyOGJkNjU2MTczZmMzMmY0NjkzYzIyNmU5OWRkZGZiNjUyYWRlYWQ5OTQxMTQ0YjNlNTNmYzVjYmUzMTI4NTgyNmY2ODZlZGMyMDVhN2JiY2VkNA==",
"jbxbajocsdstODRiYWVhM2EwMTIwNTQyYzU2MjI4NDBiZDBkMmY5NWU2NjcxNDliNWM1YzgzZmEyNjQ4MzlmODJhYzM0YWNlNzhjOTg2NzZmMGNkZTRkMzVkNA==",
"pbukgxbroxpvNmFmYWYwYWFmYzY5YjVkYjI2ZjdjZGE4MzE2YmQ0ZWNjYTkxOTRjYzMzMmU4MDUxZWI4YjI0ZjJiNTljYjM2NDljZTUzY2E2MzI1NGQzMGYzMg==",
"gxwhphghitwnYjU=",

"wnieauylswsaN2Y1ZmZiNmYzMDY0",
"tnehvpiwnbkaNzFmMTBhOGJmYzc0ZWVmYTRlMzc1YTJlY2VjMGUyOGRhYWUzOTY5MmFjNDQwZDYzYWY4ODliYWFjNTdhZDBjYw==",
"ursgomuinfklOTg4YmI4YzQzMWE2NjRhNmFlZDU0ZDNiOGVjMTRhMGZlM2I1OTM0YmFjZTg1Mw==",
"ypnsxzuumbfhMGI2YTE5YmI1YmUwM2MzNzgyZTIwMg==",
"flmxlipablzoMDY4YzQ4OWI4ZjkxOGNmNzNiNjhkMjQ4MmM0ZTllYTE5NWRi",
"slqflgbwkworZmFlZGUxZmNiY2NjN2M3OQ==",
"dezarfpgkkrmNDdmODY0NDE=",
"vrfgjwteocmvZTk3MWE2MTY1ZmQ2",
"vnfwgkmkpzvzNDg0MWUzMjdkNzliNTA1Ng==",
"tbspebytbakmOTc4YTM2NjM3ZDE5YjcyOGU3NTE1MDgxMjIxODc5"
    ]
for i in input:
    decode(i)

