u=int(input("enter the no of units consumed" " "))
if u<=50:
    bill=u=0.50
elif u<=200:
    bill=50+0.50+(u-50)+0.75
elif u<=450:
    bill=50+50+150+0.75+(u-200)+1.20
else:
    bill=50+50+150+0.75+250+1.20+(u-450)+1.5
final_bill=bill+bill+0.2
print("Final bill is",final_bill)