import random
import time
import os
has_hacked = False
def htool():
   phrases = ["[+] Enumerating the database..", "[+] Cracking passwords..", "[+] Attacking the firewall..", "CRIT ERROR! Firewall has been activated, evasion tactics initiated!", "Firewall has been bypassed!", "[+] Attacking the mainframe..", "[+] Infiltrating the server...", "SUCCESS! Server has been compromised"]

   print("Welcome to Hack Tool v3.96")
   print("(The author is not responsible for any damage inflicted or caused by this tool. By using this tool, you understand the underlying risks and consequences. USE CAREFULLY AND WITH CAUTION)")
   global company
   company = str(input("Enter the company you would like to hack (EXACT NAME NO SPACES): "))

   for phrase in phrases:
      delay = random.randint(3, 8)
      time.sleep(delay)
      print(phrase)


   print("SSH connection activated")
   print("------------------------------")
   print("* This system is for the use of authorized users only. Usage of\n* this system may be monitored and recorded by system personnel.\n* Anyone using this system expressly consents to such monitoring\n* and is advised that if such monitoring reveals possible evidence of criminal activity, system personnel may provide the\n* evidence from such monitoring to law enforcement officials.")
   print("-------------------------------\n")

   print("Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 6.2.0-33-generic ×86_64)\n* Documentation:\n* Management: https://help.ubuntu.com/ https://landscape.canonical.com/n* Support: https://ubuntu.com/advantage/nYour commands are being recorded.\nYou have mail\nLast login: Thu February 28 16:36:09 2024 from 2.43.73.120\n")

   print("Available commands: ls, cat, cd, exit, ")
   has_hacked = True

   while True:
      
      command = input(str(company).capitalize()+"Administrator@"+str(company).upper()+":~$  ")
      if command == "ls":
         print("Documents  secrets.txt   todo.txt")
      elif command == "clear":
         os.system("cls")
      elif command == "cat" or command == "cd":
         print("Error: Expected 1 argument")
      elif command == "ls -la" or command == "ls -al":
         print("Documents  secrets.txt  todo.txt  key.txt")
      elif command == "cat todo.txt":
         print("- Decrease employee salary\n- Fifth round of lay offs\n- Install Apache\n- Fix vulnreableities")
      elif command == "cat key.txt":
         print("google")
      elif command == "cat secrets.txt":
         print("Permission denied: CEO+")
      elif command == "":
         continue
      elif command == "cd ..":
         while True:
            userand = input(company+"Administrator@"+company.upper()+":/Users$  ")
            if userand == "ls":
               print(f"{company.title()}Administrator   {company.title()}Database")
            elif userand == f"cd {company.title()}Administrator":
               break
            elif userand == f"cd {company.title()}Database":
               gdb = input("Enter password: ")
               if gdb == "ifyoufoundthisthengoodjob":
                  print("Access granted")
                  while True:
                     gdbmand = input(company+"Database@"+company.upper()+":/~$  ")
                     if gdbmand == "cd ..":
                        break
                     elif gdbmand == "ls":
                        print("Documents")
                     elif gdbmand == "cd Documents":
                        while True:
                           gdbdoc = input(company+"Database@"+company.upper()+":/Documents$  ")
                           if gdbdoc == "ls":
                              print("Customer_information.txt   Data_collecting_software")
                           elif gdbdoc == "cat Customer_information.txt":
                              print("jimmy: Customer# 145, Male, Dentist, Unmarried. Google account password: Gaius's son said: dkshkjczezpdeopwgaukq (Encrypted)")
                              print("rory231: Customer# 299, Female, Senior Software Engineer at Google, Married. Google account password: ilikecats123")
                              print("bob: Customer# 150, Male, Dentist, Unmarried. Favorite dressing: Vigenerette. Google account password: nofjesifoivtgggczvj1234 (Encrypted)    Additional Notes: \"I left my key in a hidden file called key.txt\" ")
                           elif gdbdoc == "cd ..":
                              break
               else:
                  print("Access denied")
                  
               
      elif command == "cd Documents":
         while True:
            docmand = input(company+"Administrator@"+company.upper()+":/Documents$  ")

            if docmand == "cd ..":
               break
            elif docmand == "ls":
               print("2025_plans.txt   DBpass.txt")
            elif docmand == "cat 2025_plans.txt":
               print("World Domination")
            elif docmand == "cat Data_collecting_software":
               print("Is not a text file")
            elif docmand == "cat DBpass.txt":
               print("Permission denied.")
            elif docmand == "sudo cat DBpass.txt":
               print("In the square of 8, the cube of 4, entrust the base with the door.\naWZ5b3Vmb3VuZHRoaXN0aGVuZ29vZGpvYg==")
            
            else:
               print("Invalid command/invalid filename/too many or too less arguments.")
         
         
      elif command == "exit":
         print("Exiting SSH connection..")
         start()
         
      else:
         print("Invalid command")
      


