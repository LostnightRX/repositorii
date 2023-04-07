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
    ********
    *******
'''
    
        }
    for i in slovo:
        res.append(a[i].split('\n'))
    for i in range(len(res)):
         
        for j in range(8):
            print(res[i][j])
    print()
if __name__ == '__main__':
    slovar(input())
