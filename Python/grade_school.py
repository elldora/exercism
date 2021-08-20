class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            #print("the grade is in dict")
            self.students[grade].append([name])
        else:
            #print("the grade is not in dict")
            self.students[grade]=[]
            self.students[grade].append(name)
       

    def roster(self):
        sorted_students = dict(sorted(self.students.items()))
        #print(sorted_students)
        for key in sorted_students:
            sorted_students[key] = sorted(sorted_students[key])

        all_students = sorted_students.values()
        #[[,,], [,], []]
        #print(all_students)
        return [name for names in all_students for name in names]

    def grade(self, grade_number):
        return sorted(self.students[grade_number]) if(grade_number in self.students) else []
            
        

