import random

def add_quote(write_to_file):
  user_prompt = input("Add new quote? (Y/N) ")

  if user_prompt in ('Y','Yes','yes','YES'):  
    with open(write_to_file,mode = 'a') as f:
      new_quote = input("Add a new quote: ")
      f.write(new_quote)
  else:
    return

def primary(uf):
  print("Keep it logically awesome.")

  with open(uf,mode = 'r') as f:
    quotes = f.readlines()
    last = len(quotes)-1
    rnd = random.randint(0,last)
    return print(quotes[rnd])
 

if __name__== "__main__":
  uf = str(input('File name: '))
  add_quote(uf)
  
  uq_no = int(input("Number of quotes to display: "))

  while uq_no > 0:
    primary(uf)
    uq_no -= 1