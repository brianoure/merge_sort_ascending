class PLD:
    def __init__(this,parts,leftover,dividing):
        this.parts   =parts
        this.leftover=leftover
        this.dividing=dividing

def my_inclusive_ascending_sort(starting,ending,mylist):
    if(starting==ending):
        pass
    else:
        for m in range(starting,(ending+1)):
            if((m+1)<len(mylist)):
                if(mylist[m]>mylist[m+1]):
                    swap_container = mylist[m+1]
                    mylist[m+1]    = mylist[m]
                    mylist[m]      = swap_container
                    my_inclusive_ascending_sort(starting,ending,mylist)
    
def parts_leftover_dividing_list(mylength):
    rslt =[]
    power=1
    while (True):
        dividing = (2**power)
        if((mylength//dividing)==0):
            break
        else:
            parts    = mylength//dividing
            leftover = mylength%dividing
            rslt     = rslt + [ PLD(parts,leftover,dividing) ]
            power    = power+1
    return rslt

def main_merge_sort_ascending(mylist):
    #NB:Destructive sort, the original list will be lost
    is_sorted  = True
    list_length= len(mylist)
    if(list_length==1):
        return mylist
    t = 0
    while(t<list_length):
        if((t+1)<=(list_length-1)):
            if(mylist[t]>mylist[t+1]):
                is_sorted = False
                break
        t = t+1
    if(is_sorted):
        return mylist
    else:
        if(list_length==2):
            if(mylist[0]>mylist[1]):
                swap_container = mylist[m+1]
                mylist[m+1]    = mylist[m]
                mylist[m]      = swap_container
                return mylist
        pld = parts_leftover_dividing_list(list_length)
        for pld_index in range(len(pld)):
            for part in range(pld[pld_index].parts):
                parts_start_index =  pld[pld_index].dividing*part
                parts_end_index   = (  (pld[pld_index].dividing*(1+part)  )-1  )
                my_inclusive_ascending_sort(parts_start_index,parts_end_index,mylist)#parts sort
                if(pld[pld_index].leftover):
                    leftover_start_index = parts_end_index + 1
                    my_inclusive_ascending_sort(leftover_start_index,(list_length-1),mylist)#leftover sort
        #print(mylist)
        return mylist
                
"""
b=[34,5,7,9,12,34,3,3]
main_merge_sort_ascending(b)
"""

    
    
