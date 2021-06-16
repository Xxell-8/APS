def what_day(a, b):
    # 1. 월별 날짜 수
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2. 요일의 이름
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    # 3. 1월 1일부터 며칠이 지났는지 계산 > 요일 계산
    today = sum(month[:a-1]) + b
    return week[(today-1) % 7]

print(what_day(5, 24))