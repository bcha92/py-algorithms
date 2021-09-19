# Make Bricks - Python Edition
def make_bricks(small, big, goal):
    small = small * 1;
    bigc = big;
    big = big * 5;
    if goal == small + big:
        return True
    elif bigc >= goal / 5 and small >= goal % 5:
        return True
    elif bigc < goal / 5 and small > (goal - big):
        return True
    else:
        return False

make_bricks(3, 4, 6)