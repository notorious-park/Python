# 데이터 입력 / 변수 선언 / 로직 구현 / 출력물 산출!!!

books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

for book in books:  # 책 한 권씩 꺼내기 위한 루프 선언
    print(book)     # 책 한 권 데이터 출력

many_page = list()                              # 책 리스트 선언
recommends = list()                             # 책 리스트 선언
all_pages = int()                               # 전체 쪽수 변수 선언
pub_companies = set()                           # 출판사 집합 선언

# 로직구현 # if 쓰고 elif 쓰면 나머지 중 조건 찾기 / if 쓰고 또 if 쓰면 다시 원 Data 중 조건 찾기
for book in books:
    if book['쪽수'] > 250:
        many_page.append(book['제목'])
    if book['추천유무']:    # 굳이 == True 안써도 됨 / Default 값 : True
        recommends.append(book['제목'])
    all_pages = all_pages + book['쪽수']
    pub_companies.add(book['출판사'])

print('쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)



# 좋은 방법 - 추후에 적응이 됬을 때는 이런식으로 쿼리 짜보기
many_page1     = [book['제목'] for book in books if book['쪽수'] > 250] #리스트형
recommends1    = [book['제목'] for book in books if book['추천유무']] #리스트형
pub_companies1 = {book['출판사'] for book in books} #세트형
all_pages1     = sum([book['쪽수'] for book in books])
# all_pages2     = sum(book['쪽수'] for book in books)

print('쪽수가 250 쪽 넘는 책 리스트:', many_page1)
print('내가 추천하는 책 리스트:', recommends1)
print('내가 읽은 책 전체 쪽수:', all_pages1)
# print('내가 읽은 책 전체 쪽수:', all_pages2)
print('내가 읽은 책의 출판사 목록:', pub_companies1)