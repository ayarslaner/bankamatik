username_list = []
password_list = []     # Certain variables that I use in my program
balance_list = []
username_ticket = 0
transaction_history = []


def fetch_username():  # I use this function to fetch username from text file
    with open("customer_accounts.txt") as f:
        for line in f:
            line1 = line.split("***")
            x = line1[0]
            y = x.split()
            username_from_txt = y[0]
            username_list.append(username_from_txt)


def fetch_password():  # I use this function to fetch user password from text file
    with open("customer_accounts.txt") as f:
        for line in f:
            line1 = line.split("***")
            x = line1[1]
            y = x.split()
            password_from_txt = y[0]
            password_list.append(password_from_txt)


def fetch_balance():  # I use this function to fetch user balance from text file
    with open("customer_accounts.txt") as f:
        for line in f:
            line1 = line.split("***")
            x = line1[2]
            y = x.split()
            balance_from_txt = y[0]
            balance_list.append(balance_from_txt)


fetch_username()
fetch_password()    # These function calls are for fetching user information
fetch_balance()


def login_page():  # main login function
    print """Welcome to Banking Account Management Tool (v. 1.0) \n
    Please log in by providing your user credentials:\n"""
    input_username = raw_input("User Name: ")
    input_password = raw_input("Password: ")
    if input_username in username_list:
        global username_ticket
        username_ticket = username_list.index(input_username)
        if input_password == password_list[username_list.index(input_username)]:
            main_page()
        else:
            print "Your user name and/or password is not correct. Please try again!"
            login_page2()
    else:
        print "Your user name and/or password is not correct. Please try again!"
        login_page2()


def login_page2():  # Second login function if login credentials in first login function does not macth
    input_username = raw_input("User Name: ")
    input_password = raw_input("Password: ")
    if input_username in username_list:
        global username_ticket
        username_ticket = username_list.index(input_username)
        if input_password == password_list[username_list.index(input_username)]:
            main_page()
        else:
            print "Your user name and/or password is not correct. Please try again!"
            login_page2()
    else:
        print "Your user name and/or password is not correct. Please try again!"
        login_page2()


def main_page():  # Main page function that I use for calling other functions according to input
    print "Welcome, " + username_list[username_ticket] + """ Please choose one of the following options
by entering the corresponding menu number.
  1. Check Balance
  2. Transfer Money
  3. Deposit
  4. Withdraw
  5. Close Account
  6. Update Password
  7. See the latest transactions
  8. Admin Menu
  9. Quit"""
    menu_selection = input("Please make your selection: ")
    if menu_selection == 1:
        menu_item1()
    elif menu_selection == 2:
        menu_item2()
    elif menu_selection == 3:
        menu_item3()
    elif menu_selection == 4:
        menu_item4()
    elif menu_selection == 5:
        menu_item5()
    elif menu_selection == 6:
        menu_item6()
    elif menu_selection == 7:
        menu_item7()
    elif menu_selection == 8:
        menu_item8()
    elif menu_selection == 9:
        return ""
    else:
        str(menu_selection) + " is not a valid entry. Please choose from the above menu"
        main_page()


def menu_item1():  # Menu first selection function
    print """===== Check Balance =====
   You have """ + balance_list[username_ticket] + " TL in your account"
    return_to_menu()


def menu_item2():  # Menu second selection function
    recipient_name = raw_input("===== Transfer Money =====\n   Please enter the recipient: ")
    if recipient_name in username_list:
        amount = input("Please enter the amount: ")
        print str(amount) + " TL will be transferred to " + recipient_name + " today"
        approval = raw_input("Do you approve (yes/no?): ")
        if approval == "yes":
            balance_list[username_list.index(recipient_name)] = str(int(balance_list[username_list.
                                                                        index(recipient_name)]) + amount)
            balance_list[username_ticket] = str(int(balance_list[username_ticket]) - amount)
            money_transfer = "Transfer: " + str(amount) + " TL, Recipient: " + recipient_name + ", Balance: " \
                + balance_list[username_ticket] + " TL"
            transaction_history.append(money_transfer)
            print str(amount) + " TL has been transferred to " + recipient_name + "." + \
                " Your current balance is " + balance_list[username_ticket] + " TL"
            return_to_menu()
        elif approval == "no":
            print "Your transfer request has been cancelled."
            return_to_menu()
    else:
        print recipient_name + " is not a valid recipient. Please try again"
        menu_item2()


