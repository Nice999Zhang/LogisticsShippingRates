#Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the packahe weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilograms: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping Cost:{shipping_cost} USD")
