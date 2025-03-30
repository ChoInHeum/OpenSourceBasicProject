print("=========================================================================================================================================\n")
print("          학번          이름          영어          C-언어          파이썬          총점          평균          학점          등수          \n")
print("=========================================================================================================================================\n")
print("       2025041001      홍길동          80             88             90            256            86            B+            1  \n")



# 변수 선언
StudentNum = []
Name = []
EnglishScore = []
CScore = []
PyScore = []
Sum = []
Average = []
grade = []
Rank = []




# 사용자 입력
for i in range(5):
    StudentNum.append(input("학번: "))
    Name.append(input("이름: "))
    EnglishScore.append(input("영어: "))
    CScore.append(input("C-언어: "))
    PyScore.append(input("파이썬: "))
    Sum.append(EnglishScore + CScore + PyScore)
    Average.append(Sum/3)
    if Average <= 100 and Average >= 95:
        grade = "A+"
    elif Average < 95 and Average >=90:
        grade = "A0"
    elif Average < 90 and Average >= 85:
        grade = "B+"
    elif Average < 85 and Average >= 80:
        grade = "B0"
    elif Average < 80 and Average >= 75:
        grade = "C+"
    elif Average < 75 and Average >= 70:
        grade = "C0"
    elif Average < 70 and Average >= 65:
        grade = "D+"
    elif Average < 65 and Average >= 60:
        grade = "D0"
    elif Average < 60 and Average >= 55:
        grade = "E+"
    elif Average < 55 and Average >= 50:
        grade = "E0"
    else:
        grade = "F"
    


print("=========================================================================================================================================\n")
print("          학번          이름          영어          C-언어          파이썬          총점          평균          학점          등수          \n")
print("=========================================================================================================================================\n")