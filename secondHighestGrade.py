n = int(input())
students = []
for i in range(n):
	name = input()
	grade = float(input())
	students.append([name,grade])

second_highest = sorted(list(set([grade for name, grade in students])))[1]

print('\n'.join([a for a,b in sorted(students) if b == second_highest]))