from dataclasses import dataclass


@dataclass
class Student:
	name: str
	age: int
	grade: str


student = Student("Kavya", 20, "A")
print(student)
