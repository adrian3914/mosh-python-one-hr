weight = float(input("Weight: "))
unit_of_measurement = input("(K)g or (L)bs: ").upper()

if unit_of_measurement == "K":
    weight = weight * 2.20462
    print("Weight in LB: " + str(round(weight, 2)))
elif unit_of_measurement == "L":
    weight = weight / 2.20462
    print("Weight in Kg: " + str(round(weight, 2)))
else:
    print("Invalid, Enter either l, L for pounds or k, K for kilograms.")
