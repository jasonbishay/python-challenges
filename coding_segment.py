"""
fye@plaid.com
Bank to bank xfer
multiple txns b.w 2 banks, reduce total xfers per banks, send 1 instead of many
netting engine for hypothetical banks

26 banks, a,b,c,...
input xfers, 
output xfers with net effect

Central Bank algorithm, Bank A is central bank
Input:
    AB1
    BA2
Output:
    BA1

Input:
    AB1
    BA2
    BC1
Net Balances:
    A: 1
    B: -2
    C: 1
Franklin Ye3:11 PM
Output:
    BA2
    AC1
"""
# This method will calculate the net balance for each bank
def net_balance(input):
    balance_dict = {
        "A" :  0,
        "B" : 0,
        "C" : 0,
        "D" : 0
    }

    for i in input:
        bank1 = i[0]
        bank2 = i[1]
        value = int(i[2])
        balance_dict[bank1] = int(balance_dict[bank1]) - value
        balance_dict[bank2] = int(balance_dict[bank2]) + value

    return balance_dict

# This method will perform the settling of the net balanced list
def settle(balance_dict):
    print(balance_dict)
    return_list =[]
    for i in balance_dict:
        if i != "A":
            if balance_dict[i] < 0:
                strVal = i+"A"+str(balance_dict[i]*-1)
            else:
                strVal = "A"+i+str((balance_dict[i]))
            return_list.append(strVal)

    return return_list

def cba(input):
   balanced = net_balance(input)
   return settle(balanced)


input = ["AB1", "BA2"]
print(cba(input))