class Student:
    def __init__(self, name, grade, missing_assignments):
        self.name = name
        self.grade = grade
        self.missing_assignments = missing_assignments
        
    def get_info(self):
        return f"Student Name: {self.name}\nGrade: {self.grade}\n# Missing Assignments: {self.missing_assignments}"
    
    def advance(self):
        if self.missing_assignments <= 3:
            self.grade += 1
            self.missing_assignments = 0
            print(f"Student has advanced from grade {self.grade - 1} to grade {self.grade}")
        else:
            print(f"Student has {self.missing_assignments} missing assignments, cannot move on yet")
            
    def __str__(self):
        return f"({self.name}, {self.grade}, {self.missing_assignments})"
    
    def __eq__(self, other):
        return self.name == other.name and self.grade == other.grade and self.missing_assignments == other.missing_assignments
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "grade":
            return self.grade
        elif key == "missing_assignments":
            return self.missing_assignments
        return None
        
s1 = Student("Michael", 11, 2)
print(s1.get_info())
s1.advance()
print(s1.get_info())
print()
print(s1.name)
print()
print(s1)
s2 = Student("Alice", 12, 1)
print(s2)
print(s1 == s2)
s3 = Student("Alice", 12, 1)
print(s2 == s3)
s4 = s2
print(s2 == s4)
print(s2.__eq__(s4))
print()
print(s1["name"])
print(s1["grade"])
print(s1["a"])