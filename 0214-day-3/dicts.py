grades = {'Alice': 76,
          'Michael': 91,
          'Bob': 52}

print(grades)
print(grades['Alice'])
print(grades.get('Alice'))

print(list(grades.keys()))
print(list(grades.values()))
print(list(grades.items()))
print()

student_rosters = { 'class-1' : ['Bob', 'Alice', 'John'],
                    'class-2' : ['Gary', 'Grace'] }

for key, value in student_rosters.items():
    print(key, value)
    
counts = {}

counts[1] = 3

print(counts)

counts[1] += 1

print(counts)