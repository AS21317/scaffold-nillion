from nillion_nada import *

def nillion_nada_calculation():
    # Define parties
    party1 = Party(name="Party1")

    # Define inputs
    num1 = SecretInteger(Input(name="num1", party=party1))
    num2 = SecretInteger(Input(name="num2", party=party1))

    # Perform calculations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    division_result = num1 / num2

    # Return outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(product_result, "product_output", party1),
        Output(division_result, "division_output", party1)
    ]
