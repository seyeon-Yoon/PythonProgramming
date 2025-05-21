import threading

## 함수 선언 부분 ##
def calc_sum(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i
    print(f"1+2+3+.....+ {limit} = {total}")

## 메인 코드 부분 ##
t1 = threading.Thread(target=calc_sum, args=(1000,))
t2 = threading.Thread(target=calc_sum, args=(100000,))
t3 = threading.Thread(target=calc_sum, args=(10000000,))

t1.start()
t2.start()
t3.start()
