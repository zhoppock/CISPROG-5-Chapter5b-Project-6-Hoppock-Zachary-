def decimalToRep(value, base):
  table = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
  result = ""

  value = int(value)

  while value > 0:
    result += table[value % base]
    value = value // base

  result = result[::-1]
  
  return result

def main():
  value = input("Enter a numerical value: ")
  base = int(input("Enter a base for the value: "))
  print("Function returned", decimalToRep(value, base))
  print(decimalToRep("10", 8))
  print(decimalToRep("5", 16))
  print(decimalToRep("10", 2))
  print(decimalToRep("15", 8))
