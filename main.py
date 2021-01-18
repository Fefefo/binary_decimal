from colorama import Fore


def b_to_d(s) -> (int, int):
  out1, out2 = 0, 1
  for i in range(len(s)):
    out1 += int(s[i]) * (pow(2, (len(s)-i)-1))
    s[i] = not bool(int(s[i]))
    out2 += int(s[i]) * (pow(2, (len(s)-i)-1))
  return out1, -out2

def d_to_b(n) -> (str, int):
  out = ""
  o2 = 0
  n1 = n
  while int(n/2) != 0 or n % 2 != 0:
    out = str(n%2) + out
    n = int(n/2)
  while (len(out)%8 != 0):
    out = "0" + out
  out = list(out)
  if n1 <= 0:
    o2 = 1
    for i in range(len(out)):
      out[i] = str(int(not bool(int(out[i]))))
    temp = 1
    for i in range(len(out)):
      j = len(out) - i - 1

      if int(out[j]) == 1 and temp == 1:
        out[j] = str(0)

      elif int(out[j]) == 0 and temp == 1:
        out[j] = str(1)
        temp = 0
        break

      else:
        break

  out = ''.join(out)
  return out, o2

def check_int(s) -> bool:
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

# o1, o2 = d_to_b(x2) if x1 == "1" else (b_to_d(x2) if x1 == "2" else 0, 1)
while True:
  x1, x2 = 0, 'a'
  print(f"{Fore.MAGENTA}Do you want to enter a base 10 or base 2 number?{Fore.RESET}")
  while x1 != "10" and x1 != "2":
    x1 = input()
    if x1 != "10" and x1 != "2":
      print(f"{Fore.RED}'{x1}' is not '10' or '2'{Fore.RESET}")

  print(f"{Fore.MAGENTA}What is the number?{Fore.RESET}")
  while x2 == "" or not check_int(x2):
    x2 = input()
    if x2 != "" and check_int(x2):
      if x1 == "10":
        o1, o2 = d_to_b(int(x2))
        print(f"\n{Fore.BLUE}Binary number ={Fore.GREEN}" if o2 == 0 else f"\n{Fore.BLUE}Binary signed 2's complement ={Fore.GREEN}", o1, Fore.RESET, "\n")
      elif x1 == "2":
        if x2.startswith("-"):
          print(f"{Fore.RED}A binary number can't start with '-'{Fore.RESET}")
          continue
        if x2.count("1") + x2.count("0") != len(x2):
          print(f"{Fore.RED}'{x2}' is not binary number, enter a binary number{Fore.RESET}")
          continue
        o1, o2 = b_to_d(list(x2))
        print(f"\n{Fore.BLUE}Decimal number = {Fore.GREEN}{o1}{Fore.BLUE}\nDecimal from signed 2's complement = {Fore.GREEN}{o2}{Fore.RESET}", "\n")
    else:
      print(f"{Fore.RED}'{x2}' is not a number, enter a number{Fore.RESET}")