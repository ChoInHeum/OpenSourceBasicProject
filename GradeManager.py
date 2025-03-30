print("=========================================================================================================================================")
print("          학번          이름          영어          C-언어          파이썬          총점          평균          학점          등수          ")
print("=========================================================================================================================================")

students = []

def calculate_grade(avg):
    if 95 <= avg <= 100:
        return "A+"
    elif 90 <= avg < 95:
        return "A0"
    elif 85 <= avg < 90:
        return "B+"
    elif 80 <= avg < 85:
        return "B0"
    elif 75 <= avg < 80:
        return "C+"
    elif 70 <= avg < 75:
        return "C0"
    elif 65 <= avg < 70:
        return "D+"
    elif 60 <= avg < 65:
        return "D0"
    elif 55 <= avg < 60:
        return "E+"
    elif 50 <= avg < 55:
        return "E0"
    else:
        return "F"

for i in range(5):
    student_num = input("학번: ")
    name = input("이름: ")
    eng = int(input("영어: "))
    c_lang = int(input("C-언어: "))
    python = int(input("파이썬: "))
    total = eng + c_lang + python
    avg = total / 3
    grade = calculate_grade(avg)
    students.append([student_num, name, eng, c_lang, python, total, avg, grade])

students.sort(key=lambda x: x[5], reverse=True)
for rank, student in enumerate(students, start=1):
    student.append(rank)

print("=========================================================================================================================================")
print("          학번          이름          영어          C-언어          파이썬          총점          평균          학점          등수          ")
print("=========================================================================================================================================")
for s in students:
    print(f"{s[0]:<15}{s[1]:<10}{s[2]:<10}{s[3]:<10}{s[4]:<10}{s[5]:<10}{s[6]:.2f}      {s[7]:<5}      {s[8]:<5}")
