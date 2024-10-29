"""

"""
import csv

# 전역 변수
assembler_coef = 0.75
furnace_coef = 2
terminal_ingredients = ["철 판", "구리 판", "돌", "석탄"]
denying = ["", "철 광석", "구리 광석", "돌", "석탄"]



# 이름을 받아서, 해당 이름을 가진 row를 반환하는 함수
def find_row(name, file_path="data.csv"):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == name:
                file.close
                return row
    raise Exception(f"{name}이라는 이름을 가진 row가 없습니다.")


# row를 받아서, 해당 재료 '하나' 만드는 데에 필요한 말단 재료로 변환하는 함수
def convert_to_terminal_ingredients(row):
    divider = float(row[2])
    count = [0 for _ in range(len(terminal_ingredients))]
    for i in range(4, 16, 2):
        for j in range(0, len(terminal_ingredients)):
            if (row[i] == terminal_ingredients[j]):
                count[j] += float(row[i+1])
            if (row[i] in denying):
                continue
            else:
                count[j] += convert_to_terminal_ingredients(find_row(row[i]))[j] * float(row[i+1])
    for k in range(len(terminal_ingredients)):
        count[k] /= divider
    return count
"""
        if row[i] == "철 판":
            iron += float(row[i+1])
        elif row[i] == "구리 판":
            copper += float(row[i+1])
        elif ((row[i] in terminal_ingredient) or (row[i] == "")):
            continue
        else: # 재귀적으로 호출
            iron += convert_to_iron_and_copper(find_row(row[i]))[0] * float(row[i+1])
            copper += convert_to_iron_and_copper(find_row(row[i]))[1] * float(row[i+1])

    iron /= divider
    copper /= divider
    return iron, copper
"""


# 목표 아이템을 1초에 count개 만들 때, 필요한 제작기와 개수
def assembler_per_count(item, count):
    row = find_row(item)
    count
    if row[1] == "조립기계":
        count = (count * float(row[3])) / (float(row[2]) * assembler_coef)
    elif row[1] == "용광로":
        count = (count * float(row[3])) / (float(row[2]) * furnace_coef)
    return row[1], count


# 필요한 제작기 개수 print
def print_assembler(item, count):
    row = find_row(item)
    crafter, assembler_count = assembler_per_count(item, count)
    print(f"1초에 {item} {count}개 만들 때 필요한 {crafter} 개수: {round(assembler_count, 3)}개 (필요 재료: ", end="")
    for i in range(4, 16, 2):
        if (row[i] != ""):
            if ((i != 4) and (row[i] != "")):
                print(", ", end="")
            print(f"{row[i]} {round(count * float(row[i+1]), 3)}개", end="")
    print(")")


# 재귀적으로 필요한 제작기 개수 print
def print_assembler_recursive(item, count):
    row = find_row(item)
    crafter, assembler_count = assembler_per_count(item, count)
    print(f"1초에 {item} {count}개 만들 때 필요한 {crafter} 개수: {round(assembler_count, 3)}개 (필요 재료: ", end="")
    for i in range(4, 16, 2):
        if (row[i] != ""):
            if ((i != 4) and (row[i] != "")):
                print(", ", end="")
            print(f"{row[i]} {round(count * float(row[i+1]), 3)}개", end="")
    print(")")
    for i in range(4, 16, 2):
        if not((row[i] in terminal_ingredients) or (row[i] == "")):
            print_assembler_recursive(row[i], count * float(row[i+1]))


# 한번에 다 출력하는 함수
def print_all_info(item, count):
    row = find_row(item)
    terminal = convert_to_terminal_ingredients(row)
    print(row)
    for element in terminal:
        print(f"{terminal_ingredients[terminal.index(element)]}: {element}개", end="")
        if (terminal.index(element) != len(terminal) - 1):
            print(", ", end="")
    print("")
    print_assembler_recursive(item, count)
    print("")


def main():
    print_all_info("자동화 과학 팩", 0.75)
    print_all_info("물류 과학 팩", 0.75)
    print_all_info("군사 과학 팩", 0.75)



if __name__ == "__main__":
    main()