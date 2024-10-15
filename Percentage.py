def myfunction(bill_amnt, tip_percentage):
    total=(bill_amnt* (1+0.01 *tip_percentage))

    total= round(total,2)

    print("total Bill amount is:", total)

myfunction(500,60)
