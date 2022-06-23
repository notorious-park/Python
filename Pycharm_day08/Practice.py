# 순서 1) 원하는 Data Set 설정 list / dict 등
# 순서 2) 확인하고자 하는 변수의 Data Set 설정 list / dict or   int 등
# 순서 3) 확인하고자 하는 변수 로직 구현
#        항상 for문 반복 / Ex) for book in books if ~~~


books = list()

books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

for book in books:
    print(book)

many_pages = list()
recommends = list()
all_pages = int()
pub_companies = set()

year_2014 = list()
year_2014_pages = int()

many_pages = [book['제목'] for book in books if book['쪽수'] >= 250]
print(many_pages)

recommends = [book['제목'] for book in books if book['추천유무']]
print(recommends)

all_pages = sum(book['쪽수'] for book in books)
print(all_pages)

pub_companies = {book['출판사'] for book in books}
print(pub_companies)

year_2014 = [book['제목'] for book in books if int(book['출판연도']) >= 2014]
print(year_2014)

year_2014_pages = sum(book['쪽수'] for book in books if int(book['출판연도']) >= 2014)
print(year_2014_pages)