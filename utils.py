optinal_suites =["H","C","D","S"]
def create_card(rank:str, suite:str) -> dict:
    ranks={"2":2,
           "3":3,
           "4":4,
           "5":5,
           "6":6,
           "7":7,
           "8":8,
           "9":9,
           "10":10,
           "J":11,
           "Q":12,
           "K":13,
           "A":14}
    if(rank not in ranks and suite not in optinal_suites):
        return None
    
    return{
        "rank":rank,
        "suite":suite,
        "value":ranks[rank]
    }
def compare_cards(p1_card: dict, p2_card: dict) -> str:
    p1_value=p1_card["value"]
    p2_value=p2_card["value"]
    if(p1_value>p2_value):
        return "p1"
    elif(p1_value<p2_value):
        return "p2"
    
    return "WAR"
