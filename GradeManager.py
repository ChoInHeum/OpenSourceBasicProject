##################################
# 프로그램 명: 성적 관리 프로그램
# 작성자: 조인흠
# 작성일: 2025/4/11
# 프로그램 설명: 성적에 따른 학점 부여 함수인 calculate_grade, 성적의 전체 평균을 계산하는 calculate_total_and_avg, 학생 데이터를 입력받는 input_student_data, 순위를 매기는 sort()함수로 구성되어 있음음
##################################

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

def calculate_total_and_avg(scores):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg

def input_student_data():
    students = []
    for i in range(5):
        student_num = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어: "))
        c_lang = int(input("C-언어: "))
        python = int(input("파이썬: "))
        total, avg = calculate_total_and_avg([eng, c_lang, python])
        grade = calculate_grade(avg)
        students.append([student_num, name, eng, c_lang, python, total, avg, grade])
    return students

def sort(students):
    students.sort(key=lambda x: x[5], reverse=True)
    for rank, student in enumerate(students, start=1):
        student.append(rank)
    
    print("=========================================================================================================================================")
    print("          학번          이름          영어          C-언어          파이썬          총점          평균          학점          등수          ")
    print("=========================================================================================================================================")
    for s in students:
        print(f"{s[0]:<15}{s[1]:<10}{s[2]:<10}{s[3]:<10}{s[4]:<10}{s[5]:<10}{s[6]:.2f}      {s[7]:<5}      {s[8]:<5}")

def main():
    students = input_student_data()
    sort(students)

if __name__ == "__main__":
    main()