from ..dev.employee_details import employees, view_employee, add_employee, delete_employee



def test_empty_employee_list():
    name="Charan"
    if len(employees)==0:
        result=view_employee(name)
        assert result =="No employee details added"


def test_add_employees():
    name= "Charan"
    age = 21
    position = "DE"
    result =add_employee(name,age,position)
    assert result == f"{name} details Sucessfully added to the list"


def test_view_employees():
    name="Charan"
    result= view_employee(name)
    assert result == {'name': 'Charan', 'age': 21, 'position': 'DE'}

def test_delete_employees():
    name = "Charan"
    result = delete_employee(name)
    assert result==f"{name} details removed from the list"



