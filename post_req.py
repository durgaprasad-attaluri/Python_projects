# POST: Send data to the server like submitting a form, adding a new user, or saving a message.

# Youtube link: https://www.youtube.com/watch?v=sw8V7mLl3OI&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&index=6

## Request Body:- The data we send to the server
   # It has name, age, gender etc

'''
Steps:
1. POST
2. Validate: Using PyDantic model
3. Add record if the data is valid or correct
'''

from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal 
import json 

app=FastAPI()
class Student(BaseModel):
    id:Annotated[str, Field(..., title="ID of the student", example="101")]
    name:Annotated[str, Field(..., title="Student name(between 3 and 25 characters)", example="John", min_length=3, max_length=25)]
    city: Annotated[str, Field(title="City of the student must be 20 characters", max_length=30)]
    age: Annotated[int, Field(title="Student age(must be between 10 and 25)", ge=10, le=25)]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., title="Gender of the student(Male, Female, Others)")]
    marks: Annotated[int, Field(..., title="Marks of the tudent(must be between 0 and 100)", gt=0, le=100)]
    
    # Assign Grade based on marks
    @computed_field
    def grade(self)->str:
        if self.marks>85:
            return "A"
        elif self.marks>75 and self.marks<85:
            return "B"
        elif self.marks>50 and self.marks<75:
            return "C"
        else:
            return "D"
        
    @computed_field
    def res(self)->str:
        if self.grade=="D":
            return "Fail"
        return "Pass"

def load_data():
    with open('students.json', 'r') as f:
        data=json.load(f)

    return data

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.post('/create')
def create_stu(student:Student):
    data=load_data()

    # Check the new data laready exists or not
    if student.id in data:
        raise HTTPException(status_code=400, detail="Student laready exists.")
    
    # ADd student data
    data[student.id]=student.model_dump(exclude={'id'})

    # Save into the json file

    save_data(data)

    return JSONResponse(status_code=201, content={"message":"New student added successfully."})