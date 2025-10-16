'''
Ask the user is_raining and have_umbrella (True/False). Print "Go" only if
is_raining is True and have_umbrella is True; otherwise print "Stay".
'''

rain = input("Is it raining? (y/n) ")
umb = input("Do you have an Umbrella? (y/n) ")

if rain == "y":
    rain = True
else:
    rain = False
if umb == "y":
    umb = True
else:
    umb = False

if umb == True and rain == True:
    print("GO!")
else:
    print("Stay :( please I need you")