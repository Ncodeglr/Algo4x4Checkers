                        #Algorithme du jeu de la Dame pour une matrice 4x4

import numpy as np
import random as rd

def step1(matrice):
    nb = rd.randint(0,3)
    matrice[nb][0] = 1
    return matrice

def step2(matrice):
    nb = rd.randint(0,3)
    i=1
    flag=0
    while(1):
        if(nb==0):
            if(matrice[nb][i-1] == matrice[nb+1][i-1] == 0):
                matrice[nb][i] = 1
                break
            else:
                 print("Step2 : Pas de Solution == 1")
                 flag=1
                 break
        elif(nb==1 or nb==2):
            if(matrice[nb-1][i-1] == matrice[nb][i-1] == matrice[nb+1][i-1] == 0):
                    matrice[nb][i] = 1
                    break
            else:
                 print("Step2 : Pas de Solution == 2")
                 flag=1
                 break
        elif(nb==3):
             if(matrice[nb-1][i-1] == matrice[nb][i-1] == 0):
                    matrice[nb][i] = 1
                    break
             else:
                  print("Step2 : Pas de Solution == 3")
                  flag=1
                  break
                  
    if(flag==1):
        print("Recursion-Step2")
        matrice2 = np.zeros((4, 4))
        return step2(step1(matrice2))
    return matrice


def step3(matrice):
    nb = rd.randint(0,3)
    i=2
    flag=0
    while(1):
         if(nb==0):
            if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb+1][i-1] == 0):
                matrice[nb][i]=1
                break
            else:
                print("Step3 : Pas de Solution == 1")
                flag=1
                break
         elif(nb==1 or nb==2):
              if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
                    matrice[nb][i]=1
                    break
              else:
                  print("Step3 : Pas de Solution == 2")
                  flag=1
                  break
         elif(nb==3):
              if(matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1]== 0):
                        matrice[nb][i]=1
                        break
              else:
                print("Step3 : Pas de Solution == 3")
                flag=1
                break
    
    if(flag==1):
        print("Recursion-Step3")
        matrice2 = np.zeros((4, 4))
        return step3(step2(step1(matrice2)))
    return matrice
     

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
                print("Step4 : Pas de Solution == 1")
                flag=1
                break
          elif(nb==1 or nb==2):
               if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == matrice[nb+1][i-1] == 0):
                    matrice[nb][i]=1
                    break
               else:
                    print("Step4 : Pas de Solution == 2")
                    flag=1
                    break
          elif(nb==3):
               if(matrice[nb][i-3] == matrice[nb][i-2] == matrice[nb][i-1] == matrice[nb-1][i-1] == 0):
                    matrice[nb][i]=1
                    break
               else:
                    print("Step4 : Pas de Solution == 3")
                    flag=1
                    break
     if(flag==1):
        print("Recursion - Step4")
        matrice2 = np.zeros((4, 4))
        return step4(step3(step2(step1(matrice2))))
     return matrice

#------Résultats                                
matrice = np.zeros((4, 4))
print(step4(step3(step2(step1(matrice)))))

