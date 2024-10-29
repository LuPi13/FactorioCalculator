"""

"""
import csv

# 전역 변수; 조립기계2, 강철 용광로 계수
assembler_coef = 0.75
furnace_coef = 2



# 이름을 받아서, 해당 이름을 가진 row를 반환하는 함수
def find_row(name, file_path="data.csv"):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == name:
                return row
    raise Exception("해당 이름을 가진 row가 없습니다.")


# row를 받아서, 해당 재료 '하나' 만드는 데에 필요한 철 판과 구리 판 개수를 튜플 (철, 구리)로 변환하는 함수
def convert_to_iron_and_copper(row):
    divider = float(row[2])
    iron = 0
    copper = 0
    for i in range(4, 16, 2):
        if row[i] == "철 판":
            iron += float(row[i+1])
        elif row[i] == "구리 판":
            copper += float(row[i+1])
        elif ((row[i] == "구리 광석") or (row[i] == "철 광석") or (row[i] == "")):
            continue
        else: # 재귀적으로 호출
            iron += convert_to_iron_and_copper(find_row(row[i]))[0] * float(row[i+1])
            copper += convert_to_iron_and_copper(find_row(row[i]))[1] * float(row[i+1])

    iron /= divider
    copper /= divider
    return iron, copper


# 목표 아이템을 1초에 count개 만들 때, 필요한 조립기계 개수
def assembler_per_count(item, count):
    row = find_row(item)
    return (count * float(row[3])) / (float(row[2]) * assembler_coef)


# 재귀적으로 필요한 조립기계 개수 print
def print_assembler_recursive(item, count):
    row = find_row(item)
    assembler = assembler_per_count(item, count)
    print(f"1초에 {item} {count}개 만들 때 필요한 조립기계 개수: {round(assembler, 3)}개 (필요 재료: ", end="")
    for i in range(4, 16, 2):
        if (row[i] != ""):
            print(f"{row[i]} {round(count * float(row[i+1]), 3)}개, ", end="")
    print(")")
    for i in range(4, 16, 2):
        if not((row[i] == "구리 판") or (row[i] == "철 판") or (row[i] == "")):
            print_assembler_recursive(row[i], count * float(row[i+1]))


# 한번에 다 출력하는 함수
def print_all_info(item, count):
    row = find_row(item)
    iron, copper = convert_to_iron_and_copper(row)
    print(row)
    print(f"필요한 철: {iron}, 필요한 구리: {copper}")
    print_assembler_recursive(item, count)


def main():
    print_all_info("전자 회로", 3)
    print_all_info("자동화 과학 팩", 0.75)
    print_all_info("물류 과학 팩", 0.75)



if __name__ == "__main__":
    main()