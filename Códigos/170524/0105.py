# first we got maney
# then we take 2000 away because not count, if we still have maney then
# we check if got more than 1000, if more then we take 1000 and multiply that 1000 by 0.08 to get 80 bucks in tax
#
# if we stil got maney we check if we got more than 1500 and if we do we multiply 1500 by 0.18 to get 270 bucks in tax
#
# and then at the fucking end we say we balling because if we still got money left we multiply what is left by 0.28 and that is the total tax money

# so. first we have 5000 bukarooonis
# take 2000 away, got 3000
# take 1000 away, 80 bucks tax, got 2000
# take 1500 away, 80 + 270 bucks tax, got 500
# multiply that 500 by 0.28 and get 80 + 270 + 140 bucks in tax get taxed nerd ( 490 bucks in tax holy moly )

money = float(input("Give me your salary :\n"))
tax = 0.0

if money - 2000 > 0:
    money -= 2000
    if money - 1000 > 0:
        tax += 80
        money -= 1000
        if money - 1500 > 0:
            money -= 1500
            tax += 270
            money *= 0.28
            tax += money
            print("R$ %.2f" % tax)
        else:
            money *= 0.18
            tax += money
            print("R$ %.2f" % tax)
    else:
        money *= 0.08
        print("R$ %.2f" % money)
else:
    print("Insento")
    