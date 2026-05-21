import price_info

def test_total_cost_shopping():

    exResult = 46.75
    result = price_info.total_cost_shopping()

    assert (exResult == result)

def test_cost_of_fruit():

    fruit = "apple"
    quantity = 10

    exResult = 12

    result = price_info.cost_of_fruits(fruit, quantity)

    assert (exResult == result)