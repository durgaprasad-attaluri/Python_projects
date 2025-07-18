from fastapi import FastAPI, Path, Query
import json

app=FastAPI()

def load_data():
    with open('students.json', 'r') as f:
        data=json.load(f)

    return data

@app.get("/")
def home():
    return {'message': 'Student details API'}

@app.get('/about')
def abt():
    return {'message': 'API for Student details.'}

# View all the Student details
@app.get('/view')
def view():
    data=load_data()
    return data

## Path & Query Params  : https://www.youtube.com/watch?v=VVVKEfhXCQ4
  ### Path  : Get the student details whose id is 103
  ### Query : Get student details whose gender is male

## Path examples: Declared directly within the URL path using curly braces, like /items/{item_id}.
@app.get("/student/{student_id}")
def view_id(student_id:str):
    data=load_data()

    if student_id in data:
        return data[student_id]
    return {'error': 'student not found ):.'}

# Get student details with gender

## Path: A function to declare path parameters, add validation rules, add metadata like description
    ## Path(...)	Tells FastAPI this is a required path parameter, other parameters: title(short, one-line label), description(Longer explanation), example, (ge, gt, le, lt), min_length, max_length, regex  
@app.get("/student/gender/{gender}")
def get_gender(gender:str=Path(..., title="Gender of the student Male/Female", example="Female")):
    data=load_data()

    gen_data={id:info for id, info in data.items()
              if info['gender'].lower()==gender.lower()}
    return gen_data

# Get student details with their city
@app.get('/student/city/{city}')
def get_city(city:str):
    data=load_data()
    res={id:info for id, info in data.items() if info['city'].lower()==city.lower()}

    return res

## Query examples: Defined in the URL after a question mark (?) as key-value pairs, such as /items/?skip=0&limit=10. 
    # For filtering, sorting, searching and pagination(multiple pages to single page) without altering the endpoint path itself
    ## pagination: splitting large sets of data into smaller chunks("pages"), so users or clients can load data one page at a time, instead of all at once.
    
    # Here each parameter is a key-value pair

# Get by gender: http://127.0.0.1:8000/student?gender=Male
@app.get('/student')
def get_q_gender(gender:str):
    data=load_data()

    res={id:info for id, info in data.items()
            if info.get('gender').lower()==gender.lower()}
    
    return res

# Get by gender and city
@app.get('/student/info/G-C')
def get_gen_city(gender:str, city:str):
    data=load_data()

    # logs
    print(f"student details of {gender} with {city}")

    # res={id:info for id, info in data.items()
    #         if info['gender'].strip().lower()==gender.strip().lower() and 
    #         info['city'].strip().lower()==city.strip().lower()}

    res = {
        id: info for id, info in data.items()
        if info.get('gender', '').strip().lower() == gender.strip().lower()
        and info.get('city', '').strip().lower() == city.strip().lower()
    }
    
    if not res:
        return {'error': 'no student found with the given details.'}
    
    return res


## Sort

### Query: Like we have 'Path' function in Path params
@app.get('/sort')
def sort_age(sort_by:str=Query(..., title="Sorting by age", example='age'), 
             order:str=Query('asc',description="sort in asc or desc", example='asc/desc')):
    
    # Check the correct attributes that user selected
    if sort_by != 'age':
        return {'error': 'Pleasae select age'}
    
    sort_order=True if order == 'desc' else False

    data=load_data()
    res=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return res


# Custom sort: User can select among 'age', 'marks'
@app.get('/custom_sort')
def sort_age(sort_by:str=Query(..., title="Sorting by age", example='age/marks'), 
             order:str=Query('asc',description="sort in asc or desc", example='asc/desc')):
    
    # Check the correct attributes that user selected
    if sort_by not in ['age', 'marks']:
        return {'error': "Pleasae select the correct parameter 'age' or 'marks' "}
    
    sort_order=True if order == 'desc' else False

    data=load_data()
    res=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return res