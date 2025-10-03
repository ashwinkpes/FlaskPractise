from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: Optional[str] = None
    role: str = "user"

class EmployeeCreate(EmployeeBase):
    password: str

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

class EmpDepartmentBase(BaseModel):
    employee_id: int
    department_id: int

class EmpDepartmentCreate(EmpDepartmentBase):
    pass

class EmpDepartment(EmpDepartmentBase):
    id: int
    class Config:
        orm_mode = True
