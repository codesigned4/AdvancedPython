class Category:
   
    def __init__(self,name):
        self.ledger=[]
        self.name=name

    def deposit(self,amount,description=""):
        object={"amount": amount, "description": description}
        self.ledger.append(object)

    def withdraw(self,amount,description=""):
        object={"amount": -amount, "description": description}
        totalBudget=0
        for i in self.ledger:
            totalBudget+=i["amount"]
        if totalBudget>=amount:
            self.ledger.append(object)
            return True
        return False    

    def get_balance(self):
        balance=0
        for i in self.ledger:
            balance+=i["amount"]
        return balance

    def transfer(self,amount,budget):
        object={"amount": amount, "description": "Transfer from "+self.name}        
        object2={"amount": -amount, "description": "Transfer to "+budget.name}
        totalBudget=0
        for i in self.ledger:
            totalBudget+=i["amount"]
        if totalBudget-amount>=0:
            budget.ledger.append(object)
            self.ledger.append(object2)
            return True
        return False    

    def check_funds(self,amount):
        budget=0
        for i in self.ledger:
            budget+=i["amount"]

        if budget>amount:
            return True
        return False         

    def __str__(self):
        chart= self.name.center(30,"*")+"\n"
        budget=0
        for i in self.ledger:
            budget+=i["amount"]
            chart+=i["description"][:23].ljust(23)
            
            if len(str(format(i["amount"],".2f")))>=7:
                chart+=str(format(i["amount"],".2f"))+"\n"
            else:    
                chart+=str(format(i["amount"],".2f")).rjust(7)+"\n"
       
        chart+="Total: "+str(budget)  
        return chart

def create_spend_chart(categories):
    string="Percentage spent by category\n"
   # print("Percentage spent by category")
    i=0
    totalAmount=[]
    percentage=[]
    markers=[]
    sum=0
    for budget in categories:
        withdraw=0
        for member in budget.ledger:
            if member["amount"]<0:
                withdraw+=member["amount"]
        totalAmount.append(withdraw)
        
    for i in totalAmount:
        sum+=i
    
    for i in totalAmount:
        percentage.append(int(i*10/sum)+1)
        markers.append("o"*(int(i*10/sum)+1))
    #print(percentage,markers)
    numbers=["100|","90|","80|","70|","60|","50|","40|","30|","20|","10|","0|"]
    
    count=len(categories)*3+1
    #print(count)
    my_array = [[" "]*(count+2) for i in range(11)]
    
    for i in range(11):
        my_array[i][11]="\n"
        for j in range(count+1):
            if i==0:
                my_array[j][i]=numbers[j].rjust(4)
                    
        try:
            for o in percentage:
                if o==i: 
                    index=percentage.index(o)    
                    index=index*3+2                
                            
                    # print("o i ye eşit",o,percentage.index(o),index)
                    for j in range(o,-1,-1,):
                       #  print("basla",j,10-j,index)
                        my_array[10-j][index]="o"
        except:
            pass
    
    dashes=(1+len(categories)*3)*"-"
    rjustDashes=5+len(categories)*3 #5+ because of lenght of 100|  
    
    for i in range(len(my_array)):    
        for j in range(len(my_array[i])):
            string+=my_array[i][j]
           # print(my_array[i][j],end="")
    
   # print(dashes.rjust(rjustDashes))    
    string+=dashes.rjust(rjustDashes)
    
    nameslength=[]
    namesarray=[]
    for budgest in categories:
        nameslength.append(len(budgest.name))
        namesarray.append(budgest.name)
    maxLenght=max(nameslength)

    names=[[" "]*rjustDashes for i in range(maxLenght)]
    """ for i in names:
        print(i)
    """
#    print(len(names),len(names[0]))
    for o in namesarray:
        for i in range(len(names)):
            names[i][rjustDashes-1]="\n"
            if len(names)-i==len(o):
                index=namesarray.index(o)
                
                index=index*3+5  
                
                for j in range(len(o)):
                    #print(j)
                    try:
                        names[j][index]=o[j]
                    except:
                        pass
                    #print(names[i][j],end="")    
     
    """ for i in names:
        print(i)
  """
    string+="\n"
    for i in range(len(names)):
        for j in range(len(names[0])):
            string+=names[i][j]
           # print(names[i][j],end="")    

    return string