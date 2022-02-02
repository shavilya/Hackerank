if __name__ == '__main__':

    no_of_students_english_sub = int(input())
    roll_no_english_sub = list(input().split(' '))
    no_of_students_french_sub = int(input())
    roll_no_french_sub = list(input().split(' '))

    english_sub = set(roll_no_english_sub)
    french_sub = set(roll_no_french_sub)

    difference_sub = english_sub.difference(french_sub)

    print(len(difference_sub))