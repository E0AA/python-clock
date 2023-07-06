SYMHEIGHT: int = 6

SYMBOLS: dict = {
    "0": """
 .d88b.  
.8P  88. 
88  d'88 
88 d' 88 
`88  d8' 
 `Y88P'  """,
    "1": """
 db 
o88 
 88 
 88 
 88 
 VP """,
    "2": """
.d888b. 
VP  `8D 
   odD' 
 .88'   
j88.    
888888D """,
    "3": """
d8888b. 
VP  `8D 
  oooY' 
  ~~~b. 
db   8D 
Y8888P' """,
    "4": """
  j88D  
 j8~88  
j8' 88  
V88888D 
    88  
    VP  """,
    "5": """
  ooooo 
 8P~~~~ 
dP      
V8888b. 
    `8D 
88oobY' """,
    "6": """
   dD   
  d8'   
 d8'    
d8888b. 
88' `8D 
`8888P  """,
    "7": """
d88888D 
VP  d8' 
   d8'  
  d8'   
 d8'    
d8'     """,
    "8": """
.d888b. 
88   8D 
`VoooY' 
.d~~~b. 
88   8D 
`Y888P' """,
    "9": """
.d888b. 
88' `8D 
`V8o88' 
   d8'  
  d8'   
 d8'    """,
    "/": """
     . 
    8D 
   88' 
  d8'  
 d8'   
d8'    """,
    ":": """
  db   
  vp   
       
  db   
  vp   
       """,
    "P": """
d8888b. 
88  `8D 
88oodD' 
88~~~   
88      
88      """,
    "A": """
 .d8b.  
d8' `8b 
88ooo88 
88~~~88 
88   88 
YP   YP """,
    "M": """
.88b  d88. 
88'YbdP`88 
88  88  88 
88  88  88 
88  88  88 
YP  YP  YP """,
    " ": """
    
    
    
    
    
    """
}

for key in SYMBOLS:
    SYMBOLS[key] = SYMBOLS[key][1:]