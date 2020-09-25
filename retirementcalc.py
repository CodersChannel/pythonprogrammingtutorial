# 'import' is used so that one module gains access to the code that present in another module
import datetime # 'datetime' is a module to access dates and times.

def retirementcalc():
    age = int(input("what is your current age? "))
    retireyear = int(input("At what age would you like to retire? "))
    yearleft=retireyear-age
    if yearleft<0:
        print('user already retired')
    else:
        print('you have %s years left until you can retire'%(yearleft))
        now = datetime.datetime.now() # creates a datetime.datetime instance with the current local date and time.
        print("It's %s, so you can retire in %s."%(now.year,now.year+yearleft))

retirementcalc()
