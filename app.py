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

def traverse_tree(node):
    if node.question:
        response = input(node.question + " (y/n): ")
        if response.lower() == 'y':
            traverse_tree(node.yes_node)
        else:
            traverse_tree(node.no_node)
    else:
        print(f"I guess your friend is {node.guess}.")

def save_tree(tree, filename):
    with open(filename, 'wb') as file:
        pickle.dump(tree, file)

def load_tree(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    friend_tree = build_tree()
    print("Welcome to the Friend Guessing Game!")
    time.sleep(1)
    print("Think of a friend, and I will try to guess who it is.")
    time.sleep(1)

    traverse_tree(friend_tree)

    # Save the tree
    save_tree(friend_tree, 'friend_tree.pkl')

    # Load the tree
    loaded_tree = load_tree('friend_tree.pkl')

    # You can use the loaded_tree as needed
    traverse_tree(loaded_tree)
