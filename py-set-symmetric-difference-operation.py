no_of_students_who_subscribed_for_english = int(input())
rollnum_of_english_student = set(input().split(' '))
no_of_students_who_subscribed_for_french = int(input())
rollnum_of_french_student = set(input().split(' '))

symmetric_difference = rollnum_of_english_student.symmetric_difference(rollnum_of_french_student)

print(len(symmetric_difference))