def menu_item3():  # Menu third selection function
    deposit_amount = input("===== Deposit Money =====\n   Please enter the amount: ")
    balance_list[username_ticket] = str(int(balance_list[username_ticket]) + deposit_amount)
    print str(deposit_amount) + " TL has been deposited to your account. Your current balance is " + balance_list[
        username_ticket] + " TL."
    deposition = "Deposit: " + str(deposit_amount) + " TL, Balance: " + balance_list[username_ticket] + " TL"
    transaction_history.append(deposition)
    return_to_menu()


def menu_item4():  # Menu fourth selection function
    withdraw_amount = input("===== Withdraw Monet =====\n Please enter the amount: ")
    balance_list[username_ticket] = str(int(balance_list[username_ticket]) - withdraw_amount)
    withdrawal = "Withdrawal: " + str(withdraw_amount) + " TL, Balance: " + balance_list[username_ticket] + " TL"
    transaction_history.append(withdrawal)
    print str(withdraw_amount) + " TL has been withdrawn from your account. Your current balance is " + balance_list[
        username_ticket] + " TL."
    return_to_menu()


def menu_item5():  # Menu fifth selection function
    print "===== Close Your Account ====="
    if int(balance_list[username_ticket]) == 0:
        choice = raw_input("Do you approve (yes/no?): ")
        if choice == "yes":
            username_list[username_ticket] = ""
            password_list[username_ticket] = ""
            balance_list[username_ticket] = ""
            print "Your account has been closed now, and your session has ended.\nThanks for being our customer"
        else:
            print "Your account closing request has been canceled"
            return_to_menu()
    else:
        print "Sorry, we cannot close your account at this point, as you still have some balance in your account. " + \
            "You should withdraw this balance before closing your account."
        return_to_menu()


def menu_item6():  # Menu sixth selection function
    print "===== Update Password ====="
    current_password = raw_input("Please enter your current password: ")
    new_password = raw_input("Please enter your new password: ")
    new_password_re_enter = raw_input("Please re-enter your new password: ")
    if current_password == password_list[username_ticket]:
        if new_password != new_password_re_enter:
            print "Sorry, your new password entries do not match! Please try again!"
            menu_item6()
        else:
            print "Your password has been successfully updated."
            return_to_menu()
    else:
        print "Sorry, your current password entry do not match with your current password! Please try again"
        menu_item6()


def menu_item7():  # Menu seventh selection function
    print "===== See the Latest Transactions =====\n   Here, you may view your latest transactions " + \
        "starting from the most recent one."
    n = input("Please enter how many transactions you want to see: ")
    for i in range(n):
        print str(i + 1) + ". " + transaction_history[-(i + 1)]
    return_to_menu()


def menu_item8():  # Menu eight selection function
    print "===== Admin Operations ====="
    admin_username = raw_input("User Name: ")
    admin_password = raw_input("Password: ")
    if admin_username == "admin":
        if admin_password == "abc123":
            admin_main_page()
        else:
            print "Your user name and/or password is not correct. Please try again!"
            menu_item8()
    else:
        print "Your user name and/or password is not correct. Please try again!"
        menu_item8()


