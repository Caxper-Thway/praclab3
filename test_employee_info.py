import employee_info as info

def test_get_employees_by_age_range():

    result = info.get_employees_by_age_range(23,30)
    exResult = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]

    assert (result == exResult)

def test_calc_avg_salary():

    exResult = 301000
    result = info.calculate_average_salary()

    assert (exResult == result)

def test_get_employees_by_dept():

    result = info.get_employees_by_dept("Sales")
    exResult = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    
    assert (result == exResult)