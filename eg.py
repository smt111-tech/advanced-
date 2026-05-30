class Engine:
    def __init__(self,engineroom, diesel_type):
        self.engineroom = engineroom
        self.diesel_type = diesel_type

    def start(self):
        return f"Engine started in ({self.engineroom}using, {self.diesel_type})"
class Anchor:
    def __init__(self, weight):
        self.weight = weight


class Ship:
    def __init__(self,name, engine, Anchor_weight):
        self.name = name
        self.engine = engine                   # composed object
        self.anchor = [Anchor(Anchor_weight)] * 4  # list of composed objects

    def sail(self):
        engine_status = self.engine.start()
        return f"{self.engine} is sailing. {engine_status}"
    
    Engine1 =Engine("Main Engine Room","Diesel")
    Ship1 = Ship("titanic",Engine1,1000)



class Student:
    def __init__(self, name, age, matric_no, department, level, cgpa):
        self.name = name
        self.age = age
        self.matric_no = matric_no
        self.department = department
        self.level = level
        self.cgpa = cgpa


# Create an object
student1 = Student(
    "Shola",
    20,
    "CSC/2025/001",
    "Computer Science",
    200,
    4.50
)


print("Object type:", type(student1))

print("Is student1 a Student?", isinstance(student1, Student))


print("Has attribute 'cgpa'?", hasattr(student1, "cgpa"))


print("Student CGPA:", getattr(student1, "cgpa"))


print("All attributes and methods:")
print(dir(student1))

print("Object data:")
print(student1.__dict__)





