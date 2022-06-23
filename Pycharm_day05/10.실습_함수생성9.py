#Documentation strings (docstring)

def my_function():
    '''
    아무것도 하지 않지만, 문서만 기술한 함수
    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
    '''
    pass

print(my_function.__doc__)

def introduce_your_family(name, *family_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    Args:
    name : 자기이름 입력하기
    *family_names : 가족이름 입력하기
    **family_info : 가족소개하기
    :return: 없습니다/
    '''
    pass