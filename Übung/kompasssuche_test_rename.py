import numpy as np #line:1
def kompasssuche_test (f_a ,x0 :np .ndarray ,s0 :float ,theta :float)->int :#line:3	  
   
    """Kompasssuche algorithm to find the minimum of a function.
    Stops when the expected minimum of 0.0 is reached with a tolerance of 0.001.
    
    Parameters:
        f (callable): the function to minimize.
        x0 (ndarray): the initial point.
        s0 (float): the initial step size.
        theta (float): reduction factor of the step size.
        
    Returns:
        int: number of iterations needed to reach the solution (or max. 1000)
    """
    x,y=x0
  

    min =0.0
    tol =0.001
    Dim =np .concatenate ((np .identity (len (x0 )),-np .identity (len (x0 ))),axis =1 )#line:18
    k =1 #Zähler der Iterationen  
    min_wert =f_a (x0[0],x0[1])#line:23
    while (min_wert >min +tol ):#line:26
        Bol_Wert =False #line:28
        count =0 #line:29
        while count <Dim .shape [1 ]and not Bol_Wert :#line:32
            akt_wert =f_a (x0 +s0 *Dim [:,count ])#line:34
            if akt_wert <min_wert :#line:37
                x0 =x0 +s0 *Dim [:,count ]#line:39
                min_wert =akt_wert #line:40
                Bol_Wert =True #line:43
            count +=1 #line:44
        if not Bol_Wert :#line:47
            s0 =theta *s0 #line:48
        k +=1 #line:51
        if (k >=1000 ):#line:54
            break #line:55
    return k 
