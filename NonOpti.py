import numpy as np
import random as rd

def randint_with_exclusions(start, end, exclusions):
    while True:
        n = rd.randint(start, end)
        if n not in exclusions:
            return n



def step1(matrice):
    nb = rd.randint(0,3)
    matrice[nb][0] = 1
    return matrice


def step2(matrice):
    nb = rd.randint(0,3)
    i=1
    if(nb==0): #Cas de bord [0][1]
            while(1):
                if(matrice[nb][i-1] != 1 and matrice[nb+1][i-1]!= 1):
                    matrice[nb][i] = 1
                    break
                else:
                    nb2 = randint_with_exclusions(0, 3, {0,1})
                    if(nb2==2):
                        if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                    else:
                        if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                        else:
                            nb = rd.randint(0,3)
    elif(nb==1):
            while(1):
                if(matrice[nb-1][i-1] != 1 and matrice[nb][i-1]!= 1 and matrice[nb+1][i-1]!= 1):#gamma==1 forcément
                    matrice[nb][i] = 1
                    break
                else:
                    nb2 = rd.randint(2,3)
                    if(nb2==2):
                        if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                    else:
                        if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                        else:
                            nb = 0
                            matrice[nb][i] = 1
                            break

    elif(nb==2):
            while(1):
                 if(matrice[nb-1][i-1] != 1 and matrice[nb][i-1]!= 1 and matrice[nb+1][i-1]!= 1):#alpha==1 forcément
                    matrice[nb][i] = 1
                    break
                 else:
                    nb2 = randint_with_exclusions(0, 3, {2})
                    if(nb2==3):
                        if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                        else:
                            nb = 0
                            matrice[nb][i] = 1
                            break
                    elif(nb2==0):
                        if(matrice[nb2][i-1] != 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break 
                        else:
                            nb = 3
                            matrice[nb][i] = 1
                            break 
                    elif(nb2==1): 
                       if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break 
                       else:
                            nb2 = randint_with_exclusions(0, 3, {1,2})
                            if(nb2 == 0):
                                if(matrice[nb2][i-1] != 1 and matrice[nb2+1][i-1]!= 1):
                                    matrice[nb2][i] = 1
                                    break 
                                else:
                                    nb=3
                                    matrice[nb][i] = 1
                                    break
                            else:
                                if(matrice[nb2][i-1] != 1 and matrice[nb2-1][i-1]!= 1):
                                    matrice[nb2][i] = 1
                                    break 
                                else:
                                    nb=0
                                    matrice[nb][i] = 1
                                    break

    elif(nb==3):
            while(1):
                if(matrice[nb-1][i-1] != 1 and matrice[nb][i-1]!= 1):
                    matrice[nb][i] = 1
                    break
                else:
                     nb2 = randint_with_exclusions(0, 3, {2,3})
                     if(nb2==0):
                          if(matrice[nb2][i-1] != 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                          else:
                              nb=1
                              matrice[nb][i] = 1
                              break
                     elif(nb2==1):
                         if(matrice[nb2-1][i-1] != 1 and matrice[nb2][i-1]!= 1 and matrice[nb2+1][i-1]!= 1):
                            matrice[nb2][i] = 1
                            break
                         else:
                              nb=0
                              matrice[nb][i] = 1
                              break
    return matrice



def step3(matrice):
    nb = rd.randint(0,3)
    i=2
    if(nb==0):#Cas de bord [0][2]
        if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb+1][i-1] == 0):
            matrice[nb][i]=1
            return matrice
        else:
            nb2 = randint_with_exclusions(0, 3, {0})
            if(nb2==1):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                     matrice[nb2][i]=1
                     return matrice
                else:
                    nb2=2
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                        nb2=3
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                            matrice[nb2][i]=1
                            return matrice
                        else:
                            print(matrice)
                            print("")
                            print("")
                            matrice2 = np.zeros((4, 4))
                            return step3(step2(step1(matrice2)))
            
            elif(nb2==2):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                     matrice[nb2][i]=1
                     return matrice
                else:
                    nb2=3
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                        nb2=1
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                        else:
                             print(matrice)
                             print("")
                             print("")
                             matrice2 = np.zeros((4, 4))
                            
                            
                             return step3(step2(step1(matrice2)))
                        
                        
            elif(nb2==3):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                    matrice[nb2][i]=1
                    return matrice
                else:
                    nb2==1
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                        nb2=2
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                        else: 
                            print(matrice)
                            print("")
                            print("")
                            matrice2 = np.zeros((4, 4))
                            return step3(step2(step1(matrice2)))

    
    elif(nb==1):#Cas [1][2]
        if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
            matrice[nb][i]=1
            return matrice
        else:
            nb2 = randint_with_exclusions(0, 3, {1})
            if(nb2==0):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                    matrice[nb2][i]=1
                    return matrice
                else:
                    nb2=2
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                         nb2=3
                         if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                            matrice[nb2][i]=1
                            return matrice
                         else:
                             print(matrice)
                             print("")
                             print("")
                             matrice2 = np.zeros((4, 4))
                             return step3(step2(step1(matrice2)))
                             
            elif(nb2==2):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                else:
                    nb2=3
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                        nb2=0
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                        else:
                             print(matrice)
                             print("")
                             print("")
                             matrice2 = np.zeros((4, 4))
                             return step3(step2(step1(matrice2)))
            elif(nb2==3):
                if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                    matrice[nb2][i]=1
                    return matrice
                else:
                    nb2=0
                    if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                    else:
                        nb2=2
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                        else:
                             print(matrice)
                             print("")
                             print("")
                             matrice2 = np.zeros((4, 4))
                             return step3(step2(step1(matrice2)))


    elif(nb==2):#Cas [2][2]
         if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
                        matrice[nb][i]=1
                        return matrice
         else:
             nb2 = randint_with_exclusions(0, 3, {2})
             if(nb2==0):
                 if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                 else:
                     nb2=1
                     if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                     else:
                         nb2=3
                         if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                            matrice[nb2][i]=1
                            return matrice
                         else:
                              print(matrice)
                              print("")
                              print("")
                              matrice2 = np.zeros((4, 4))
                              return step3(step2(step1(matrice2)))
             elif(nb2==1):
                  if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                        matrice[nb2][i]=1
                        return matrice
                  else:
                      nb2=3
                      if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                        matrice[nb2][i]=1
                        return matrice
                      else:
                          nb2=0
                          if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                          else:
                               print(matrice)
                               print("")
                               print("")
                               matrice2 = np.zeros((4, 4))
                               return step3(step2(step1(matrice2)))
             elif(nb2==3):
                 if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1]== 0):
                        matrice[nb2][i]=1
                        return matrice
                 else:
                     nb2=0
                     if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                     else:
                         nb2=1
                         if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                         else:
                             print(matrice)
                             print("")
                             print("")
                             matrice2 = np.zeros((4, 4))
                             return step3(step2(step1(matrice2)))
    elif(nb==3):#Cas [3][2]
         if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1]== 0):
                        matrice[nb][i]=1
                        return matrice
         else:
             nb2 = randint_with_exclusions(0, 3, {3})
             if(nb2==0):
                  if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                  else:
                      nb2=1
                      if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                      else:
                          nb2=2
                          if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                             matrice[nb2][i]=1
                             return matrice
                          else:
                              print(matrice)
                              print("")
                              print("")
                              matrice2 = np.zeros((4, 4))
                              return step3(step2(step1(matrice2)))
             elif(nb2==1):
                  if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                            matrice[nb2][i]=1
                            return matrice
                  else:
                       nb2=2
                       if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                             matrice[nb2][i]=1
                             return matrice
                       else:
                            nb2=0
                            if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                                matrice[nb2][i]=1
                                return matrice
                            else:
                                 print(matrice)
                                 print("")
                                 print("")
                                 matrice2 = np.zeros((4, 4))
                                 return step3(step2(step1(matrice2)))
             elif(nb2==2):
                   if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                             matrice[nb2][i]=1
                             return matrice
                   else:
                        nb2=0
                        if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2+1][i-1] == 0):
                                matrice[nb2][i]=1
                                return matrice
                        else:
                             nb2=1
                             if(matrice[nb2][i-2] == matrice[nb2][i-1] == matrice[nb2-1][i-1] == matrice[nb2+1][i-1] == 0):
                                matrice[nb2][i]=1
                                return matrice
                             else:
                                 print(matrice)
                                 print("")
                                 print("")
                                 matrice2 = np.zeros((4, 4))
                                 return step3(step2(step1(matrice2)))


def step4(matrice):
     nb = rd.randint(0,3)
     i=3
     flag=0
     while(1):
          if(nb==0):
            if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb+1][i-1] == 0):
                matrice[nb][i]=1
                break
            else:
                print("PasSol==1")
                flag=1
                break
          elif(nb==1):
                if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
                                matrice[nb][i]=1
                                break
                else:
                     print("PasSol==2")
                     flag=1
                     break
          elif(nb==2):
               if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
                                matrice[nb][i]=1
                                break
               else:
                     print("PasSol==3")
                     flag=1
                     break
          elif(nb==3):
               if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == 0):
                                matrice[nb][i]=1
                                break
               else:
                     print("PasSol==4")
                     flag=1
                     break
               
     if(flag==1):
        print("Recursion")
        matrice2 = np.zeros((4, 4))
        return step4(step3(step2(step1(matrice2))))
          
     return matrice
              

              
                    
#------Résultats                                
matrice = np.zeros((4, 4))
print(step4(step3(step2(step1(matrice)))))
