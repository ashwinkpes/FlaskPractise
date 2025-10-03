from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from . import models, schemas, crud, auth, dependencies, exceptions, database
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
app.add_exception_handler(HTTPException, exceptions.http_exception_handler)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.name, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.create_employee(db, employee)

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_user)):
    return crud.get_employees(db, skip=skip, limit=limit)

@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.create_department(db, department)

@app.get("/departments/", response_model=list[schemas.Department])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_user)):
    return crud.get_departments(db, skip=skip, limit=limit)

@app.put("/departments/{department_id}", response_model=schemas.Department)
def update_department(department_id: int, department: schemas.DepartmentBase, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.update_department(db, department_id, department)

@app.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.delete_department(db, department_id)

@app.post("/empdepartments/", response_model=schemas.EmpDepartment)
def create_empdepartment(empdepartment: schemas.EmpDepartmentCreate, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.create_empdepartment(db, empdepartment)

@app.get("/empdepartments/", response_model=list[schemas.EmpDepartment])
def read_empdepartments(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_user)):
    return crud.get_empdepartments(db, skip=skip, limit=limit)

@app.delete("/empdepartments/{empdepartment_id}")
def delete_empdepartment(empdepartment_id: int, db: Session = Depends(dependencies.get_db), current_user: models.Employee = Depends(auth.get_current_active_admin)):
    return crud.delete_empdepartment(db, empdepartment_id)
