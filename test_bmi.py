import Lab2.calculate_bmi as bmi

def test_bmi_normal_weight():

    
    result = bmi.calculate_bmi(1.73,57)
    test = 0

    assert (result == test)

def test_bmi_over_weight():

    result = bmi.calculate_bmi(1.73,80)
    test = 1

    assert (result == 1)

def test_bmi_under_weight():

    result = bmi.calculate_bmi(1.73,40)

    test = -1

    assert(result == test)


