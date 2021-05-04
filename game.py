print("--게임--")

userdict = {
    'health' : 100,
    'mana' : 100,
    'attack_damage' : 10,
    'mizardry_damage' : 10,
    'movement_speed' : 300,
    'money':1000
}

mondict = {
    'health':500
}

joblist=['1. 검사', '2.마법사']

storelist=['1. 공격력 강화','2. 마법전투력 강화','3. 상점나가기']

def skillenhance():
    userdict['mizardry_damage'] +=20

def attackenhance():
    userdict['attack_damage'] +=20

def myinfor():
    print()
    print("================================")
    print("[캐릭터정보]")
    print("현재 체력 : "+str(userdict['health']))
    print("현재 마나 : "+str(userdict['mana']))
    print("공격데미지 : "+str(userdict['attack_damage']))
    print("스킬데미지 : "+str(userdict['mizardry_damage']))
    print("돈 : "+str(userdict['money']))
    print("================================")
    print()

def monster():
    print()
    print("[괴물정보]")
    print("체력 : "+str(mondict['health']))

userdict['name'] = input("당신의 이름은 무엇인가요? ")
while True:
    print(joblist)
    userdict['type'] = int(input("캐릭터의 직업을 골라주세요 : "))
    if userdict['type']==1:
        userdict['attack_damage'] = 40
        userdict['health'] = 150
        print("검사를 고르셨습니다. 당신의 공격 데미지는 "+str(userdict['attack_damage'])+"로 증가하고 체력이 "+str(userdict['health'])+"로 증가합니다.")
        break
    elif userdict['type']==2:
        userdict['mizardry_damage'] = 40
        userdict['mana'] = 200
        print("마법사를 고르셨습니다. 당신의 스킬데미지는 "+str(userdict['mizardry_damage'])+"로 증가하고 마나가 "+str(userdict['mana'])+"로 증가합니다.")
        break
    else:
        print("다시 골라주세요")
        continue
print()
print()
print("------------------------------------------")
print(userdict['name']+"님, 게임을 시작하겠습니다.")
print()
print()
myinfor()
while True:
    print("[1. 전투 2. 상점 3. 종료]")
    i = int(input("어디로 향하시겠습니까? : "))
    if i == 1:
        print("괴물을 만났습니다. 해치워주세요.")
        monster()
        while True:
            k=int(input("1. 공격 2. 스킬 3. 포기 : "))
            if k==1:
                mondict['health'] -= userdict['attack_damage']
                if mondict['health'] <=0:
                    userdict['money'] +=1000
                    myinfor()
                    print("괴물을 해치웠어요!!!")
                    print("1000원의 보상을 획득하였습니다. 축하합니다!")
                    mondict['health']=500
                    break
                else:
                    monster()
            elif k==2:
                mondict['health'] -= userdict['mizardry_damage']
                if mondict['health'] <=0:
                    userdict['money'] +=1000
                    myinfor()
                    print("괴물을 해치웠어요!!!")
                    print("1000원의 보상을 획득하였습니다. 축하합니다!")
                    mondict['health']=500
                    break
                else:
                    monster()
            elif k==3:
                print("처치하지못하셨습니다. 화면으로 돌아갑니다.")
                monster()
                mondict['health']=500
                break
            else:
                print("다시 선택해주세요.")
                continue

    elif i == 2:
        print("돈을 사용하여 당신의 능력을 올리실 수 있습니다.")
        print("강화비용은 회당 200원입니다.")
        print()
        while True:
            print(storelist)
            j=int(input("무엇을 강화하시겠습니까? : "))
            if j == 1 and userdict['money']>=200:
                attackenhance()
                userdict['money'] -=200
                myinfor()
                print("공격데미지가 20 오르셨습니다.")
                print()
            elif j == 2 and userdict['money']>=200:
                skillenhance()
                userdict['money'] -=200
                myinfor()
                print("스킬데미지가 20 오르셨습니다.")
                print()
            elif j==3:
                print("상점을 나가겠습니다.")
                print()
                break
            elif (j == 1 or j == 2) and userdict['money'] <200:
                print("돈이 충분하지않습니다. 자동으로 상점을 나가겠습니다.")
                print()
                break
            else:
                print("잘못입력하셨습니다. 다시 선택해주세요.")
                print()
                continue
    elif i == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")
        print()
        continue
    