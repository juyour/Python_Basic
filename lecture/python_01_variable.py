# 주석(comment) : 단순 메모, 개발 실행x
# 출력 함수( print)
# - ()안의 값을 출력
# - 변수 값 확인 용도 또는 메세지 출력 용도

print("hello python")

# 문자열 타입(String Type)
# - Python: '', "" -> String
# - C, Java: ''(Char), ""(String)

# 참고: Escape Code
# - 문법: \(역 슬러쉬) + @
# - 무자열 내의 일부 문자의 의미를 달리하여 특정한 효과 추가
# - 예) \n: 한 줄  개행,  \t: 탭(8칸 공백)
print("Hello \nPython")
print("Hello \tPython")

# 자료형(Type)
# - Python의 모든 자료형은 객체(Object)
# - C, Java언어 문자형(Char): 'A', 'E'
# 1) 문자열(String): "Hello", 'Hi'
# 2) 정수형(int): 3, 0, -1
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 예) 다양한 종류의 자료형을 사용하는 이유?
# - Java 정수형: byte, short, int, long
# - Python 정수형: int
# 만들어진지 오래 된 언어는 다양한 종휴의 자료형을 사용!
# 이유는: 자원(메모리를 효율적으로 사용하기 위해서!
# 예: 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
#     예를 들어서 int는 (-10000~10000)까지 담을 수 잇다고 가정
#     그런데 우리 회사에서 특정 값이 0~9만 사용!
#     int를 사용하게 되면 메모리 낭비, 이런 경우 크기의 범위가 더
#     작은 자료형을 사용하면 좋음(short)

#None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
# - 기타 언어의 Null과 같은 의미로 사용!
# 예) student_name
print("=" * 200)
student_name = None  # 적극 권장 X(절때 사용 금지)
student_name = ""  # 적극 권장 O
# 이유? "Null Pointer Excepthion" Error 개발 공포의 대상!!

# 기본 자료형(Primitive Type)
# 객체 자료형(Reference Type)
# * Java: 기본, 객체 모두 사용
# * Python: 객체만 사용

# C언어 변수 생성 -> int b; (변수 생성, 값X)
# Python 변수 생성 -> b(변수 호출)

# 변수(Variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간

print("=" * 200)
num = 4
unm = 10
print(num)  # 출력: 10
# - 변수 생성 및 초기화
# num = 5  #문법
#