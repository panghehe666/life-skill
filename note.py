import re
import pandas as pd


print(r'''
      ___           ___           ___           ___     
     /\__\         /\  \         /\  \         /\  \    
    /::|  |       /::\  \        \:\  \       /::\  \   
   /:|:|  |      /:/\:\  \        \:\  \     /:/\:\  \  
  /:/|:|  |__   /:/  \:\  \       /::\  \   /::\~\:\  \ 
 /:/ |:| /\__\ /:/__/ \:\__\     /:/\:\__\ /:/\:\ \:\__\
 \/__|:|/:/  / \:\  \ /:/  /    /:/  \/__/ \:\~\:\ \/__/
     |:/:/  /   \:\  /:/  /    /:/  /       \:\ \:\__\  
     |::/  /     \:\/:/  /     \/__/         \:\ \/__/  
     /:/  /       \::/  /                     \:\__\    
     \/__/         \/__/                       \/__/   
''')

print(r'''
    [*]“mk note" mains make note
    [*]“ov note" mains over note
    [*]“lk" mains look noteswhile 1:
    [*]“exit" mains quite
''')


while 1:
  a=input('>>')
  if a=='lk':
    xiaoshuaib = pd.read_csv('xsb.csv')
    print(xiaoshuaib)
    
  elif 'mk' in a:
    new_a = a.replace('mk','')
    df = pd.read_csv('xsb.csv')
    new_data = pd.DataFrame({'note':[ new_a],'statue':['待办']})
    df = df.append(new_data)
    df.to_csv('xsb.csv', index=False)
    print('Ok to make note')
    
  elif a=='exit':
    print('Bye')
    break

  elif 'ov' in a:
    df = pd.read_csv('xsb.csv')
    line = [int(num) for num in re.findall(r'\d+', a)]
    df = df.drop(line)
    df.to_csv('xsb.csv', index=False)
    print('Over to removed note')

  else:
    print(f'No model name “{a}“')
  
    
  
  
