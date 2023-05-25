#5/24

total_day=0
#Day of the week
DOTW = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

userMonth, userDay = map(int, input().split())

#입력한 달의 전 달까지의 모든 요일 더해주기
for i in range(userMonth-1):
    total_day += month[i]

#유저가 입력한 날 더해주기(1일부터 세니 1 빼주기)
total_day += userDay - 1


print(DOTW[total_day % 7])



    

