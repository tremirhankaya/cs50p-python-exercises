import random


def main():
    score=0
    level=get_level()
    for i in range(10):
        false_count=0
        numbers=(generate_integer(level), generate_integer(level))
        while false_count<3:
            user_answer=input(f"{numbers[0]} + {numbers[1]} = ")
            if not user_answer.isdigit():
                print("EEE")
                false_count+=1
                continue
            user_answer=int(user_answer)
            if user_answer==numbers[0]+numbers[1]:
                score+=1
                break
            else:
                print("EEE")
                false_count+=1
       
        if false_count==3:
            print(f"{numbers[0]} + {numbers[1]} = {numbers[0]+numbers[1]}")
        
    print(f"Score: {score}")    


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
