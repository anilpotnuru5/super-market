print("***WELCOME TO ANIL SUPER MARKET***\n")
print("___ITEMS LIST___\n")
print("1.SHAMPOO      -20/-\n2.SOAP         -50/-\n3.PICKELS      -80/-\n4.CHOCOLATE    -120/-\n5.CHIPS        -40/-\n6.COOL DRINKS  -100/-\n7.ICE CREAM    -40/-\n"
     +" 8.PERFUMES     -170/-\n9.BISCKETS     -40/-\n10.BOOKS       -150-/-\n11.OIL         -70/-\n12.DRY FRUITS  -200/-\n13.EXIT        -0/-\n")
bill=0
cart={}
list1=[]
a=True
while (a):
    x=int(input("Select The Items:"))
    if x==1:
        y=int(input("Select The Quantity:"))
        print("SHAMPOO Is Added To Your Bill")
        cart.update({"SHAMPOO":20})
        bill+=y*20
        list1.append(y)
    elif x==2:
        y=int(input("Select The Quantity:"))
        print("SOAP Is Added To Your Bill")
        cart.update({"SOAP":50})
        bill+=y*50
        list1.append(y)
    elif x==3:
        y=int(input("Select The Quantity:"))
        print("PICKELS Is Added To Your Bill")
        cart.update({"PICKELS":80})
        bill+=y*80
        list1.append(y)
    elif x==4:
        y=int(input("Select The Quantity:"))
        print("CHOCOLATE Is Added To Your Bill")
        cart.update({"CHOCOLATE":120})
        bill+=y*120
        list1.append(y)
    elif x==5:
        y=int(input("Select The Quantity:"))
        print("CHIPS Is Added To Your Bill")
        cart.update({"CHIPS":40})
        bill+=y*40
        list1.append(y)
    elif x==6:
        y=int(input("Select The Quantity:"))
        print("COOL DRINKS Is Added To Your Bill")
        cart.update({"COOL DRINKS":100})
        bill+=y*100
        list1.append(y)
    elif x==7:
        y=int(input("Select The Quantity:"))
        print("ICE CREAM Is Added To Your Bill")
        cart.update({"ICE CREAM":40})
        bill+=y*40
        list1.append(y)
    elif x==8:
        y=int(input("Select The Quantity:"))
        print("PERFUMES Is Added To Your Bill")
        cart.update({"PERFUMES":170})
        bill+=y*170
        list1.append(y)
    elif x==9:
        y=int(input("Select The Quantity:"))
        print("BISCKETS Is Added To Your Bill")
        cart.update({"BISCKETS":40})
        bill+=y*40
        list1.append(y)
    elif x==10:
        y=int(input("Select The Quantity:"))
        print("BOOKS Is Added To Your Bill")
        cart.update({"BOOKS":150})
        bill+=y*150
        list1.append(y)
    elif x==11:
        y=int(input("Select The Quantity:"))
        print("OIL Is Added To Your Bill")
        cart.update({"OIL":70})
        bill+=y*70
        list1.append(y)
    elif x==12:
        y=int(input("Select The Quantity:"))
        print("DRY FRUITS Is Added To Your Bill")
        cart.update({"DRY FRUITS":200})
        bill+=y*200
        list1.append(y)
    elif x==13:
        print("__Calculated Your Bill__\n")
        a=False
    else:
        print("Select The Correct Item:")
x=0
for i,j in cart.items():
    print(f"{i}     -{j}/-   ={list1[x]}")
    x+=1
print(f"\nYour Total Bill Is :{bill}")
print("Thanking You Visiting Again.....")
import matplotlib.pyplot as plt
p=(cart.keys())
q=(cart.values())
plt.pie(q,labels=p,autopct="%1.1f%%")
plt.legend(title="Your Items")
plt.title("YOUR BILL STATICS")
plt.show()