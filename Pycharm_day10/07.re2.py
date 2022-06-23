import re

text = """
옛날 옛적에 김진수라는 사람이 살았습니다.
그에게는 5형제가 있었는데, 김진수, 김진구, 김진용, 김진태, 김진욱 이렇게 다섯명 있었습니다.
그리고 그는 결혼을 해서 김찬영, 김준영, 김채영 3남매를 낳고 알콩달콩 행복하게 잘 살았습니다.
채영이가 좋아하는 사촌은 김예영이랑 김민영이랍니다. 김서영이는 본지가 너무 오래되었네요.
"""

print('-'*100, '\n# 형제들 이름 찾기')
pattern = re.compile('김진\w')

brother = pattern.findall(text)
print(brother)                 # '김진수' 중복값 존재

brother = sorted(set(brother)) # 세트형(중복 제거) 변경 후 정렬
print(brother)

print('-'*100, '\n# 아이들 이름 찾기')
pattern = re.compile('김\w영')

children = pattern.findall(text)
print(children)