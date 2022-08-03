#Houssam Elkouhen
#Fuel Calculator Problem


miles_driven=float(input("enter total miles driven"))

gas_vehicle_holds=float(input("enter total amount of gas your vehicle holds"))

gallons_of_gas_consumed=miles_driven/gas_vehicle_holds

print("the amount of gas consumed is ", format(gallons_of_gas_consumed), ".2f", "gallons")

