from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")

    # Define secret integers
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))
    d = SecretInteger(Input(name="d", party=party1))

    # Calculate componendo and dividendo
    numerator = a + b
    denominator = c + d

    result = numerator / denominator

    return [Output(result, "result", party1)]
