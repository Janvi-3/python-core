''' Flash Card using python
    1. Add flash card
    2. View all flash card
    3. quiz flashcard
    4. exit 
    5. main fuction 
'''

import json 
import os
import random

FLASH_CARD_PATH=r"C:\Users\Dell\OneDrive\Desktop\python project\Flash_Card\flash_card.json"

def load_flashcards():
        if os.path.exists(FLASH_CARD_PATH):
            try:
                with open(FLASH_CARD_PATH,'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return[]
        else:
              return[]
        
def save_flashcards(flashcards):
    with open(FLASH_CARD_PATH,'w')as f:
        json.dump(flashcards,f,indent=4)
        
def add_flashcards(flashcards):
    print(" Add New FlashCard ")
    question =input("Enter your question  ")
    while not question :
        print("question cannot be empty ")
        question=input("Enter Your question ")


    answer=input("Enter your answer ")
    while not answer:
        print("answer cannot be empty /n " )
        answer=input("Enter your answer ")

    flashcards.append({"question ": question ,
                        "answer ": answer })
    save_flashcards(flashcards)
    print("\n  FlashCard added successfully ")

def view_flashcards(flashcards):
    print("\n  View all flashcard")
    if not flashcards:
        print("\n  You haven't add any  flashcard ! \n  ")
        return 
    
    for i, card in enumerate(flashcards,1):
        print(f"\n card{i}:")
        print(f"Question :{card['question']}")
        print(f"Answer :{card['answer']}")
        print()

def quiz_flashcards(flashcards):
    if not flashcards:
        print(" No flashcards to quiz . Please add some flashcards\n ")
        return 
    
    print("--->flashcards Quiz<---\n ")
    print("Type 'exit ' at any time to stop the quiz \n ")

    while True:
        card=random.choice(flashcards)
        user_answer=input(f"Question:{card['question']} \n Your answer")
        
        if user_answer.lower()=="exit":
            print("\n Quiz ended \n ")
            break

        print(f" correct answer: {card['answer']}")
        print("-----------------------------------------------")


def main():
    flashcards=load_flashcards()

    while True:
        print("\n====> FLASHCARD PROGRAM <====")
        print(" 1. ADD FLASHCARD  ")
        print(" 2. VIEW ALL FLASHCARDS  ")
        print(" 3. QUIZ FLASHCARDS  ")
        print(" 4. EXIT   ")

        choice=input("ENTER YOUR CHOICE (1-4) :")

        if choice=="1":
            add_flashcards(flashcards)
        elif choice=="2":
            view_flashcards(flashcards)
        elif choice=="3":
            quiz_flashcards(flashcards)
        elif choice=="4":
            print("\n GoodBye Your Flashcard has been saved. ")
            break
        else:
            print(" Invalid Choice ! PLease Enter valid choice (1-4): ")


if __name__ == "__main__":
    main()

