ls=[1,2,3,4,5,6,7,8,9]
XOls=['X','O']
players=[]
selected=[]
def printable():
    x=0
    while x<len(ls):
        if x%3==0:
            print()
        print(ls[x]," ",end="")
        x+=1
print("-----------------------Welcome to XOXO game---------------------------------")
player1=input("Enter the first player")
player2=input("Enter the second player")
players.extend([player1,player2])
player1choice=XOls[0]
player2choice=XOls[1]
print()
print(players[0],"Your character is:",player1choice)
print(players[1],"Your character is:",player2choice)
count=0
player_index=0
while True:
    print("\n\nPlease play your turn:",players[player_index])
    Box=int(input("Enter box number"))
    if Box in selected:
        print("This Box is already filled")
    elif len(selected)<8:
        selected.append(Box)
        ls[(Box-1)]=XOls[player_index]
        printable()
        if ls[0]==ls[1]==ls[2]=="X" or ls[3]==ls[4]==ls[5]=="X" or ls[6]==ls[7]==ls[8]=="X" or ls[0]==ls[3]==ls[6]=="X" or ls[0]==ls[4]==ls[8]=="X" or ls[2]==ls[4]==ls[6]=="X":
            print()
            print(players[0],"Win the match")
            break
        elif ls[0]==ls[1]==ls[2]=="O" or ls[3]==ls[4]==ls[5]=="O" or ls[6]==ls[7]==ls[8]=="O" or ls[0]==ls[3]==ls[6]=="O" or ls[0]==ls[4]==ls[8]=="O" or ls[2]==ls[4]==ls[6]=="O":
            print()
            print(players[1],"Win the match")
            break
        player_index+=1
    count+=1
    if player_index>1:
        player_index=0