if __name__ == '__main__':
    no_of_students_sub_to_english = int(input())
    roll_numbers_of_english_sub_students = list(input().split(' '))
    no_of_students_sub_to_french = int(input())
    roll_numbers_of_french_sub_students = list(input().split(' '))

    set_english = set(roll_numbers_of_english_sub_students)
    set_french = set(roll_numbers_of_french_sub_students)

    union_method = set_english.intersection(set_french)
    print(len(union_method))