from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sshcalculations import totalMarks, averageMarks, gradeAssignment


app=FastAPI()

class StudentInput(BaseModel):
    id: int
    name: str
    marks: List[float]

students_db=[]

@app.post("/add_students/")
def add_students(student:StudentInput):
    total=totalMarks(student.marks)
    average=averageMarks(student.marks)
    grades=gradeAssignment(average)

    student_list={
        "id": student.id,
        "name" : student.name,
        "marks" : student.marks,
        "totalmarks" : total,
        "averagemarks" : average,
        "grade": grades
    }
    for s in students_db:
        if s["id"] == student.id:
            return {"message": "Student ID already exists"}
    
    students_db.append(student_list)
    
    return {"message": "Student added successfully", "student": student_list}

# Get all students
@app.get("/students")
def get_all_students():
    return students_db

# Get student by name
@app.get("/students/name/{name}")
def get_student_by_name(name: str):
    for student in students_db:
        if student["name"] == name:
            return student
    return {"message":"Student not found"}

@app.get("/students/id/{id}")
def get_student_by_id(id : int):
    for student in students_db:
        if student["id"] == id:
            return student
    return {"message":"Student not found"}



@app.put("/students/id/{id}")
def update_student(id: int, updated_student: StudentInput):
    for index, student in enumerate(students_db):
        if student["id"] == id:
            total = totalMarks(updated_student.marks)
            average = averageMarks(updated_student.marks)
            grades= gradeAssignment(average)

            students_db[index] = {
                "id": id,
                "name": updated_student.name,
                "marks": updated_student.marks,
                "totalmarks": total,
                "averagemarks": average,
                "grade": grades
            }

            return {"message": "Student updated successfully"}

    return {"message": "Student not found"}


@app.delete("/students/id/{id}")
def delete_student(id: int):
    for index,student in enumerate(students_db):
        if student["id"] == id:
            students_db.pop(index)
            return {"message": "student removed successfully"}

    return{"message":"student not found"}