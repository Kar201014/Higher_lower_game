from game_data import data
import random 



def hopar():
    y = True
    while y:
        correct_count = 0                
        chosen_account1 = random.choice(data)
        chosen_account2 = random.choice(data)
        if chosen_account1 == chosen_account2:
           chosen_account2 = random.choic(data)
        x = input("a or b").lower()
        a = chosen_account1
        b = chosen_account2
        
        if a["follower_count"] > b["follower_count"]:
           if x == "a":
               correct_count += 1
               print(f"correct_count {a}, {correct_count}")                        
           else:
                print(f"correct_count{b}, {correct_count}")
                y = False
        elif b["follower_count"] > a["follower_count"]:
            if x == "b":                
               correct_count += 1
               print(f"correct_count {a}, {correct_count}")     
       
       
def format(accont):
    name = accont["name"]
    description = accont["description"]
    countri = accont["countri"]
    print(f"{name} is {description} from {countri}")
    
    
hopar()
    