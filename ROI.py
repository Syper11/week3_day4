#1 Rental Income like laundary,storage,Misc
#2 Expenses Tax, Insurence,Utilities,HOA,Lawn Service or Snow removal, Vaconcy, CapEx, property manager, mortgage
#3 Cash flow - expenses for monthly income convert this after to yearly amount *12
#4 Cash On cash return Down payment, closing cost, rehab budget, misc other add evrything up then take it divide by year cash flow.

class ROI():
    def __init__(self):
        self.Extra_Income = None
        self.Property_Expenses = None
        self.Yearly_Cash_Flow = None
    
    def Get_Rental_Income(self):
        print("I am here to help figure out the rental income cost!")
        Income = int(input("How much are you getting paid for rent? If you do not enter 0! $"))
        storage = int(input("Do you have extra storage on the property? If you do not enter 0! $"))
        laundary = int(input("Do you charge for laundary on the property if so how much? If you do not enter 0! $"))
        misc = int(input("Do you charge for anything else on the property if so how much? If you do not enter 0! $"))
        print(f'Rental income amount,${Income},storage amount,${storage},laundary amount,${laundary},misc amount,${misc}! Adding this all up for you!')
        self.Extra_Income = (storage + laundary + misc + Income)
        print(f'${self.Extra_Income}')

    def Get_Expenses(self):
        print('We will help you calculate your expenses now!')
        Tax = int(input('What is the tax for this property? $'))
        Insurence = int(input('How much is the insurence for this property? $'))
        Utilities = int(input('How much is the utilities for this property? Such as electric,sewer,water,garbage,gas, and etc? If you do not enter 0. $'))
        property_maintance = int(input('Do you pay for lawn car or snow removal for this property if so how much? If you do not enter 0. $'))
        Vaconcy = int(input('How much do you want to put into vaconcy?"recommend 5%" $'))
        Mortgage = int(input('How much do you owe the bank monthly? If you do not enter 0.$'))
        print(f'Tax Expense amount,${Tax},Insurence amount,${Insurence},Utilities amount,${Utilities},proprty_maintance amount,${property_maintance}, Vaconcy amout,${Vaconcy},Mortgage amout,${Mortgage}! Adding this all up for you!')
        self.Property_Expense = (Tax + Insurence + Utilities + property_maintance + Vaconcy + Mortgage)
        print(f'${self.Property_Expense}')
        

    def Get_Cash_Flow(self):
        Cash_Flow = (self.Extra_Income - self.Property_Expense)
        print(f'This is your monthly income${Cash_Flow}')
        self.Yearly_Cash_Flow = (Cash_Flow*12)
        print(f'This is your yearly cash flow ${self.Yearly_Cash_Flow}')
    
        

    def Payback(self):
        print("Here We will figure out your Payback % for the rental")
        Down_Payment = int(input('How much of a down payment did you do for the property? If you do not enter 0.$'))
        Closing_Cost = int(input('How much was or will be the closing cost for the property? If you do not enter 0.$'))
        Rehab_budget = int(input('How much for repairs for the property? If you do not enter 0.$'))
        misc_other = int(input('Any other expense for the property? If you do not enter 0.$'))
        print(f'Down payment amount,${Down_Payment}, Closing cost amount, ${Closing_Cost}, Fixes after purchase amount, ${Rehab_budget},Anything else amount, ${misc_other}')
        Total_Investment = (Down_Payment + Closing_Cost + Rehab_budget + misc_other)
        print(f'This is the total cost for investment.${Total_Investment}')
        Cash_On_Cash = (self.Yearly_Cash_Flow / Total_Investment)
        Cash_On_Cash_ROI = (Cash_On_Cash*100)
        print(f'This is the ROI {Cash_On_Cash_ROI}%')

    def run(self):
        while True:
            x = input('Lets get started with the ROI type start or at anytime you want to quit type Q.')
            if x.lower() == 'Q':
                print('Thanks for trying out the RIO.')
                break
            elif x.lower() == 'start':
                ROI.Get_Rental_Income(self)
                ROI.Get_Expenses(self)
                ROI.Get_Cash_Flow(self)
                ROI.Payback(self)
            return

x = ROI
x.run(x)

