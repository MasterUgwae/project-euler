from types import NoneType


class bestHand:
    ranks=["High","Pair","Two Pair","Three of a Kind","Straight", "Flush","Full House","Four of a Kind","Straight Flush"]
    cards=["2",'3','4','5','6','7','8','9','T','J','Q','K','A']
    def __init__(self,name:str,val:str) -> None:
        self.name = name
        self.val = val

    def reassign(self,newName:str|NoneType = None,newVal:str|NoneType = None)->None:
        if newName:
            self.name=newName
        if newVal:
            self.val=newVal

    def __eq__(self, value: object) -> bool:
        if isinstance(value,bestHand):
            if self.name==value.name and self.val==value.val:
                return True
        return False
    
    def __lt__(self, value: object) -> bool:
        if isinstance(value,bestHand):
            if bestHand.ranks.index(self.name)<bestHand.ranks.index(value.name):
                return True
            elif bestHand.ranks.index(self.name)>bestHand.ranks.index(value.name):
                return False
            else:
                match self.name:
                    case "High"|"Pair"|"Three of a Kind"|"Straight"|"Straight Flush"|"Two Pair"|"Full House"|"Four of a Kind":
                        return bestHand.cards.index(self.val)<bestHand.cards.index(value.val)
                    case "Flush":
                        return False
        return False


    def __gt__(self, value: object) -> bool:
        if isinstance(value,bestHand):
            if bestHand.ranks.index(self.name)>bestHand.ranks.index(value.name):
                return True
            elif bestHand.ranks.index(self.name)<bestHand.ranks.index(value.name):
                return False
            else:
                match self.name:
                    case "High"|"Pair"|"Three of a Kind"|"Straight"|"Straight Flush"|"Two Pair"|"Full House"|"Four of a Kind":
                        return bestHand.cards.index(self.val)>bestHand.cards.index(value.val)
                    case "Flush":
                        return False
        return False
    def __le__(self, value: object) -> bool:
        if isinstance(value,bestHand):
            if bestHand.ranks.index(self.name)<bestHand.ranks.index(value.name):
                return True
            elif bestHand.ranks.index(self.name)>bestHand.ranks.index(value.name):
                return False
            else:
                match self.name:
                    case "High"|"Pair"|"Three of a Kind"|"Straight"|"Straight Flush"|"Two Pair"|"Full House"|"Four of a Kind":
                        return bestHand.cards.index(self.val)>=bestHand.cards.index(value.val)
                    case "Flush":
                        return True
        return False

    def __ge__(self, value: object) -> bool:
        if isinstance(value,bestHand):
            if bestHand.ranks.index(self.name)>bestHand.ranks.index(value.name):
                return True
            elif bestHand.ranks.index(self.name)<bestHand.ranks.index(value.name):
                return False
            else:
                match self.name:
                    case "High"|"Pair"|"Three of a Kind"|"Straight"|"Straight Flush"|"Two Pair"|"Full House"|"Four of a Kind":
                        return bestHand.cards.index(self.val)>=bestHand.cards.index(value.val)
                    case "Flush":
                        return True
        return False

def find_duplicate(lst)->list[str]: 
    seen = set() 
    duplicates=set()
    for item in lst: 
        if item in seen: 
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

def find_triplicate(lst)->str|NoneType:
    seen = []
    for item in lst:
        if item in seen:
            if seen.count(item)==2:
                return item
        seen.append(item)
    return None


def find_four_of(lst)->str|NoneType:
    seen = []
    for item in lst:
        if item in seen:
            if seen.count(item)==3:
                return item
        seen.append(item)
    return None

def get_txt_file()->list[str]:
    with open("0054_poker.txt","r") as file:
        poker=file.readlines()
    return poker

