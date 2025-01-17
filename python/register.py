print('================================')
print("회원가입")
print('================================')

register=False  #회원가입 여부 확인

while not register: #False+not  = 참(실행)
    print('회원가입을 진행하시겠습니까? (y/n)')
    register_input = input('>> ') #y/n 입력받기
    register_input = register_input.lower()  #대문자를 입력해도 소문자로 통일

    if register_input == 'y':
        register=True

        print('================================')
        print("회원가입이 진행됩니다")
        print('================================')

    elif register_input == 'n':
        print('================================')
        print("회원가입이 취소됩니다")
        print('================================')
        exit()  #프로그램 전체 취소

    else :
        print('입력 값을 확인해 주세요') #register=False, 다시 처음으로 돌아감


users=[]

while True:

    user={}  #딕셔너리에 저장

    username = input('ID : ')
    while True:
        password = input('PW: ')
        password_confirm = input('PW 확인: ')
        if password==password_confirm:
            break
        else:
            print('패스워드가 일치하지 않습니다.')
    
    name=input('이름 : ')

    while True:
        birth_date = input('생년월일(6자리): ')
        if len(birth_date) == 6:
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다.")
    
    email = input('이메일: ')

    user['username'] = username
    user['password'] = password
    user['name'] = name
    user['birth_date'] = birth_date
    user['email'] = email

    users.append(user)
    print(users)

    print('--------------------------------------')
    print(f"{user['name']}님 가입을 환영합니다!")
    print('--------------------------------------')

    print('회원가입을 추가로 진행하시겠습니까? (y/n)')
    register_another_input = input('>> ')
    register_another_input = register_another_input.lower()

    if register_another_input == 'y':
        pass  #어떠한 작업도 수행하지 않고 넘어간다
    elif register_another_input=='n':
        exit() #프로그램 전체 취소