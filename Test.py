def test_customer_login():
    #The system shall require account holders to insert bank card to the teller machine and put in the correct preset password in order to login.
    cardinfo=Cardinfo()
    #get the cardnumber from the bank card inserted
    cardnumber=cardinfo.getcardnumber()
    #get the preset pin number from central security system
    pin1=cardinfo.getpresetpin()
    
    assert len(account) == 123456
    assert len(pin1)==456789
    #check access has not been granted
    assert len(access)==0

    
    cutomerlogin()
    #ask user to enter pin number
    pin2=int(input("\nEnter account pin: "))
    #if password matches
    if pin2==pin1:
        #check if access has been granted
        assert access==1





    

def test_teller_login():
    #The system shall require bank tellers to put in the preset account number and password in order to login.
    cardinfo=Cardinfo()
    #get the cardnumber from the bank card inserted
    cardnumber1=cardinfo.getcardnumber()
    #get the preset pin number from central security system
    pin1=cardinfo.getpresetpin()
    
    assert len(account) == 123456
    assert len(pin1)==456789
    #check access has not been granted
    assert len(access)==0

    
    tellerlogin()
    #ask user to enter cardnumber number
    cardnumber2=int(input("\nEnter card number: "))
    #ask user to enter pin number
    pin2=int(input("\nEnter preset pin number: "))
    #if password and cardnumber match
    if cardnumber2==cardnumber1&pin2==pin1:
        #check if access has been granted
        assert access==1




        
    
def test_authorized_login():
    #The system shall allow bank tellers to access customers’s account with the correct answer to customers private questions.
    cardinfo=Cardinfo()
    #get the cardnumber from the bank card inserted
    cardnumber1=cardinfo.getcardnumber()
    #get the preset pin number from central security system
    pin1=cardinfo.getpresetpin()
    #get the preset personal information from central security system
    dateofbirth1=cardinfo.getdob()
    
    assert len(account) == 123456
    assert len(pin1)==456789
    #check access has not been granted
    assert len(access)==0

    authorizedlogin()
    #ask user to enter cardnumber number
    cardnumber2=int(input("\nEnter card number: "))
    #ask user to enter pin number
    pin2=int(input("\nEnter preset pin number: "))
    #ask user to enter the date of birth for the account holder
    dateofbirth2=int(input("\nEnter the preset date of birth "))
    #if password and cardnumber and personal information match
    if cardnumber2==cardnumber1&&pin2==pin1&&dateofbirth1=dateofbirth2:
        #check if access has been granted
        assert access==1




        

def test_balance_checking():
    #The system shall provide the current balance of the select account.
    cardinfo=Cardinfo()
    #start a new account, so the current balance will be zero.
    startnewaccount()
    #Get the current balance from central security system
    balance= cardinfo.getbalance()
    #Check if the current on the new account is 0.
    assert balance==0
    

    
def test_Withdraw_amount_verification():
    #The system shall provided options for account holder to choose the amount of money to be withdrawn.
    cardinfo=Cardinfo()
    #get the current balance
    balance1= cardinfo.getbalane()
    #Select the amount to be withdrawn
    amount=getwithdrawamount()
    #Withdraw the same amount of money
    cardinfo.withdraw(amount)
    #Check the new balance
    balance2= cardinf.getbalance()
    #Check if the amount of withdrawed money equals to the slected amount.
    assert int(balance1-balance2)==amount







    
def test_Deposit_amount_verification():
    #The system shall provided the amount of money that account holder just put in and wait for holder’s verification to see if the amount is correct.
    cardinfo=Cardinfo()
    #get the current balance
    balance1= cardinfo.getbalane()
    #Select the amount to be deposited
    amount=getdepositeamount()
    #Deposite the same amount of money
    cardinfo.deposite(amount)
    #Check the new balance
    balance2= cardinf.getbalance()
    #Check if the amount of deposite money equals to the slected amount.
    assert int(balance2-balance1)==amount
    






def test_Withdraw_failed_transition():
    #The system shall provide an information for user to show that the balance is insufficient and ask user to re-select the amount of of money to be withdrawn.
    #The system shall provided options for account holder to choose the amount of money to be withdrawn.
    cardinfo=Cardinfo()
    #get the current balance
    balance1= cardinfo.getbalane()
    #Select the amount to be withdrawn
    amount=getwithdrawamount()
    #Withdraw the same amount of money
    cardinfo.withdraw(amount)
    #Check the new balance
    balance2= cardinf.getbalance()
    #Check if the amount does not change
    assert balance2==balance1





    

def test_password_changing():
    #The system shall allow holder to change the password when preset password is received and access is granted
    cardinfo=Cardinfo()
    #get the cardnumber from the bank card inserted
    cardnumber=cardinfo.getcardnumber()
    #get the preset pin number from central security system
    pin1=cardinfo.getpresetpin()
    
    assert len(account) == 123456
    assert len(pin1)==456789

    changepin()
    #ask user to enter new pin number
    pin2=int(input("\nEnter new pin number: "))
    #Exit the current account
    cardinfo.exit()
    customerlogin()
    #ask user to enter pin number
    pin3=int(input("\nEnter account pin: "))
    #if password matches
    if pin3==pin2:
        #check if access has been granted
        assert access==1




    
def test_offline_offlineaccess():
    #The system shall not grant any access to users when the system is offline or not connected with central server.
    cardinfo=Cardinfo()
    #get the cardnumber from the bank card inserted
    cardnumber=cardinfo.getcardnumber()
    #get the preset pin number from central security system
    pin1=cardinfo.getpresetpin()
    
    assert len(account) == 123456
    assert len(pin1)==456789

    customerlogin()
    #ask user to enter pin number
    pin2=int(input("\nEnter account pin: "))
    #if password matches
    if pin2==pin1:
        #check if access has been granted, No access should be granted.
        assert access==0
    
