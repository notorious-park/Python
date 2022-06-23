# ★★★★★ 최종정리 ★★★★★
# 1) 리스트형 list()  : 변경 가능 / 중복 허용 []
#                      추가 : append, insert / 삭제 : remove, pop / 변경 : list[old변수 순서] = new변수

# 2) 튜플형  tuple()  : 변경 불가 / 중복 허용 ()
#                      추가 / 삭제 / 변경 불가

# 3) 세트형  set()    : 변경 가능 / 중복 불가 {}
#                      추가 : add / 삭제 : discard, remove

# 4) 사전형  dict()   : 변경 가능 / 중복 불가 {} -> 000 : 000으로 묶음으로 구성
#                      추가 및 변경 : dict['Variable'] = 'Value' / 삭제 del

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
for x in books:
    if x['쪽수'] > 250:
        many_page.append(x['제목'])
    if x['추천유무']:
        recommends.append(x['제목'])
    all_pages += x['쪽수']
    pub_companies.add(x['출판사'])

print('쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)


# ------------------------------------------------------------------------------
# ★★★★★ 기본 구성 : 확인코자하는 변수  /  for x in 라이브러리  /  if 조건문 ★★★★★
# ------------------------------------------------------------------------------
many_page1 = [x['제목'] for x in books if x['쪽수'] > 250]
recommends1 = [x['제목'] for x in books if x['추천유무']]
all_pages1 = sum(x['쪽수'] for x in books)
pub_companies1 = {x['출판사'] for x in books}

print('쪽수가 250 쪽 넘는 책 리스트:', many_page1)
print('내가 추천하는 책 리스트:', recommends1)
print('내가 읽은 책 전체 쪽수:', all_pages1)
print('내가 읽은 책의 출판사 목록:', pub_companies1)