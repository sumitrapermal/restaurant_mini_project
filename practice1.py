menu={
    "pasta":100,
    "maggie":50,
    "poha":40,
    "tea":10,
    "coffe":20
}
print("welcome to The Morning Dish Restaurant!")
print("pasta: Rs.100\nmaggie: Rs.50\npoha: Rs.40\nTea: Rs.10\ncoffee: Rs.20 ")
order_total=0
item_1=input("please order something:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} is added.")
else:
    print(f"this item {item_1} is not available !")
another_order= input("Do you want order again?(yes/no):")
if another_order =="yes":
    item_2=input("please order something:")
    if item_2 in menu:
        order_total+=menu[item_2]
    else:
        print(f"your item {item_2} is not availabel !")
print(f"your Bill amount is {order_total}.\nTHANK YOU ")
