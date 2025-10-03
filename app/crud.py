from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    hashed_password = auth.get_password_hash(employee.password)
    db_employee = models.Employee(name=employee.name, email=employee.email, role=employee.role, hashed_password=hashed_password)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeBase):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db_employee.role = employee.role
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()

def update_department(db: Session, department_id: int, department: schemas.DepartmentBase):
    db_department = get_department(db, department_id)
    if db_department:
        db_department.name = department.name
        db.commit()
        db.refresh(db_department)
    return db_department

def delete_department(db: Session, department_id: int):
    db_department = get_department(db, department_id)
    if db_department:
        db.delete(db_department)
        db.commit()
    return db_department

def create_empdepartment(db: Session, empdepartment: schemas.EmpDepartmentCreate):
    db_empdepartment = models.EmpDepartment(employee_id=empdepartment.employee_id, department_id=empdepartment.department_id)
    db.add(db_empdepartment)
    db.commit()
    db.refresh(db_empdepartment)
    return db_empdepartment

def get_empdepartment(db: Session, empdepartment_id: int):
    return db.query(models.EmpDepartment).filter(models.EmpDepartment.id == empdepartment_id).first()

def get_empdepartments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EmpDepartment).offset(skip).limit(limit).all()

def delete_empdepartment(db: Session, empdepartment_id: int):
    db_empdepartment = get_empdepartment(db, empdepartment_id)
    if db_empdepartment:
        db.delete(db_empdepartment)
        db.commit()
    return db_empdepartment
