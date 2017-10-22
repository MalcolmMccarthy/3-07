#made by malcolm mccarthy
#in october 2017
#for loop practice

import ui

def factortial_button(sender):
	# calculates factorial
 input = int(view['integer_textfield'].text)
 counter = 1
 answer = 1
 for i in range(1, 20):
        if counter <= input: 
            answer = answer * counter
            counter = counter + 1
            view['answer_label'].text = "{}".format(answer)
    

view = ui.load_view()
view.present('sheet')
