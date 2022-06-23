import re

# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'
print('# 테스트 문자열 : {} \n {}'.format(text,'-'*50))

# 1. 소문자 찾기
result = re.findall('a',text)
print('# 1. 소문자 찾기 : ',result)

# 2. 소문자 찾기
result = re.findall('i',text)
print('# 2. 소문자 찾기 : ',result)

# 3. 대문자 찾기
result = re.findall('A',text)
print('# 3. 대문자 찾기 : ',result)

# 4. 소문자 전체 찾기
result = re.findall('[a-z]',text)
print('# 4. 소문자 전체 찾기 : ',result)

# 5. 소문자 연속해서 찾기
result = re.findall('[a-z]+',text)
print('# 5. 소문자 연속해서 찾기 : ',result)

# 6. 대문자 전체 찾기
result = re.findall('[A-Z]',text)
print('# 6. 대문자 전체 찾기 : ',result)

# 7. 숫자 전체 찾기
result = re.findall('[0-9]',text)
print('# 7. 숫자 전체 찾기 : ',result)

# 8. 숫자 연속해서 찾기
result = re.findall('[0-9]+',text)
print('# 8. 숫자 연속해서 찾기 : ',result)

# 9. 영문자 및 숫자 찾기
result = re.findall('[a-zA-Z0-9]',text)
print('# 9. 영문자 및 숫자 찾기 : ',result)

# 10. 영문자 및 숫자 연속해서 찾기
result = re.findall('[a-zA-Z0-9]+',text)
print('# 10. 영문자 및 숫자 연속해서 찾기 : ',result)

# 11. 영문자 및 숫자 아닌 문자 찾기
result = re.findall('[^a-zA-Z0-9]',text)
print('# 11. 영문자 및 숫자 아닌 문자 찾기 : ',result)

# 12. 영문자 및 '_' 특수 기호 찾기
result = re.findall('[\w]',text)
print('# 12. 영문자 및 '' 특수 기호 찾기 : ',result)

# 13. 영문자 및 '_'특수기호 연속해서 찾기
result = re.findall('[\w]+',text)
print('# 13. 영문자 및 ''특수기호 연속해서 찾기 : ',result)

# 14. 영문자 및 '_'특수기호 아닌 문자 찾기
result = re.findall('[\W]',text)
print('# 14. 영문자 및 ''특수기호 아닌 문자 찾기 : ',result)