def admin_main_page():  # Admin main page function that informs users about their selections
    print """Welcome! Please choose one of the following options by entering the corresponding menu number.
  1. Load Customer Account Data from a File
  2. Create Account
  3. Close Account
  4. Search for an Account
  5. See the stats
  6. Go to the Main Menu"""
    admin_menu_selection = input("Please make your choice: ")
    if admin_menu_selection == 1:
        admin_menu_item1()
    elif admin_menu_selection == 2:
        admin_menu_item2()
    elif admin_menu_selection == 3:
        admin_menu_item3()
    elif admin_menu_selection == 4:
        admin_menu_item4()
    elif admin_menu_selection == 5:
        admin_menu_item5()
    elif admin_menu_selection == 6:
        return_to_menu()
    else:
        print str(admin_menu_selection) + " is not a valid entry. Please choose from the above menu."
        admin_main_page()


def admin_menu_item1():  # Admin menu first selection
    print "===== Admin: Load Customer Account Data =====\nLoading...\nThe account data for " + \
        str(len(username_list)) + " customers have been loaded."
    return_to_admin_menu()


def admin_menu_item2():  # Admin menu second selection
    print "===== Admin: Create Account ====="
    new_account_name = raw_input("Please enter account holder name: ")
    new_account_password = raw_input("Please create a password for " + new_account_name + ": ")
    new_account_balance = raw_input("Opening Balance: ")
    username_list.append(new_account_name)
    password_list.append(new_account_password)
    balance_list.append(new_account_balance)
    print "An account has been created for " + new_account_name + " with starting balance of " + \
        new_account_balance
    return_to_admin_menu()


def admin_menu_item3():  # Admin menu third selection
    print "===== Admin: Close Account ====="
    account_holder_name_to_close = raw_input("Please enter acccunt holder name: ")
    if account_holder_name_to_close in username_list:
        print "The account for customer " + account_holder_name_to_close + " will be closed."
        approval = raw_input("Do you approve (yes/no?): ")
        if approval == "yes":
            password_list[username_list.index(account_holder_name_to_close)] = ""
            balance_list[username_list.index(account_holder_name_to_close)] = ""
            username_list[username_list.index(account_holder_name_to_close)] = ""
            print "The account for customer " + account_holder_name_to_close + " has been closed."
            return_to_admin_menu()
        else:
            print "Your account closing request has been cancelled."
            return_to_admin_menu()
    else:
        print "There is no available account for this account holder.\n " + \
            "You may try again with another name"
        admin_menu_item3()


def admin_menu_item4():  # Admin menu fourth selection function
    print "===== Admin: Search for an Account ====="
    search_for_account_holder = raw_input("Please enter account holder name: ")
    if search_for_account_holder in username_list:
        print "Account Holder: " + username_list[username_list.index(search_for_account_holder)]
        print "Current Balance: " + balance_list[username_list.index(search_for_account_holder)]
        return_to_admin_menu()
    else:
        print "There is no available account for this account holder.\n " + \
            "You may try again with another name."
        admin_menu_item4()


def admin_menu_item5():  # Admin menu fifth selection function
    print "===== Admin: See the Stats ====="
    print "Total number of accounts: " + str(len(username_list))
    non_zero_balance = 0
    total_balance = 0
    for i in range(len(balance_list)):
        if int(balance_list[i]) != 0:
            non_zero_balance += 1
        else:
            continue
    print "Number of Accounts with Non-Zero Balance: " + str(non_zero_balance)
    for i in range(len(balance_list)):
        total_balance += int(balance_list[i])
    print "Total Balance: " + str(total_balance)
    print "Average Balance: " + str(total_balance / len(username_list))
    return_to_admin_menu()


def return_to_admin_menu():  # Function to generalize returning to admin main menu
    choice = raw_input("   What do you want to do next?\n   1: Go to the admin menu\n   2: Quit\n   Your choice: ")
    quitting = ""
    if choice == "1":
        admin_main_page()
    else:
        return quitting


def return_to_menu():  # Function to generalize returning to main menu
    choice = raw_input("   What do you want to do next?\n   1: Go to main menu\n   2: Quit\n   Your choice: ")
    quitting = ""
    if choice == "1":
        main_page()
    else:
        return quitting


login_page()
