import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    day_price, month_price, quarter_price, year_price = map(int, input().split())
    plan = list(map(int, input().split()))
    day = [plan[i] * day_price for i in range(12)]
    month = [month_price if day[i] > month_price else day[i] for i in range(12)]
    quarter = []
    for i in range(12):
        price_3month = sum(month[i:i+3])
        if price_3month > quarter_price:
            price_3month = quarter_price
        quarter.append(price_3month)
    year = []
    for i in range(3):
        price_year = sum(month[:i])
        for j in range(i, 12, 3):
            price_year += quarter[j]
        year.append(price_year)
    print(month)
    print(quarter)
    result = min(year)
    if result > year_price:
        result = year_price
    print(f'#{tc}', result)