def login():
   set_python_enviroment1 = "howlongdi"
   set_python_enviroment2 = "dthistakeyou"
   set_python_enviroment3 = "hardtocrack"
   set_python_enviroment4 = "password123"

   exclone = set_python_enviroment1+set_python_enviroment2
   inclone = set_python_enviroment3+set_python_enviroment4

   while True:
      username = input("Enter username: ")
      password = input("Enter password: ")
      if username == "bob" and password == inclone:
         print("Access granted")
         while True:
               comm = input("bob@GOOGLE:~$   ")
               if comm == "ls":
                  print("Documents  flag.txt")
               elif comm == "exit":
                  print("Exiting..")
                  start()
               elif comm == "cat flag.txt":
                  print("Second part of the flag: HGSKJHhguy739agh37ydghYIF7G37Y. Good job")
               elif comm == "cd Documents":
                  while True:
                     docomm = input("bob@GOOGLE:/Documents$   ")
                     if docomm == "ls":
                           print("Dentistry_notes.txt")
                     elif docomm == "cat Dentistry_notes.txt":
                           print("The terminal edge of gingiva (gums) that surrounds the teeth is known as the gingival margin (marginal gingiva). Roughly half of individuals have a gingival margin that is demarcated from the adjacent gingiva by a shallow linear depression (free gingival groove).")
                     elif docomm == "cd ..":
                           break
               elif comm == "cd ..":
                  while True:
                     usercommand = input("bob@GOOGLE:/Users$   ")
                     if usercommand == "ls":
                           print("bob")
                     elif usercommand == "cd bob":
                           break
                     elif usercommand == "cd ..":
                           while True:
                              homecommand = input("bob@GOOGLE:/home$   ")
                              if homecommand == "ls":
                                 print("Users")
                              elif homecommand == "cd Users":
                                 break
                              elif homecommand == "cd ..":
                                 while True:
                                       rootcommand = input("bob@GOOGLE:/$   ")
                                       if rootcommand == "ls":
                                          print("bin   dev   etc   home   opt   mnt   root   tmp   usr")
                                       elif rootcommand == "cd home":
                                          break
                                       elif rootcommand == "cd root":
                                          print("Permission denied")

                                       
                                       elif rootcommand == "sudo cd root":
                                          passw = input("Sudo Password: ")
                                          if passw == "toor":
                                             while True:
                                                   root = input("bob@GOOGLE:/root$   ")
                                                   if root == "ls":
                                                      print("flag.txt")
                                                   elif root == "cd ..":
                                                      break
                                                   elif root == "cat flag.txt":
                                                      print("This is the third part of the flag: HDGghidhdhsyskFGD783Htyd73gw")
                                          else:
                                             print("Incorrect password. This incident will be recorded!")


                                 
               elif comm == "":
                  continue
               else:
                  print("Invalid command")

      elif username == "jimmy" and password == exclone:
         print("Access granted")
         while True:
               command = input("jimmy@GOOGLE:~$  ")
               if command == "ls":
                  print("Documents  flag.txt")
               elif command == "exit":
                  print("Exiting..")
                  start()
                  
               elif command == "cat" or command == "cd":
                  print("Error: Expected 1 argument")
               elif command == "cat flag.txt":
                  print("Congrats! You have found the first part of the flag: GKSHghGHGhkh7782shjkay7i3. The final flag is the concatenation of 2 flags from Jimmy's account and 2 flags from Bob's account. Gain access to the other account. Good luck")
               elif command == "cd Documents":
                  while True:
                     docmand = input("jimmy@GOOGLE:/Documents$  ")
                     if docmand == "ls":
                           print("Dentistry_notes.txt   PC_password.txt")
                     elif docmand == "cat Dentistry_notes.txt":
                           print("teeth go brush brush cavity go wa wa")
                     elif docmand == "cat PC_password.txt":
                           print("907352")
                     elif docmand == "cd ..":
                           break
                     else:
                           print("Invalid command")
               elif command == "cd ..":
                  while True:
                     usercommand = input("jimmy@GOOGLE:/Users$   ")
                     if usercommand == "ls":
                           print("jimmy")
                     elif usercommand == "cd bob":
                           break
                     elif usercommand == "cd ..":
                           while True:
                              homecommand = input("jimmy@GOOGLE:/home$   ")
                              if homecommand == "ls":
                                 print("Users")
                              elif homecommand == "cd Users":
                                 break
                              elif homecommand == "cd ..":
                                 while True:
                                       rootcommand = input("jimmy@GOOGLE:/$   ")
                                       if rootcommand == "ls":
                                          print("bin   dev   etc   home   opt   mnt   root   tmp   usr")
                                       elif rootcommand == "cd home":
                                          break
                                       elif rootcommand == "cd tmp":
                                          while True:
                                             tmp = input("jimmy@GOOGLE:/tmp$   ")
                                             if tmp == "ls":
                                                   print("flag.txt")
                                             elif tmp == "cat flag.txt":
                                                   print("This is the final flag: GHGJDSAIUGHgygg82ggGYG8t")
                                             elif tmp == "cd ..":
                                                   break


      elif username == "rory231" and password == "ilikecats123":
         print("Access granted")
         while True:
               rory = input("rory231@GOOGLE:~$   ")
               if rory == "ls":
                  print("Documents")
               elif rory == "exit":
                  print("Exiting..")
                  start()
               elif rory == "cd Documents":
                  while True:
                     rorydoc = input("rory231@GOOGLE:/Documents$   ")
                     if rorydoc == "ls":
                           print("default_creds.txt   note.txt")
                     elif rorydoc == "cd ..":
                           break
                     elif rorydoc == "cat default_creds.txt":
                           print("... ..- -.. --- / -.. . ..-. .- ..- .-.. - / .--. .- ... ... .-- --- .-. -.. / ..-. --- .-. / --. --- --- --. .-.. . / .- -.-. -.-. --- ..- -. - ... ---... / - --- --- .-.")
                     elif rorydoc == "cat note.txt":
                           print("Orange cats are the best")

      else:
         print("Invalid login or password")



flag = "GKSHghGHGhkh7782shjkay7i3HGSKJHhguy739agh37ydghYIF7G37YHDGghidhdhsyskFGD783Htyd73gwGHGJDSAIUGHgygg82ggGYG8t"
def flag_checker():
   while True:
      galf = input("Enter flag: ")
      if galf == flag:
         print("Congratulations! You have found the flag!")
      elif galf == "exit":
          start()
      else:
         print("Not quite..")
   

def start():
   print("Welcome to my puzzle! Try to hack into google, log into the users, and get the final flag! (Say Exit to return back to main menu)")
   print("1. Hack\n2. Login\n3. Check your flag")
   choice = int(input())
   if choice == 1:
      htool()
   elif choice == 2:
      login()
   elif choice == 3:
      flag_checker()
   else:
      print("Choose from 1-3. Try again..")

start()