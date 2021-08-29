
def arithmetic_arranger(problems,isCalculate=False):

    arranged_problems=""
    if len(problems)>5:
      return "Error: Too many problems."
    arranger_array = []    
    answers=[]
    for i in range(len(problems)):
       
       splittedNumbers=problems[i].split()
       numbers=[splittedNumbers[0],splittedNumbers[2]]
       opeartors=[c for c in problems[i] if c in '+-/*()_'] 

       if "*" in opeartors or "/" in opeartors:  
           return "Error: Operator must be '+' or '-'." 
       
       try:
            max=int(numbers[0]) if int(numbers[0])>int(numbers[1]) else int(numbers[1])
       except:
           return "Error: Numbers must only contain digits."
       maxLen=len(str(max))
       dashes=(maxLen+2)*"-"
       
       
       if len(numbers[0])>4 or len(numbers[1])>4:
           return "Error: Numbers cannot be more than four digits."
       
       a=numbers[0].rjust(len(dashes))
       b=opeartors[0]+numbers[1].rjust(len(dashes)-1)
       c=dashes 
       arranger_array.append(a)      
       arranger_array.append(b)
       arranger_array.append(c)
       answers.append(eval(numbers[0]+opeartors[0]+numbers[1]))

    space="    "
   
    for i in range(0,len(arranger_array),3):
        if i ==0:
            arranged_problems+=arranger_array[i]+space
        else:
            arranged_problems+=arranger_array[i]+space
    arranged_problems+="\n" 
    
    for i in range(1,len(arranger_array),3):
        arranged_problems+=arranger_array[i]+space
    arranged_problems+="\n"

    for i in range(2,len(arranger_array),3):
        arranged_problems+=arranger_array[i]+space

    
    if isCalculate==True:
        arranged_problems+="\n"
        for i in range(len(answers)):
            if i==0:
                arranged_problems+=str(answers[i]).rjust(len(arranger_array[2]))+space
            else:
                arranged_problems+=str(answers[i]).rjust(len(arranger_array[i*3+2]))+space

        
    return arranged_problems

#print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
