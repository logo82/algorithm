#5/24

total_day=0
#Day of the week
DOTW = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

userMonth, userDay = map(int, input().split())

#�Է��� ���� �� �ޱ����� ��� ���� �����ֱ�
for i in range(userMonth-1):
    total_day += month[i]

#������ �Է��� �� �����ֱ�(1�Ϻ��� ���� 1 ���ֱ�)
total_day += userDay - 1


print(DOTW[total_day % 7])



    

