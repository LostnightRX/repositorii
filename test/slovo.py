import sys
def slovar(slovo):
    slovo = list(slovo)
    res = []
    a = {'а': '''
        *    
       ***   
      ** **  
     **   ** 
    *********
    *********
    ***   ***
    ***   ***
                 ''',
    'б': '''
    *********
    *********
    *****    
    *******  
    **    ***
    **    ***
    ***  *** 
    *******  
''',
    'в' : '''
    ******** 
    **     **
    **     **
    ******** 
    ******** 
    **     **
    **     **
    ******** 
''',
    'г' : '''
    *********
    *********
    **       
    **       
    **       
    **       
    **       
    **       
''',
    'д' : '''
        *    
        *    
       ***   
      ** **  
    *********
    *********
    **     **
    **     **
''',
    'е' : '''
    *********
    *********
    **       
    *******  
    *******  
    **       
    *********
    *********
''',
    'ж': '''
    **  *  **
    **  *  **
     ** * ** 
      *****  
      *****  
     ** * ** 
    **  *  **
    **  *  **
''',
    'з': '''
    ******** 
      *******
           **
        **** 
        **** 
          ***
      *******
    ******** 
''',
    'и':'''
    **     **
    **    ***
    **   ****
    **  ** **
    ** **  **
    ****   **
    ***    **
    **     **
''',
    'й':'''
      *****  
    **     **
    **    ***
    **   ****
    **  ** **
    ** **  **
    ****   **
    ***    **
''',
    'к': '''
    **     **
    **    ** 
    **   **  
    ******   
    ******   
    **   **  
    **    ** 
    **     **
''',
    'л':'''
       ******
      *******
     **    **
     **    **
     **    **
     **    **
     **    **
    **     **
''',
    'м':'''
    **      **
    ***    ***
    ** *  * **
    **  **  **
    **  **  **
    **  **  **
    **  **  **
    **  **  **
''',
    'н':'''
    **     **
    **     **
    **     **
    *********
    *********
    **     **
    **     **
    **     **
''',
    'о':'''
     ******* 
    *********
    **     **
    **     **
    **     **
    **     **
    *********
     ******* 
''',
    'п':'''
    *********
    *********
    **     **
    **     **
    **     **
    **     **
    **     **
    **     **
''',
    'р':'''
    ******** 
    **      *
    **      *
    ******** 
    **       
    **       
    **       
    **       
''',
    'с':'''
     ********
    ******** 
    **       
    **       
    **       
    **       
    ******** 
     ********
''',
    'т':'''
    *********
    *********
       ***   
       ***   
       ***   
       ***   
       ***   
       ***   
''',
    'у':'''
     **   ***
      ** *** 
       ****  
       ***   
       **    
      **     
     **      
    **       
''',
    'ф':'''
       ***   
     *  *  * 
    *   *   *
    *   *   *
    *   *   *
     *  *  * 
       ***   
        *    
''',
    'х':'''
    **     **
     **   ** 
      ** **  
       ***   
       ***   
      ** **  
     **   ** 
    **     **
''',
    'ц':'''
    **    ** 
    **    ** 
    **    ** 
    **    ** 
    **    ** 
    ******** 
          ***
           **
''',
    'ч': '''
    ***   ***
    ***   ***
    ***   ***
    *********
    *********
          ***
          ***
          ***
''',
    'ш': '''
    **  ***  **
    **  ***  **
    **  ***  **
    **  ***  **
    **  ***  **
    **  ***  **
    ***********
    ***********
''',
    'щ': '''
    **  **  **  
    **  **  **  
    **  **  **  
    **  **  **  
    **  **  **  
    *********** 
            *** 
             ***
''',
    'ъ':'''
    ****     
      **     
      **     
      ****** 
      *** ***
      **   **
      *** ***
       ***** 
''',
    'ы':'''
    **     **
    **     **
    **     **
    *****  **
    **  ** **
    **  ** **
    **  ** **
     ****  **
''',
    'ь':'''
    **       
    **       
    **       
    ******** 
    **     **
    **     **
    **     **
     ******* 
''',
    'э':'''
    *******  
    ******** 
          ***
    *********
    *********
          *** 
    ******** 
    *******  
''',
    'ю':'''
    **  **** 
    ** **  **
    ** **  **
    *****  **
    *****  **
    ** **  **
    ** **  **
    **  **** 
''',
    'я':'''
     ********
    **     **
    **     **
     **    **
      *******
      **   **
     **    **
    ***    **
''',
        }
    for i in slovo:
        if i == 'ё':
            i = 'е'
        res.append(a[i].split('\n'))
    for j in range(9):
        for i in range(len(res)):
            sys.stdout.write(res[i][j])
        sys.stdout.write('\n')
if __name__ == '__main__':
    slovar(input())
