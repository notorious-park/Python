#BMI 계산

weight = float(input("당신의 체중(kg)은 얼마입니까?"))
height = float(input("당신의 키(cm)는 얼마입니까?"))

#BMI 계산
height = height / 100 #단위 수정
bmi = weight / height ** 2

#시뮬레이션
result = '' #변수 선언 안할 경우, 아래에 해당되는 CASE 없으면 오류남 / 여기선 상관 없음
if bmi < 18.5:
    result = '[마른체형] 면봉의 몸을 지니셨습니다.'
elif (bmi >= 18.5) and (bmi < 25): #그냥 하나로 묶어서 써도 됨
    result = '[정상체형] 보통의 체격이시군요!'
elif (bmi >= 25) and (bmi < 30): #그냥 하나로 묶어서 써도 됨
    result = '[약간 비만] 살크업의 징조가 보입니다. 관리가 필요합니다.'
# elif bmi >= 30:
#     result = '심한 비만'
else: result = '[심한 비만] 지금 이순간에도 무엇을 먹고 계시지 않나요?'

#최종 결과
print('BMI 지수 : ',int(bmi))
print('BMI 판정 : ',result)