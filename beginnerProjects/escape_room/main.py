# game object initializer and  class
class GameObject:
    name = ""
    appearace = ""
    feel = ""
    smell = ""
    # the initializer will set up the name,appearance, feel and smell. theres no need to set up the fields beforehand but we will keep them as referance.
    def __init__(self,name,appearace,feel,smell) :
        self.name = name
        self.appearace = appearace
        self.feel = feel
        self.smell = smell
# using formatted strings to use the fields of a given object
    def look(self):
        return f"You look at the {self.name}. {self.appearace}\n"

    def touch(self):
        return f"You touch  the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"


# Room initializer and class
class Room:
    def __init__(self,escape_code,game_objects):
        self.escape_code= escape_code
        self.game_objects= game_objects

    def check_code(self,code):
        return code == self.escape_code

    def get_game_objects(self):
        names=[]
        for object in self.game_objects:
            names.append(object.name)
        return names

# Game initializer and class
class Game:
    def __init__(self):
        self.attempts=0
        objects= self.create_object()
        self.room=Room(375,objects)
    
    def create_object(self):
        return[
            GameObject(
                "Coat",
                "It's Blue and has a small number 3 on the right arm.",
                "It feels leathery and durable.",
                "It smells musky and in need of a wash."),
            GameObject("Knife",
                    "it's sharp and looks to have a bloody edge.",
                    "the metal feels cold, its very sharp, the handle has a 2 etched on it.",
                    "smells like metal and strawberries?"),
            GameObject("Journal",
                    "It looks old, it has a leather cover and theres a few pages missing.",
                    "As you examine it you notice that the last page has a date on it, you can only make out the month. May. ",
                    "it smells like rotting paper and dust."),
            GameObject("Energy drink",
                    "Its an unopened can of energy drink, it says try all of our 7 flavors! on the side.",
                    "It still feels cold and wet, it has been recently placed here.",
                    "It smells fruity, and there is a hint of strawberries."),
            GameObject("Photo",
                    "It looks to be a Photo of a man wearing a Coat writing on a journal under the shade of a tree.",
                    "There is a red stain near the edge, also the back of the photo has the initias C.E.J. written hastily on it.",
                    "The photo has a distinct smell of dust."),
        ]
    
    def take_turn(self):
        prompt= self.get_room_prompt()
        selection=int(input (prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection-1)
            self.take_turn()
        else:
            is_code_correct=self.guess_code(selection)
            if is_code_correct:
                print("You input the right combination and escape!!")
            else:
                if self.attempts == 3:
                    print("The lock makes a clicking noise and it no longer accepts inputs...You Lose.")
                else:
                    print(f"The lock clicks but doesnt open you have used {self.attempts}/3 attempts.\n")
                    self.take_turn()
    
    def get_room_prompt(self):
        prompt= "Try to guess the code or interact with an object:\n(enter the code or choose an object by typing the number)\n"
        names=self.room.get_game_objects()
        index=1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    def select_object(self,index):
        selected_object= self.room.game_objects[index]
        prompt=self.get_object_interaction(selected_object.name)
        interaction=input(prompt)
        clue=self.interct_with_object(selected_object,interaction)
        print(clue)
        return
    
    def get_object_interaction(self,name):
        interact=f"What do you want to do?\n 1.Look at the {name}\n 2.Touch the {name}\n 3.Smell the {name}\n "
        return interact
    
    def interct_with_object(self,object,interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else :
            return object.sniff()
    
    def guess_code(self,code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts+=1
            return False
        
# Game Start
game=Game()
game.take_turn()

