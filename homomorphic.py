import tenseal as ts


def setup_context():
    poly_modulus_degree = 2048  
    plain_modulus = 1032193    
    context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree, plain_modulus)
    
    context.generate_relin_keys()
    return context

context = setup_context()

number1 = 75
number2 = 326

enc_number1 = ts.bfv_scalar(context, number1)
enc_number2 = ts.bfv_scalar(context, number2)

enc_result = enc_number1 + enc_number2

result = enc_result.decrypt()

print(f"De som van {number1} en {number2} is: {result}")
