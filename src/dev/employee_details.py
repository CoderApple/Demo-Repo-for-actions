
employees=[]
def add_employee(name,age,position):
    details={"name": name, "age": age, "position": position}
    employees.append(details)
    return f"{name} details Sucessfully added to the list"

def view_employee(name):
    if not employees:
        return "No employee details added"
    for detail in employees:
        if detail["name"]==name:
            return detail

def delete_employee(name):
    for detail in employees:
        if detail["name"]==name:
            employees.remove(detail)
        return f"{name} details removed from the list"

