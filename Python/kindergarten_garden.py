class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.rows = diagram.split("\n")
        self.children = sorted(students)
        
    def plant_swticher(self, plant):
        switcher={
            "V": "Violets",
            "R": "Radishes",
            "G": "Grass",
            "C": "Clover"}
        return switcher.get(plant,"Invalid name of plant!")
    
    def plants(self, name):
        student_id = self.children.index(name)
        student_plants = []
        for row in range(len(self.rows)):
            student_plants.append(self.plant_swticher((self.rows[row][student_id*2])))
            student_plants.append(self.plant_swticher(self.rows[row][student_id*2+1]))
        return student_plants
