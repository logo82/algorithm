#5/24

coinCount, price = map(int, input().split())

coinPriceList = []

for i in range(coinCount):
    coinPriceList.append(int(input()))
coinPriceList.sort(reverse=True)
#print(coinPriceList)

#큰 수부터 나눠 몫 더하고 나머지로 다음 숫자 계산
i = 0
coinNum = 0
while True:
    if price != 0:
        coinNum += price // int(coinPriceList[i])
        price = price % coinPriceList[i]
        i += 1
    else:
        break

print(int(coinNum))
