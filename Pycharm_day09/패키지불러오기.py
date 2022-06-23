
from Packages.golf import *

# 대상 작업파일
excel_file = "data/golf_score_board.xlsx"

# 대상자 파일
filename = "./data/명단.txt"

## 미션0 : 엑셀등록과 시트선정
'''
(1) loading_excel함수 => 대상작업파일 등록
(2) ws               => 스코어 시트 작업하기
(3) ws2              => 대회결과
'''
loading_excel(excel_file)
# wb, ws, ws2 = loading_excel(excel_file) # 결정1. 패키지에서 되게할지 결정

## 미션1 : 참가선수들 등록 (실시간입력/등록명단파일호출)
'''
'''
선수등록(filename, excel_file)

## 미션2 : 참가선수들 HOLE별 스코어를 랜덤하게 입력
'''
'''
난수뿌리기(filename, excel_file)

# # 미션3 : 18홀까지의 스코어, 보정치를 계산하여 등록 (핸디는 옵션), 보정치는 없다. 1개 함수
'''
'''
스트로크합산(filename,excel_file)

# # 미션4 : 보정치 기준으로 랭킹 등록, 각종 기록 갯수 등록, 5개 함수
선수점수가져오기(filename,excel_file)
선수점수정렬() #없음
등수만들기()  #없음
랭킹채우기(filename,excel_file)
기록카운트(excel_file)

# # 미션5 : 대회결과 시트에 결과에 맞는 선수명과 최종성적/기록수를 등록, 2개 함수
선수정보담기(excel_file)
대회결과(excel_file)
최고기록선수넣기()

# wb.save(excel_file) # 결정1. 패키지에서 되게할지 결정
# print('프로그램 종료')