from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated, Literal, Optional
import json

from post_req import Student

# Put =>Update
## /edit steps-> which student id we want to update, in that id whihc field-age, name, city etc

## Creating a PyDantic model that has all features that user want to update which
    ## We are making them optional as we don't know which feature user will update
class StudentUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age:  Annotated[Optional[int], Field(default=None, gt=0, le=30)]
    gender: Annotated[Optional[str], Field(default=None)]
    marks: Annotated[Optional[int], Field(default=None, gt=0, le=100)]

def load_data():
    with open('students.json', 'r') as f:
        data=json.load(f) 
    return data

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

# If the update is valid, we will update
app=FastAPI()

@app.put('/edit/{student_id}')
def update_student(student_id:str, student_update:StudentUpdate):
    #print(student_update) # For debugging

    data=load_data()

    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Get the existing student record to update
    existing_student_info = data[student_id]

    # # Pydantic obj to dict
    updated_student_info=student_update.model_dump(exclude_unset=True)  # output is like {'name': updated name, 'city':updated city}

    for k, v in updated_student_info.items():
        existing_student_info[k]=v   # Updating the new valuesin the exisiting data

    # Resetting grade and result in the updated student data

    # Since 'id' is not in our existing dtudent data we will add and pass to our student pydantic model
    existing_student_info['id']=student_id
    stude_pydantic_obj=Student(**existing_student_info) # pydantic obj for updated student data

    # # Pydantic obj to dict
    existing_student_info=stude_pydantic_obj.model_dump(exclude='id')


    #existing_student_info.update(updated_fields)

    # updated_student_data = Student(id=student_id, **existing_student_info)
    # updated_student_data_dict = updated_student_data.model_dump(exclude={"id"})
    # add dict to data
    data[student_id]=existing_student_info

    # save the data
    save_data(data)

    return JSONResponse(status_code=200, content="Successfully updated.")


## Delete student info
@app.delete('/delete/{student_id}')
def del_stu(student_id:str=Path(..., description="Enter the id to update")):
    data=load_data()

    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    del data[student_id]
    save_data(data)
    return JSONResponse(status_code=200, content={'message':"Deleted sucessfully."})
