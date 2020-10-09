#this contains importable function that returns the solution 
#copy this file to the same dir , where you are going to use this 

#from TwoSums import twosums

#the function takes in two arguments , the list and the target

def twosums(list_name,target):
    length = len(list_name)             
    pos = list()                        #to save the answer

    for i in range(length):             #looping through the entire list
        for j in range(1,length):       #looping through the list excluding the above element
            if list_name[i]+list_name[j] == target:  #checking all the possible combination for answer
                if i != j:              #we cannot use same numbers twice
                    pos.append(i)       #adding thte index to the list
                    pos.append(j)       #adding the index to the list
    return pos
