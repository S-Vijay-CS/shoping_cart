import sqlite3

db=sqlite3.connect('shoping_cart.db')
db1=db.cursor()

# Product_DB table create 
"""
t=''' create table product(
prod_name varchar,
qty integer,
price integer);'''
db1.execute(t)
print('Product Table Created')
"""

#Customer_DB table create
"""
c='''create table customer(
cus_name varchar,
cus_phone integer,
cus_adderss varchar)'''
db1.execute(c)
print('Customer Table Created')
"""

#Admin  table
"""
c='''create table admin(
username varchar,
password varchar)'''
db1.execute(c)
print('Admin Table Created')
"""
#cusomer Column Name update
"""
c='''alter table customer rename column cus_adderss to cus_address''';
db1.execute(c)
print('sucess')
"""

#customer_cart Table create
"""
cc='''create table cus_cart(
prod varchar,
qty integer);'''
db1.execute(cc)
print('Customer Cart Table Created')
"""

#DELETE 
"""
db1.execute('''delete from product''')
db.commit()
"""
class e_shop:
    shop_name='VIJAY E-COMM'
    location='chennai'
    phone_no=7639936769

    def __init__(self,prod_name,qty, price):
        self.prod_name=prod_name
        self.qt=qty
        self.price=price


    def admin(cls):
        print('---------------------------------------------')
        print(' #####     L O G I N - P A G E     #####')
        print('---------------------------------------------',end='\n\n')
        user_name=input('ENTER USER NAME :')
        db1.execute('SELECT username from admin where username=?',(user_name,))
        result=db1.fetchone()
        if result:
            password=input("Enter Your Password :")
            db1.execute('SELECT password from admin where username=? and password=?',(user_name,password))
            result=db1.fetchone()
            if result:
                    print('---------------------------------------------')
                    print(' #####     W E L C O M E     #####')
                    print('---------------------------------------------',end='\n\n')
                    while True:
                        print('Change Shop Details  : PRESS 1')
                        print('ADD PRODUCTS         : PRESS 2')
                        print('REMOVE PRODUCTS      : PRESS 3')
                        print('EXIT                 : PRESS 4 ')
                        num=int(input('ENTER YOUR CHOICE : '))
                        if num==1:
                            a=input('ENter Your Shop Name:')
                            b=input('Enter Your Shop Location :')
                            c=input('Enter Your Phone Number  :',end='\n')
                            e_shop.shop_name=a
                            e_shop.location=b
                            e_shop.phone_no=c
                            print('SHOP DETAILS UPDATED !!!...',end='\n\n')
                        elif num==2:
                            print(end='\n\n')
                            e_shop.add_prod(input('Enter The Prod Name :').upper(),input('Enter The Qty :'),input('Enter Price :'))
                        elif num==3:
                            print(end='\n\n')
                            e_shop.remove_prod(input('Enter The Product Name : ').upper())
                        elif  num==4:
                            print('---------------------------------------------------',end='\n\n')
                            break

            else:
                print('Password Not Match',end='\n\n')
        else:
            print('Wrong Username ',end='\n\n')
            
                
        
    @classmethod
    def shop_display(cls):

        print('------------------------------------------------------')
        print("Shop Name :",  cls.shop_name)
        print("Location :", cls.location)
        print("Phone No :", cls.phone_no)
        print('------------------------------------------------------',end='\n\n')

    def admin_user(cls):
        pass

    def add_prod(prod_name,qty, price):
        db1.execute('''insert into product (prod_name,qty,price) values(?,?,?)''',(prod_name,qty,price))
        db.commit()
        print('Product Succesfully Added !',end='\n\n')
        a=input('Do You Want Other Product : ( Y / N )')
        if a=='Y' or a== 'y':
            print(end='\n\n')
            e_shop.add_prod(input('Enter The Prod Name :').upper(),input('Enter The Qty :'),input('Enter Price :'))
        elif a =='N' or a=='n':
            pass
            
    def add_cart_prod(prod,qty):
        db1.execute('''insert into cus_cart (prod,qty) values(?,?)''',(prod,qty))
        db.commit()
        print('Product Succesfully Added !',end='\n\n')
    def remove_prod(prod_name):
        db1.execute('''select Prod_name from product where prod_name =? ''',(prod_name,))
        result=db1.fetchone()
        if result:
            db1.execute('''DELETE from product where prod_name=?;''',(prod_name,))
            db.commit()
            print('Product Removed  Successfully !!!!...',end='\n\n')
        else:
            print('This Product Not Available In This Store',end='\n\n')
    def prod_list(cls):
        out='''select * from product;'''
        display=db1.execute(out)
        print('------------------------------------------------------')
        print('Name , qty, Price')
        for i in display:
            print(i[0],i[1],i[2])
        print('------------------------------------------------------')
        print(end='\n\n')
            

        
    def customer_details(cus_name,cus_phone,cus_address):
        db1.execute('''insert into customer(cus_name,cus_phone,cus_address) values(?,?,?)''',(cus_name,cus_phone,cus_address))
        db.commit()
        print('Customer Details Add Succesfully !',end='\n\n')
        
    def cus_display(cls):
        print('------------------------------------------------------',end='\n\n')
        display=db1.execute('''select * from customer;''')
        for i in display:
            print('CUSTOMER NAME  : ',i[0])
            print('PHONE NUMBER   : ',i[1])
            print('ADDRESS        : ',i[2])
        cart_display=db1.execute('''select * from cus_cart;''')
        print('Produt  ,  Qty')
        if list(cart_display)!=[]:
            display=db1.execute('''select * from cus_cart;''')
            for i in display:
                print(i)
        else:
            print('Your Card Is Empty')
        print('------------------------------------------------------',end='\n\n')

    def add_cart(cls):
        prod_name= input("Enter The Product Name : ").upper()
        db1.execute('''select Prod_name from product where prod_name =? ''',(prod_name,))
        result=db1.fetchone()
        if result:
            prod_qty=int(input("Enter The Product Qty :"))
            db1.execute('''select qty from product where prod_name =? AND qty >=? ''',(prod_name,prod_qty))
            result=db1.fetchone()
            if result:
                db1.execute('''select prod from cus_cart where prod =? ''',(prod_name,))
                result=db1.fetchone()
                if result:
                    db1.execute('''UPDATE product SET qty=qty-? where prod_name=?''',(prod_qty,prod_name))
                    db1.execute('''UPDATE cus_cart SET qty=qty+? where prod=?''',(prod_qty,prod_name))
                    db.commit()
                    print('Product Updated!',end='\n\n')
                else:
                    db1.execute('''UPDATE product SET qty=qty-? where prod_name=?''',(prod_qty,prod_name))
                    db.commit()
                    e_shop.add_cart_prod(prod_name,prod_qty)
                    
            else:
                print('Stock Not Available',end='\n\n')
            
        else:
            print(f'{prod_name}This Product Not Avilable',end='\n\n')

    def remove_cart(cls):
        cart_display=db1.execute('''select * from cus_cart;''')
        if list(cart_display)!=[]:
            prod_name=input("Enter Product Name : ").upper()
            db1.execute('''select Prod from cus_cart where prod =? ''',(prod_name,))
            result=db1.fetchone()
            if result:
                prod_qty=int(input("Enter The Product Qty :"))
                db1.execute('''select qty from cus_cart where prod =? AND qty >=? ''',(prod_name,prod_qty))
                result=db1.fetchone()
                if prod_qty==0:
                    display=db1.execute('''select qty from cus_cart WHERE prod=?;''',(prod_name,))
                    bal=((list(display)[0][0])-prod_qty)
                    db1.execute('''UPDATE product SET qty=qty+? where prod_name=?''',(bal,prod_name))
                    db1.execute('''DELETE from cus_cart where prod=?;''',(prod_name,))
                    db.commit()
                    print('Product Removed Successfully!!!...',end='\n\n')
                    
                elif result:
                    display=db1.execute('''select qty from cus_cart WHERE prod=?;''',(prod_name,))
                    bal=((list(display)[0][0])-prod_qty)
                    db1.execute('''UPDATE product SET qty=qty+?''',(bal,))
                    db1.execute('''UPDATE cus_cart SET qty=? WHERE prod=?''',(prod_qty,prod_name))
                    db.commit()
                    print('Quantity Removed Successfully!!!!',end='\n\n')
                    
                    
                else:
                    print("Can't remove, ",end='\n\n')
                
            else:
                print('This Product Is Not Available In this Cart',end='\n\n')
            
 
        else:
            print('Your Card Is Empty',end='\n\n')
        



            
while True:
    print('ADMIN USER        : press 1')
    print("SHOP_DETAILS      : press 2")
    print("PRODUCT_DETAILS   : press 3")
    print("CUSTOMER_DETAILS  : press 4") 
    print("ADD_PROD To CART  : press 5")
    print("REMOVE_CART PROD  : Press 6")
    print("EXIT              : press 7 ",end='\n')
    number=int(input("Enter The Number :- "))
    if number==1:
        print(end='\n\n')
        e_shop.admin(0)
    elif number==2:
        print(end='\n\n')
        e_shop.shop_display()
    elif number==3:
        print(end='\n\n')
        e_shop.prod_list(0)
    elif number==4:
        print(end='\n\n')
        e_shop.cus_display(0)
    elif number==5:
        print(end='\n\n')
        e_shop.add_cart(0)
    elif number==6:
        print(end='\n\n')
        e_shop.remove_cart(0)
    elif number==7:
        break
    
    
