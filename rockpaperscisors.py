choice1=input("WELCOME TO ROCK PAPER SCISSORS, CHOOSE 0 FOR ROCK , CHOOSE 1 FOR PAPER, CHOOSE 2 FOR SCISSORS: ")
if choice1=="0":
    print(r"""YOUR CHOICE
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice1=="1":
    print(r"""YOUR CHOICE
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:
    print(r"""YOUR CHOICE
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
comp1=random.randint(0,2)
if comp1==0:
    print(r"""THE COMPUTERS CHOICE
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif comp1==1:
    print(r"""THE COMPUTERS CHOICE
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:
    print(r"""THE COMPUTERS CHOICE
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if choice1==comp1:
    print("   ITS A TIE")
elif choice1=="0" and comp1==2:
    print("HUMAN WINS")
elif choice1=="1" and comp1==0:
    print("HUMAN WINS")
elif choice1=="2" and comp1==1:
    print("HUMAN WINS")
else:
    print("COMPUTER WINS")
