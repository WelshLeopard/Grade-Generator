# Grade Generator
# ask student for name of test
#test_name = input("What is the name of the test? ")
# max score they could recive
max_score = int(input("What is th max score of the test? "))
# how many point they think recive
student_score = int(input("What is your score? "))

#print out the score of the test "You got score% in the test"

ans = round((student_score / max_score) * 100, 2)

if ans >= 0 and ans <= 50:
  print(ans)
  print("You got a 'U'. try harder!")
elif ans > 50 and ans <= 59:
  print(ans)
  print("You got a 'D', it's a pass")
elif ans >= 60 and ans <= 69:
  print(ans)
  print ("You got a 'C', very middle of the road.")
elif ans >= 70 and ans >=79:
  print(ans)
  print("You got a 'B', slightly above avarage'")
elif ans >= 80 and ans >=79:
  print(ans)
  print("You got a 'A', noice")
elif ans >= 90 and ans <= 100:
  print(ans)
  print("You got a 'A+', get the big brain on you")
