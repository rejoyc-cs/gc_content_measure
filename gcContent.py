def gcContent(DNA):
  n = len(DNA)
  count = 0
  for i in range(n):
    if DNA[i] == 'G' or DNA[i] == 'C':
      count = count+1
  
  return count/n

def main():
  #You may uncomment this section and directly put the DNA string

  #DNA = "" #Here put the string

  #Or you can take the string as Input
  DNA = input("Enter the DNA string ")

  print("GC Content in DNA is: ",gcContent(DNA))

if __name__ == '__main__':
  main()
