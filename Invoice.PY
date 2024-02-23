print ("invoice System MacLaine Design Ver 1.0")
#requires valid password for invoice (may be unnecessary but ensures security)
password = input("welcome please insert password")
if password == password.lower():
   print("password incorrect")
   input("please insert password")
   lowerpass = True
   if password == password.__contains__("!@#$%^&*()-_=+(""),./<>?;':"):
       print("cannot contain special charecters")
       input(" please insert password")
   passcontains = True
else :print ("welcome user" )
passgood =True


quantity = input("please insert quantity")
total = 85.99*int(quantity)
tax = input("is invoice tax exempt")
if tax == "yes":
   print  (total)
else:
   print(total*1.08)
