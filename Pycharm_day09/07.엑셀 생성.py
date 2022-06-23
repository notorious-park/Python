import openpyxl
import os

try:
    chk_list = os.listdir()
    print(chk_list)
    if 'data' not in chk_list:
        os.mkdir('data')
except Exception as err:
    print(err)

#excel_file = 'data/basic.xlsx'   # 파일명
excel_file = 'data/JBFG_임직원.xlsx'


# 엑셀파일 생성
wb = openpyxl.Workbook()

# Sheet - 현재 활성화된 시트 선택
# ws = wb.active
ws = wb.create_sheet('요온_작업v2')   # 기본 default 값으로 sheet 생성

# 시트 이름 변경
# ws.title = '요온_작업'

# 워크시트 삭제
del wb['Sheet']

# 엑셀파일 저장
wb.save(excel_file)

print('프로그램 종료!')