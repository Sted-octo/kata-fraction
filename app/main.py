
def main():
  again = True
  
  while again :
    print("Fraction operation to do ([number]/[number] [+|-|*|/] [number]/[number]) | [q|Q : Quit]:")
    wording = input()
    if wording == "q" or wording == "Q" :
      again = False



if __name__ == "__main__":
  main()