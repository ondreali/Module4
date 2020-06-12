"""
Program: Coupon Calculation.py
Author:  Ondrea Li
Date: 6/10/20

The purpose of this program is
"""
NUMBER_TEST = 1
def average():
    # Get input for scores
    # declare variables, use score1, score2, score3 in calculation
    return average_scores

score1 = int(input("What is score1?"))
score2 = int(input("What is score2?"))
score3 = int(input("What is score3?"))

def average(score1, score2, score3):
    NUMBER_TESTS = 3
    try:
        if 0<score1<= 100:
           print ("score is within range")
        else:
            print("score needs to be a positive integer")
            raise ValueError
        if 0<score2<= 100:
            print("score is within range")
        else:
            print("score needs to be a positive integer")
            raise ValueError
        if 0<score3<= 100:
            print("score is within range")
        else:
            print("score needs to be a positive integer")
            raise ValueError
    except:
        print("score not convert")
        raise ValueError

    return float((score1 + score2 + score3)/NUMBER_TESTS)


average_score = average(score1, score2, score3)
print(average_score)

if __name__ == '__main__':
    pass
