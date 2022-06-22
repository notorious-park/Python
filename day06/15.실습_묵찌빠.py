'''
묵찌빠 게임

STEP1 : 게임시작 출력
STEP2 : 가위(0), 바위(1), 보(2)를 하여 공격/수비 결정
STEP3 : [공격] / [수비] 묵(1), 찌(0), 빠(2) ?
STEP4 : 게임의 승부 or 공격/수비 결정?
STEP5 : 결과메시지를 보여준다


cf.컴퓨터는 랜덤값, 플레이어는 입력값
'''

import random

class GameMZP:

    # 속성
    player  = dict()
    com = dict()

    is_draw = bool()    # True : 비김 (step=0, 가위바위보)
    is_over = bool()    #  True : 종료 (step=0, 묵찌빠)

    is_attack = bool()  # True : 공격, False : 수비
    mode = str()    #공격/수비

    새로운_공격수 = str()

    matching = [{'1':'가위','2':'바위','3':'보'},
                {'1':'찌','2':'묵','3':'빠'}]

    def startgame(self):
        print('묵찌빠를 시작합니다.')

        #
        # while True:
        #     print('묵찌빠를 시작합니다.')
        #     user = input('가위(0) 바위(1) 보(2) 중 하나를 입력하세요!')
        #     com  = random.randint(0,2)
        #     if :
        #         pass
        #
    def step2(self):
        print('가위바위보해서 공격수비결정')
        # 사용자값 입력
        # 컴퓨터값 랜덤
        # 둘을 비교해서 이기면 공격, 지면 수비

        while True:
            print("플레이어 값 입력")
            player_no = input("가위(1)/바위(2)/보(3) ? ")
            self.player[player_no] = self.matching[0][player_no]
            # print("플레이어 : ", self.player)
            print("플레이어 : ", self.matching[0][player_no])
            player_val = self.matching[0][player_no]

            computer_no = str(random.randint(1,3))
            self.com[computer_no] = self.matching[0][computer_no]
            computer_val = self.matching[0][computer_no]
            print("컴퓨터 : ", self.matching[0][computer_no])

            # print("가위바위보 승부?")
            # self.is_draw = True
            if player_val == computer_val:
                self.is_draw = True
                print('가위바위보 다시')
                continue
            elif (player_val=='가위' and computer_val=='보') or (player_val=='바위' and computer_val=='가위')\
                        or (player_val=='보' and computer_val=='바위'):
                self.is_attack = True
                print('사용자 승리입니다. 공격하세요!')
                break
            else:
                self.is_attack = False
                print('사용자 패배입니다. 수비하세요!')
                break

   # STEP3: [공격] / [수비] 묵(1), 찌(0), 빠(2) ?
    def step3(self):

        while True:
           player_no = input("묵(2)/찌(1)/빠(3) ? ")
           self.player[player_no] = self.matching[1][player_no]
           # print("플레이어 : ", self.player)
           print("플레이어 : ", self.matching[1][player_no])
           player_val = self.matching[1][player_no]

           computer_no = str(random.randint(1,3))
           self.com[computer_no] = self.matching[1][computer_no]
           computer_val = self.matching[1][computer_no]
           print("컴퓨터 : ", self.matching[1][computer_no])

           if (player_val == '찌' and computer_val == '빠') or (player_val == '묵' and computer_val == '찌') \
                   or (player_val == '빠' and computer_val == '묵'):
               self.is_attack = True
               self.mode = '공격'
               self.새로운_공격수 = '사용자'
               print('{} 공격입니다. 공격하세요'.format(self.새로운_공격수))
               pass
           elif (player_val == '찌' and computer_val == '묵') or (player_val == '빠' and computer_val == '찌') \
                   or (player_val == '묵' and computer_val == '빠'):
               self.is_attack = False
               self.mode = '수비'
               self.새로운_공격수 = '컴퓨터'
               print('{} 공격입니다. 수비하세요'.format(self.새로운_공격수))
               pass
           else:
               self.is_over = True
               print('끝')
               break

    def step4(self):
        if self.새로운_공격수 == '사용자' and self.is_over:
            print('사용자 승리, 컴퓨터 패배')
        else:
            print('컴퓨터 승리, 사용자 패배')


gameMZP = GameMZP()
gameMZP.startgame()
gameMZP.step2()
gameMZP.step3()
gameMZP.step4()

