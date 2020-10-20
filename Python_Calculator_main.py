import math
print(" ")
print(" Welcome to Cores ``Advanced_Calculator.exe`` ")
print(" ")
print("---")
print("---")
print("---")
print(" ")
print(" Please write down your calculation and press ``ENTER`` ")
print(" ")
while 1:
    x = input(">>>  ")          
    if x == 'exit':
        print(" thank you for using ``Advanced_Calculator.exe`` ")
        print(" do you really want to shut down the application? ")
        y = input("  <>-<>  ")
        if y == 'yes':
            break
   
    if x == 'panzer':
        print("verdank Cobra dass es das hier gibt")           
        print("")
        print("░░░░░░███████ ]▄▄▄▄▄▄▄▄▃")
        print("▂▄▅█████████▅▄▃▂")
        print("I███████████████████].")
        print("◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..")

    if x == 'Mathemann':
        timer = 1
        while 2:
            print("hdf?")
            timer = timer + 1
            if timer == 9999:
                print("ok reicht")
                exit()            
    try:
        Mathe = eval(x)
        if Mathe: print(Mathe)
    except:
        try:
            eval('math.'+x)
        except:
            try:
                exec(x)
            except Exception as e:
                if x == "panzer":
                    round
                else:
                    print("I don`t think this is what you expected... anyway: ", e)

