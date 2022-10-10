import pickle
import pyperclip

mass = input("Enter Master Password:")

if(mass == "mass_pw"):
    acc_name = input("Enter app name:")
    with open("saved.pass","br") as res:
        info = pickle.load(res)

        if acc_name in info:
            pyperclip.copy(info[acc_name])
            print("user name & password = ",info[acc_name])
            print("user name & password is Copied")
        else:
            print("Profile not found")
else:
    print("WRONG PASSWORD")
