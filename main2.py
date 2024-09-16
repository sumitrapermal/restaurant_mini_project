menu={
    "regular momos":100,
    "fry momos":150,
    "cheese momos":200,
    "paneer momos":250,
    "fry cheese momos":250,
    "regular frankie":50,
    "cheese frankie ":100,
    "paneer frankie":200,
    "sandwich":60,
    "toast sandwich":80,
    "cheese sandwich":100
    }
print("Welcome To Tasty Tableaux Restaurant ")
print("regular momos : RS100 \nfry momos : RS150\ncheese momos : RS200\npaneer momos: RS250 \nfry cheese momos : RS250 \nregular frankie :RS50 \ncheese frankie :RS100 \npaneer frankie :RS200\nsandwich :RSS60 \ntoast sandwich :RS80 \ncheese sandwich:RS100")
get_order=input("please order something :")
if get_order in menu:
    order_total=0
    order_total+=menu[get_order]
    print(f"your item {get_order} is added")
else:
    print(f"your item {get_order} is not available")
order_again=input("Do you want order again ?(yes/no):")
while order_again=="yes":
        get_order2=input("please order something :")
        if get_order2 in menu:
            order_total+=menu[get_order2]
            print(f"your item {get_order2} is added")
            order_again=input("Do you want order again?(yes/no) :")
        else:
            print(f"your item {get_order2} is not available")
print(f"your total Bill is {order_total}\n THANKYOU")



