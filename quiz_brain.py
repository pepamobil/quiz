class QuizBrain:
    def __init__(self, all_object_list):
        self.all_objects = all_object_list
        self.obj_count = 0
        self.right_count = 0

    def still_question(self):
        if self.obj_count < len(self.all_objects):
            return True
        else:
            return False
        
    def next_question(self):
        print(f"Otázka č. {self.obj_count +1}: {self.all_objects[self.obj_count].ques}\nA = ano, N = ne ")
        

    def right_question(self):
        player = input().lower()
        if player == "a":
            player = "Ano"
        else:
            player = "Ne"
        if self.all_objects[self.obj_count].answ == player:
            print("SPRÁVNĚ !")
            self.right_count += 1
        else:
            print("ŠPATNĚ...")
        print(f"Skore správných odpovědí: {self.right_count}/ {self.obj_count +1}")
        self.obj_count += 1