def change_color(color, word):
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "purple":
    print("\033[0;35m", word, sep="", end="")
  elif color == "blue":
    print("\033[0;34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")
    
print("Super Function\n")
print("With my ", end="")
change_color("purple", "new program ")
change_color("reset", "I can just call red ")
change_color("red", "and ")
change_color("reset", "that word will appear in the color I set it to.\n")
print()
print("With no ", end="")
change_color("blue", "weird gaps")
change_color("reset", ".")
print()
print()
print("Epic.")
