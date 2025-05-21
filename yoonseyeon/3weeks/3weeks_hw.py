# 진수 변환 프로그램
def convert_number():
    base = int(input("입력 진수 결정(16/10/8/2) : "))
    value = input("값 입력 : ")

    # 입력값을 정수로 변환
    num = int(value, base)

    print(f"\n16진수 ==> 0x{num:x}")
    print(f"10진수 ==> {num}")
    print(f"8진수 ==> 0o{num:o}")
    print(f"2진수 ==> 0b{num:b}")

convert_number()
