import pickle
import time

class Node:
    def __init__(self, question=None, yes_node=None, no_node=None, guess=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.guess = guess

def build_tree():
    root = Node("Is your friend a male?", 
                    yes_node=Node("Is your friend from MCA", 
                                    yes_node=Node("Does Your Friend Own a Company", 
                                                guess="Rijfas",
                                                no_node=Node("Has Your Friend got selected in IIM",
                                                guess="Pranav")), 
                                    no_node=Node("Is your friend from CS?", 
                                                yes_node=Node("Does Your Friend sneeze a lot?", 
                                                                yes_node=Node(guess="Rishin"),
                                                no_node=Node("Has he stayed abroad",
                                                yes_node=Node("Is your friend a fan of kannada movies?",
                                                              yes_node=Node(guess="Sooraj Mathew"),
                                                              no_node=Node("Is your friend Single?",
                                                                           yes_node=Node(guess="Siddarth Sajeev"),
                                                                           no_node=Node("Is your friend Vegetarian",
                                                                                         yes_node=Node(guess="Harikrishnan")))))),
                                                ),
                    ),
                    no_node=Node("Is Your fiend from MCA",
                                    yes_node=Node("Is Your friend a rank holder",
                                                    yes_node=Node(guess="Sarika"),
                                                    no_node=Node("Does she wear glasses",
                                                                    yes_node=Node(guess="Rifana")
                                                                )
                                                ),
                                    
                                    no_node=Node("IS your friend talkative?",
                                                    yes_node=Node("is she assosciated with IEEE",
                                                               yes_node=Node(guess="Gayathri"),
                                                               no_node=Node("is she from palakkad",
                                                                           yes_node=Node(guess="Sarika")
                                                                           )
                                                                ),
                                                    no_node=Node("Does She wear glasses",
                                                                 yes_node=Node(guess="Sandra")
                                                                 )
                                                )
                                )
        )

    return root

def traverse_tree(node, prev=None):
    if node is None:
        print("I couldn't guess your friend. Please provide more information.")
        new_friend = input("Enter the name of your friend: ")
        new_question = input(f"Provide a yes/no question that distinguishes {new_friend} from the previous friend: ")
        response = input(f"For {new_friend}, what would the answer be to the question: {new_question} (y/n): ")

        if response.lower() == 'y':
            new_node = Node(new_question,yes_node=Node(guess=new_friend))
        else:
            new_node = Node(new_question,no_node=Node(guess=new_friend))

        if prev:
            prev.no_node = new_node
        else:
            return new_node

        print(f"Thanks for teaching me about {new_friend}!")

        # Save the updated tree
        save_tree(node, 'friend_tree.pkl')
        return

    if node.question:
        response = input(node.question + " (y/n): ")
        if response.lower() == 'y':
            traverse_tree(node.yes_node, node)
        else:
            traverse_tree(node.no_node, node)
    else:
        response = input(f"Is your friend {node.guess}? (y/n): ")
        if response.lower() == 'y':
            print(f"I guessed correctly! Your friend is {node.guess}.")
        else:
            print("I couldn't guess your friend. Please provide more information.")


def save_tree(tree, filename):
    with open(filename, 'wb') as file:
        pickle.dump(tree, file)

def load_tree(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

import os
def main():
    filename = 'friend_tree.pkl'
    
    if os.path.exists(filename):
        loaded_tree = load_tree(filename)
        print("Loaded existing friend tree.")
    else:
        loaded_tree = build_tree()
        print("No existing friend tree found. Created a new one.")

    print("Welcome to the Friend Guessing Game!")
    time.sleep(1)
    print("Think of a friend, and I will try to guess who it is.")
    time.sleep(1)

    traverse_tree(loaded_tree)

    # Save the updated tree
    save_tree(loaded_tree, filename)

if __name__ == "__main__":
    main()
