from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Course(BaseModel):
    id: int
    name: str
    is_completed: bool

# database for now!
courses: List[Course] = []


@app.get('/')
def get_root():
    return {'message' : 'Welcome to courses list!'}


@app.get('/courses')
def get_courses():
    return courses


@app.post('/courses/add')
def add_course(course: Course):
    courses.append(Course)
    return course


@app.put('/courses/edit/{id}')
def edit_course(id: int, edited_course: Course):
    for idx, course in enumerate(courses):
        if course.id == id:
            courses[idx] = edited_course
            return edited_course
    return {'error' : 'course not found'}


@app.delete('/courses/delete/{id}')
def delete_course(id: int):
    for idx, course in enumerate(courses):
        if course.id == id:
            deleted = courses.pop(idx)
            return deleted
    return {'error' : 'course not found'}