def check_winner(hands:str)->int:
    cardRanks:list[str]=["2",'3','4','5','6','7','8','9','T','J','Q','K','A']
    player1=hands.split()[:5]
    player1num=[i[:-1] for i in player1]
    player1suit=[i[-1] for i in player1]
    player2=hands.split()[5:]
    player2num=[i[:-1] for i in player2]
    player2suit=[i[-1] for i in player2]
    

    #Find Highest card
    p1Best=bestHand("High", cardRanks[max(cardRanks.index(i) for i in player1num)])
    
    #check player 1 hand value
    #Check pair
    if max(player1num.count(i) for i in set(player1num))>=2:
        p1Best.reassign("Pair",find_duplicate(player1num)[0])
    #Check Two Pair
    if [player1num.count(i) for i in set(player1num)].count(2)==2:
        p1Best.reassign("Two Pair",max(find_duplicate(player1num)))
    
    #Check Three of a Kind
    if max(player1num.count(i) for i in set(player1num))>=3:
        p1Best.reassign("Three of a Kind",find_triplicate(player1num))

    #Check Straight
    if sorted(player1num)==sorted(list(set(player1num))):
        if sorted([cardRanks.index(i) for i in player1num])==list(range(min([cardRanks.index(i) for i in player1num]),max([cardRanks.index(i) for i in player1num])+1)):
            topCard=cardRanks[max(cardRanks.index(i) for i in player1num)]
            p1Best.reassign("Straight",topCard)

    #Check Flush
    if len(set(player1suit))==1:
        p1Best.reassign("Flush",player1suit[0])

    #Check Full House
    if max(player1num.count(i) for i in set(player1num))>=3:
        if len(set(find_duplicate(player1num)))==2:
            p1Best.reassign("Full House",find_triplicate(player1num))

    #Check Four of a Kind
    if max(player1num.count(i) for i in set(player1num))==4:
        p1Best.reassign("Four of a Kind",find_four_of(player1num))

    #Check Straight Flush
    if len(set(player1suit))==1 and sorted(player1num)==sorted(list(set(player1num))):
        if sorted([cardRanks.index(i) for i in player1num])==list(range(min([cardRanks.index(i) for i in player1num]),max([cardRanks.index(i) for i in player1num])+1)):
            topCard=cardRanks[max(cardRanks.index(i) for i in player1num)]
            p1Best.reassign("Straight Flush",topCard)
    
    #Find Highest card
    p2Best=bestHand("High", cardRanks[max(cardRanks.index(i) for i in player2num)])
    
    #check player 2 hand value
    #Check pair
    if max(player2num.count(i) for i in set(player2num))>=2:
        p2Best.reassign("Pair",find_duplicate(player2num)[0])
    #Check Two Pair
    if [player2num.count(i) for i in set(player2num)].count(2)==2:
        p2Best.reassign("Two Pair",max(find_duplicate(player2num)))
    
    #Check Three of a Kind
    if max(player2num.count(i) for i in set(player2num))>=3:
        p2Best.reassign("Three of a Kind",find_triplicate(player2num))

    #Check Straight
    if sorted(player2num)==sorted(list(set(player2num))):
        if sorted([cardRanks.index(i) for i in player2num])==list(range(min([cardRanks.index(i) for i in player2num]),max([cardRanks.index(i) for i in player2num])+1)):
            topCard=cardRanks[max(cardRanks.index(i) for i in player2num)]
            p2Best.reassign("Straight",topCard)

    #Check Flush
    if len(set(player2suit))==1:
        p2Best.reassign("Flush",player2suit[0])

    #Check Full House
    if max(player2num.count(i) for i in set(player2num))>=3:
        if len(set(find_duplicate(player2num)))==2:
            p2Best.reassign("Full House",find_triplicate(player2num))

    #Check Four of a Kind
    if max(player2num.count(i) for i in set(player2num))==4:
        p2Best.reassign("Four of a Kind",find_four_of(player2num))

    #Check Straight Flush
    if len(set(player2suit))==1 and sorted(player2num)==sorted(list(set(player2num))):
        if sorted([cardRanks.index(i) for i in player2num])==list(range(min([cardRanks.index(i) for i in player2num]),max([cardRanks.index(i) for i in player2num])+1)):
            topCard=cardRanks[max(cardRanks.index(i) for i in player2num)]
            p2Best.reassign("Straight Flush",topCard)

    if p1Best>p2Best:
        return True
    return False



poker=get_txt_file()
count=0
for i in poker:
    if check_winner(i):
        count+=1#
print(count)
