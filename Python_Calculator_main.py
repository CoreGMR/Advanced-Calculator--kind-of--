print(" ")
print(" Willkommen zu Leons ``Advanced_Taschenrechner.exe`` ")
print(" ")
print("---")
print("---")
print("---")
print(" ")
print(" Bitte geben sie ihre Rechung ein")
print(" ")
while 1:
    x = input(">>>  ")          
    if x == 'exit':
        print(" danke fürs benutzen")
        print(" möchtest du das Programm wirklich schließen?")
        y = input("  <>-<>  ")
        if y == 'ja':
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
         exec(x)
      except Exception as e:
        if x == "panzer":
            round
        else:
            print("SO DUMM IST DOCH NICHT MAL ELIAS... Schau:", e)

