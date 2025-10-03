from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, default="user")
    hashed_password = Column(String)
    departments = relationship("EmpDepartment", back_populates="employee")

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    employees = relationship("EmpDepartment", back_populates="department")

class EmpDepartment(Base):
    __tablename__ = "empdepartment"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    department_id = Column(Integer, ForeignKey("department.id"))
    employee = relationship("Employee", back_populates="departments")
    department = relationship("Department", back_populates="employees")
