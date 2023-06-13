def start_game() :
    your_answers = []
    correcr_answers = 0
    question_num = 1



    for key in questions :
        print("\n")
        print(key)
        for i in opptions[question_num -1] :
            print(i)
        question_num += 1
        your_answer =input("enter your answer ? ").upper()
        your_answers.append (your_answer)

        correcr_answers += check_responses(questions.get(key) , your_answer)

    display_score( your_answers , questions )
    print(" \n your score from 100 is : "+str(100*(correcr_answers/(question_num-1))))
   
   

def check_responses(answer , guess) :
   if answer == guess : 
       print( " correct !")
       return 1
   else :
       print(' wrong ')
       return 0
       

def display_score(your,correct ) :
    print("\n")
    print(" result")
    print("\n")
    for i in your :
        print(i , end="  ")
    print("\n")
    for j in correct :
        print(correct.get(j) , end="  ")

    
def again1() :
    start_game()




questions ={
    "who created appele company ?" : "A" ,
    "who created facebook company ?" : "B" ,
    "who created microsoft company ?" : "C" ,
    "who created amazon company ?" : "D" ,
}
opptions = [["A.steve jobs", "B.mark zakerberg" , "bil gates" , 'jef bzos'] ,
["A.steve jobs", "B.mark zakerberg" , "ilan musk" , 'jef bzos'], 
["A.steve jobs", "B.mark zakerberg" , "bil gates" , 'jef bzos'],
["andro tate ", "B.mark zakerberg" , "bil gates" , 'jef bzos'],
]
 
while True :
    start_game()
    yes_no = ['yes', 'no']
    again = None
    while again not in yes_no :
         again =input('do you want to play again ? yes or no    ').lower()
    if again =="yes " :
        continue
    elif again == "no" :
        break
print(" by by ")