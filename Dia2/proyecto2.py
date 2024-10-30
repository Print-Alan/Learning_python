user_name = input ("¿Cual es su nombre? ")
user_sold = float(input("¿Cuánto has vendido este mes? "))
user_comition = round(13 * user_sold / 100,2)
print(f"Ok {user_name} este mes ganaste de comisión {user_comition} pesotes")