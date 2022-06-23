#unpacking - 예제1
def get_area(w,h):
    return w*h

data = 10,20 #tuple형
print(type(data))

#print(get_area(data)) #오류 발생 : 튜플형이나 그 자체 셋을 1개로 봐서 읽히지 않음
#unpacking
print(get_area(*data)) # * : unpacking (튜플형)


#unpacking - 예제2
def introduce(name,greeting,bye):
    return '{}님, {} {}'.format(name,greeting,bye)

introduce_dict = {
    'name' : '박요온',
    'greeting' : '반갑습니다',
    'bye' : '안녕히 가세요'
}
#unpacking
print(introduce(**introduce_dict)) # ** : unpacking (사전형)