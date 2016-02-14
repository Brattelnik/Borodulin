from sys import argv

nums = []        
verbose = False  
action = None    
for arg in argv[1:]:                                
    if action is True:                              
        action = arg                                
        if action not in ('-', '+', '*', '/'):      
            raise ValueError("unknown operator")   
    elif '-' not in arg:                            
        nums.append(arg)                            
    elif arg in ('-v', '--verbose'):
        verbose = True
    elif arg in ('-a', '--action'):                 
        action = True                               
    else:                                           
        print('usage: python ex.py [-v] [-a] [action] [vales]')
        exit()
        
if len(nums) > 2:                                   
    print('Warning! Number of arguments is greater than two. Do you wish to proceed? \nThis will apply the operator to all of the values. (y/n)')
    ans = ""
    if ans in ('no', 'n'):
        exit()

ans = float(nums[0])                                
for num in nums:                                    
    if action == "+":
        ans += float(num)
    elif action == "-":
        ans -= float(num)
    elif action == "*":
        ans *= float(num)
    else:
        ans /= float(num)
        
if verbose:
    print(action.join([str(i) for i in nums]) + "=" + (str(int(ans)) if int(ans) == ans else str(ans)))
else:
    print(str(int(ans)) if int(ans) == ans else str(ans))

