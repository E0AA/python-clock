SYMHEIGHT: int = 16

SYMBOLS: dict = {
    "0": """
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0 000 0:::::0
0:::::0 000 0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000     """,
    "1": """
  1111111   
 1::::::1   
1:::::::1   
111:::::1   
   1::::1   
   1::::1   
   1::::1   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
111::::::111
1::::::::::1
1::::::::::1
111111111111""",
    "2": """
 222222222222222    
2:::::::::::::::22  
2::::::222222:::::2 
2222222     2:::::2 
            2:::::2 
            2:::::2 
         2222::::2  
    22222::::::22   
  22::::::::222     
 2:::::22222        
2:::::2             
2:::::2             
2:::::2       222222
2::::::2222222:::::2
2::::::::::::::::::2
22222222222222222222""",
    "3": """
 333333333333333   
3:::::::::::::::33 
3::::::33333::::::3
3333333     3:::::3
            3:::::3
            3:::::3
    33333333:::::3 
    3:::::::::::3  
    33333333:::::3 
            3:::::3
            3:::::3
            3:::::3
3333333     3:::::3
3::::::33333::::::3
3:::::::::::::::33 
 333333333333333   """,
    "4": """
       444444444  
      4::::::::4  
     4:::::::::4  
    4::::44::::4  
   4::::4 4::::4  
  4::::4  4::::4  
 4::::4   4::::4  
4::::444444::::444
4::::::::::::::::4
4444444444:::::444
          4::::4  
          4::::4  
          4::::4  
        44::::::44
        4::::::::4
        4444444444""",
    "5": """
555555555555555555 
5::::::::::::::::5 
5::::::::::::::::5 
5:::::555555555555 
5:::::5            
5:::::5            
5:::::5555555555   
5:::::::::::::::5  
555555555555:::::5 
            5:::::5
            5:::::5
5555555     5:::::5
5::::::55555::::::5
 55:::::::::::::55 
   55:::::::::55   
     555555555     """,
    "6": """
        66666666   
       6::::::6    
      6::::::6     
     6::::::6      
    6::::::6       
   6::::::6        
  6::::::6         
 6::::::::66666    
6::::::::::::::66  
6::::::66666:::::6 
6:::::6     6:::::6
6:::::6     6:::::6
6::::::66666::::::6
 66:::::::::::::66 
   66:::::::::66   
     666666666     """,
    "7": """
77777777777777777777
7::::::::::::::::::7
7::::::::::::::::::7
777777777777:::::::7
           7::::::7 
          7::::::7  
         7::::::7   
        7::::::7    
       7::::::7     
      7::::::7      
     7::::::7       
    7::::::7        
   7::::::7         
  7::::::7          
 7::::::7           
77777777            """,
    "8": """
     888888888     
   88:::::::::88   
 88:::::::::::::88 
8::::::88888::::::8
8:::::8     8:::::8
8:::::8     8:::::8
 8:::::88888:::::8 
  8:::::::::::::8  
 8:::::88888:::::8 
8:::::8     8:::::8
8:::::8     8:::::8
8:::::8     8:::::8
8::::::88888::::::8
 88:::::::::::::88 
   88:::::::::88   
     888888888     """,
    "9": """
     999999999     
   99:::::::::99   
 99:::::::::::::99 
9::::::99999::::::9
9:::::9     9:::::9
9:::::9     9:::::9
 9:::::99999::::::9
  99::::::::::::::9
    99999::::::::9 
         9::::::9  
        9::::::9   
       9::::::9    
      9::::::9     
     9::::::9      
    9::::::9       
   99999999        """,
    "/": """
       BBBBBBBB
       B::::::B
      B::::::B 
      B::::::B 
     B::::::B  
     B::::::B  
    B::::::B   
    B::::::B   
   B::::::B    
   B::::::B    
  B::::::B     
  B::::::B     
 B::::::B      
 B::::::B      
B::::::B       
BBBBBBBB       """,
    ":": """
                   
                   
                   
       XXXXX       
      X:::::X      
      X:::::X      
       XXXXX       
                   
       XXXXX       
      X:::::X      
      X:::::X      
       XXXXX       
                   
                   
                   
                   """,
    "P": """
PPPPPPPPPPPPPPPPP   
P::::::::::::::::P  
P::::::PPPPPP:::::P 
PP:::::P     P:::::P
  P::::P     P:::::P
  P::::P     P:::::P
  P::::PPPPPP:::::P 
  P:::::::::::::PP  
  P::::PPPPPPPPP    
  P::::P            
  P::::P            
  P::::P            
PP::::::PP          
P::::::::P          
P::::::::P          
PPPPPPPPPP          """,
    "A": """
               AAA               
              A:::A              
             A:::::A             
            A:::::::A            
           A:::::::::A           
          A:::::A:::::A          
         A:::::A A:::::A         
        A:::::A   A:::::A        
       A:::::A     A:::::A       
      A:::::AAAAAAAAA:::::A      
     A:::::::::::::::::::::A     
    A:::::AAAAAAAAAAAAA:::::A    
   A:::::A             A:::::A   
  A:::::A               A:::::A  
 A:::::A                 A:::::A 
AAAAAAA                   AAAAAAA""",
    "M": """
MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM""",
    " ": """
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               """
}

for key in SYMBOLS:
    SYMBOLS[key] = SYMBOLS[key][1:]