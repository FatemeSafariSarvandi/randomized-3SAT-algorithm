from CnfResolver import CnfResolver
import random
from datetime import datetime


startTime = datetime.now()

#Random initialization to literals
def random_initialization (cnf) :
    for i in range(0, cnf.nv):
        cnf.literals_values.append(random.choice([True, False]))
    

#A function that calculates the SAT value according to the guessed values for literals
def calculate_SAT(info , cnf):
    info["number_of_false_Clauses"] = 0
    info["answer"] = True
    info["clauses"] = []
    for cluase in cnf.clauses:
        for literal in cluase:
            if literal > 0:
               info["clause_values"] |= cnf.literals_values[literal-1]
            else:
               info["clause_values"] |= not cnf.literals_values[abs(literal)-1]
         
        info["clauses"].append(info["clause_values"])       
        info["answer"] &= info["clause_values"]
        if info["clause_values"]==False:
            info["number_of_false_Clauses"] +=1
        info["clause_values"] = False
    return info

#function for change valuation of literal in false clause
def change_valuation (info , cnf , i, calculate_SAT ):
    for lit in cnf.clauses[i]:
        cnf.literals_values[abs(lit) - 1] = not cnf.literals_values[abs(lit) - 1]
        temp = info["number_of_false_Clauses"]
        calculate_SAT(info, cnf)
        if temp > info["number_of_false_Clauses"] :
            print("change valuation of " , abs(lit) , "th literal" , sep="")
            break
        else : 
            cnf.literals_values[abs(lit) - 1] = not cnf.literals_values[abs(lit) - 1]
            calculate_SAT(info, cnf)


cnf = CnfResolver('uf20-05.cnf')
#cnf = CnfResolver('uf50-0993.cnf')
#cnf = CnfResolver('uf75-08.cnf')
#cnf = CnfResolver('uf100-04.cnf')
#cnf = CnfResolver('uf125-02.cnf')
#cnf = CnfResolver('uf150-06.cnf')
#cnf = CnfResolver('uf175-03.cnf')
#cnf = CnfResolver('uf200-039.cnf')
#cnf = CnfResolver('uf225-03.cnf')
#cnf = CnfResolver('uf250-02.cnf')

info = {
 "clause_values" : False,
 "answer" : True,
 "clauses" : [],
 "number_of_false_Clauses" : 0,
}

random_initialization(cnf)    
calculate_SAT(info, cnf)

change_order = cnf.nv/10
order = 0
while info["answer"] == False :
    order +=1
    for i in range(len(info["clauses"])):
        if info["clauses"][i] == False : 
            change_valuation(info , cnf , i , calculate_SAT)
            if info["answer"] == True:
                break
    if order > (change_order) :
        order = 0
        cnf.literals_values = []
        random_initialization(cnf)

print("valuation : ")
print(cnf.literals_values)
print("-------------------")
endTime = datetime.now()
print("run time : " ,end="")
print(endTime-startTime)    
    