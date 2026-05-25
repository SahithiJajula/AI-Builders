def calculate_score(

security,

bugs,

performance

):

    score=100

    score-=len(

    security

    )*20

    score-=len(

    bugs

    )*10

    score-=len(

    performance

    )*15

    if score<0:

        score=0

    return score
