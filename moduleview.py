import importlib
import inspect
import os

flag=1
while(flag==1):
 try: 
  name=input("Enter the module name or path in it:")
  file=open(name+".txt","w+")
  file.write(inspect.getsource(importlib.import_module(name)))
  file.close()
  print("Module saved to "+name+".txt")
  if(input("Press z to quit:")=="z"):
   flag=0
 except:
  print("Enter a valid module present in system or typo or ")
  try:
   mod=input("Enter the module to install:")
   os.system("pip install "+mod)
  except:
   flag=0
   print("Entered module cannot be installed or not valid")
