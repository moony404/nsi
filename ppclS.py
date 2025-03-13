from random import randint
pierre=1
papier=2
ciseaux=3
lezard=4
spock=5
random_number=randint(1,5)
def text():
    print("\n##################\n🏆Vous avez gagné🏆\n##################\n")
def check(user_input):
    if user_input==pierre and (random_number==lezard or random_number==ciseaux):
        text()
    if user_input==ciseaux and (random_number==papier or random_number==lezard):
        text()       
    if user_input==lezard and (random_number==spock or random_number==papier):
        text()
    if user_input==papier and (random_number==pierre or random_number==spock):
        text()
    if user_input==spock and (random_number==ciseaux or random_number==pierre):
        text()
    else:
        print("Vous avez perdu !!")
user_input=int(input("Choisissez : "))
check(user_input)