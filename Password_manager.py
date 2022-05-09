class BasePasswordManager:
    old_passwords=['11111','22222','Nivash@25']
    def __init__(self):
        pass
    def get_password(self):
        return self.old_passwords[-1]
    def is_correct(self):
        enter_pass=input("Enter the password to check : ")
        if self.old_passwords[-1]==enter_pass:
            return True
        else:
            return False
            
class PasswordManager(BasePasswordManager):
    def set_password(self,new_password):
        self.new_password=new_password
        if self.new_password.strip()=='':
            print("Invalid password (all characters are null)")
            return 0
        elif len(self.new_password)>=6 and p.get_level(self.new_password)>=p.get_level(p.old_passwords[-1]):
            p.old_passwords.append(self.new_password)
            print("Password changed successfully")
            return 1
        elif len(self.new_password)<6:
            print("Password should be more than 6 characters")
            return 0
        elif p.get_level(self.new_password)<p.get_level(p.old_passwords[-1]):
            print("The level of new password is less than old password\nTo increase level password should contain\nalphanumeric and special characters")
            return 0
        



    def get_level(self,last_pass):
        self.last_pass=last_pass
        if self.last_pass.isalpha() or self.last_pass.isnumeric():
            return 0
        elif self.last_pass.isalnum():
            return 1
        else:
            return 2


def start(option):
    if option=='1':
        print('Old passwords : ',p.old_passwords)
    elif option=='2':
        print('Current password : ',p.get_password())
    elif option=='3':
        check_pass=p.is_correct()
        if check_pass==True:
            print("Entered password is correct")
        else:
            print("Entered password is wrong. Please check!"),
    elif option=='4':
        new_password=input("Enter new password : ")
        if p.set_password(new_password)==1:
            level=p.get_level(new_password)
            print("Security level of new password : level {}".format(level)),
    elif option=='5':
        level=p.get_level(p.old_passwords[-1])
        print("Security level of current password : level {}".format(level))
    elif option not in ['1','2','3','4','5','6']:
        print("Invalid option. Please check!")
        
        
p = PasswordManager()
print("\n_________________PASSWORD MANAGER_________________\n")
repeat=True
while repeat:
    print('')
    print("\n\n1.List all the old passwords\n2.Get the current password\n3.Enter the current password and check\n4.Set new password\n5.Get the level of password\n6.Exit\n")
    print('____________________________________\n______________OUTPUT_________________')
    option=input("Enter the number to perform the operation : ")
    start(option)
    if option=='6':
        choose=input('Are you sure you want to exit (Yes/No)? : ')
        if choose=='Yes' or choose=='yes':
            print("\n___________________Exit successful!_______________\n")
            repeat=False
        else:
            repeat=True


        
