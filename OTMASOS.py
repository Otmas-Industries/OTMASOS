#this line sets up the while loop
goAgain = "y"
#these lines give a little backround
print (" Hello, welcome to OtmasOS 2.0.0.")
print ("Unfortunately, we are in Alpha development right now, so you cannot access the")
print ("internet, and the developers have not said they will add that capability.")
print ("type info for more information")
#this adds a little security but not much since everyon can see it
print ("in order to continue, please enter your username")
user_name = input (" username:")
if user_name == ("Otmas") :
    print ("Welcome, Otmas creator of us all")
elif user_name == ("Owen M.") :
    print ("welcome owen.")
elif user_name == ("Zach") :
    print ("Welcome Zach, friend of Otmas")
else :
    print ("STOP HACKING YOU BIG BOZO")
    #since the while loop uses variables to control itself, this breaks the loop and exits the program
    goAgain = "n"
    while goAgain == "n" :
        exit
#security clearance will have a use later in development, but right now, it just looks professional.
print ("Please Enter your password")
passWord = input("password:")
if passWord == ("Otmas64134@@") :
    print ("Access granted, Security Clearance: 10")
elif passWord == ("macofish") :
    print ("Access granted, Security Clearance: 8")
elif passWord == ("zachpixils") :
    print ("Access Granted, Security Clearance: 9")
else :
    print ("Access Denied. You have been locked out of the facility for 48 hours")
    goAgain = "n"
    while goAgain == "n" :
        exit
while goAgain == "y":      
    print (" the different options are: Shutdown, Launch a nuke, DEATH, and info")
    user_response = input("what would you like to do today?")
    if user_response == "DEATH" :
            print (" YOU WILL DIE NOW!")
            exit
    elif user_response == ("Do My Homework") :
            print ("This is a WIP")
    elif user_response == ("info") :
            print ("This is a fake OS developed by Otmas with help from Macfisherman")
    elif user_response == (" WHERE THE HECK IS OWEN???") :
            print ("He is in the bathroom")
    elif user_response == ("Launch a nuke") :
        nuke_location = input ("Where would you like to nuke?")
        print ("%s got nuked" %nuke_location)
    elif user_response == ("Set TARDIS Co-ords") :
        tardis_timePlace = input ("Where would you like to go?")
        print ("Welcome to %s" %tardis_timePlace)
    elif user_response == ("Make an Appointment") :
        print ("this is WIP")
    elif user_response == ("Shutdown") :
        goAgain = ("n")
        break
    goAgain = input ("Press Y to continue, or any other letter to exit")

    
exit
