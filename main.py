from turtle import *

C: tuple[str, str, str, str, str, str, str] = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
BG_COLOURS: tuple = ('white', 'white smoke', 'gainsbro', 'light gray', 'silver', 'dark gray', 'gray', 'dim gray', 'black',
'light slate gray', 'slate gray', 'alice blue', 'light steel blue', 'cornflower blue', 'royal blue', 'blue', 'medium blue', 'navy', 'dark blue', 'midnight blue',
'light blue', 'deep sky blue', 'dodger blue', 'powder blue', 'sky blue', 'light sky blue', 'steel blue', 'azure', 'light cyan', 'cyan',
'pale turquoise', 'dark turquoise', 'turquoise', 'meduim turquoise', 'light sea green', 'cadet blue', 'dark cyan', 'teal', 'dark slate gray',
'mint cream', 'aquamarine', 'medium aquamarine', 'dark sea green', 'medium sea green', 'sea green', 'honedew', 'pale green', 'light green',
'medium spring green', 'spring green', 'lime green', 'green', 'forest green', 'dark green', 'green yellow', 'chartreuse', 'lawn green',
'lime', 'yellow green', 'olive drab', 'beige', 'dark khaki', 'olive', 'dark olive green', 'pale goldenrod', 'khaki', 'ivory', 'light yellow',
'light goldenrod yellow', 'cornsilk', 'lemon chiffon', 'yellow', 'gold', 'goldenrod', 'dark goldenrod', 'wheat', 'tan', 'burlywood', 'peru',
'sienna', 'saddle brown', 'floral white', 'old lace', 'navajo white', 'moccasin', 'sandy brown', 'orange', 'dark orange', 'chocolate',
'firebrick', 'brown', 'dark red', 'maroon', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'light salmon',
'coral', 'tomato', 'orange red', 'red', 'crimson', 'dark salmon', 'salmon', 'light coral', 'indian red', 'rosy brown', 'linen', 'seashell',
'misty rose', 'pink', 'light pink', 'hot pink', 'deep pink', 'snow', 'lavender blush', 'pale violet red', 'violet red', 'medium violet red',
'purple', 'dark magenta', 'violet', 'magenta', 'thistle', 'plum', 'orchid', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
'medium purple', 'rebecca purple', 'indigo', 'ghost white', 'lavender', 'light slate blue', 'medium slate blue', 'slate blue', 'dark slate blue'
)
YES: set[str] = {'yes', '', 'y'}
NO: set[str] = {'no', 'n'}


def is_str_yes_or_no(true_cond: set[str], false_cond: set[str], input_str: str) -> bool:
	while True:
		inputs: str = input(input_str)
		if inputs.lower() not in true_cond.union(false_cond):
			continue
		return True if inputs in true_cond else False
  

def does_str_fit_condition(true_cond: set[str] | tuple, input_str: str) -> str:
	while True:
		inputs = input(input_str)
		if inputs.lower() not in true_cond:
			continue
		return inputs
  

def check_cond_int(input_str: str) -> int:
	while True:
		inputs: str = input(input_str) 
		if inputs.isdigit():
			return int(inputs)
	   

def check_cond_float(input_str: str) -> float:
	while True:
		try:
			inputs: str = input(input_str) 
			return float(inputs)
		except ValueError:
			continue
		

c_select: int = 0
speed(check_cond_int('Speed (0 = No animations, 1 = slowest, 10 = fastest with animations): '))
colour_debug: bool = is_str_yes_or_no(YES, NO, 'Colour debug? (Y/n): ')
hide_turtle: bool = is_str_yes_or_no(YES, NO, 'Hide turtle? (Y/n): ')
max_iteration: int = check_cond_int('Max iteration: ')
pattern_debug: bool = is_str_yes_or_no(YES, NO, 'Pattern debug on? (Y/n): ')
spacing: float = check_cond_float('Spacing (Sensitive): ')
set_angle: int = check_cond_int('Angle (u should have learned this by now): ')
start_pos_x: int = check_cond_int('Starting position (x): ')
start_pos_y: int = check_cond_int('Starting position (y): ')

background_colour: str = does_str_fit_condition(BG_COLOURS, f'Background colour (Here are all the colours: {", ".join(BG_COLOURS)}): ')

rainbow_mode: bool = is_str_yes_or_no(YES, NO, 'RAINBOW MODE?!! (Y/n): ')

if rainbow_mode == False:
	colour: str = does_str_fit_condition(BG_COLOURS, f'Colour (Here are all the colours: {", ".join(BG_COLOURS)}): ')
	bgcolor(background_colour)
	color(colour)

penup()
goto(start_pos_x, start_pos_y)
pendown()

if hide_turtle == True:
	hideturtle()

for n in range(max_iteration):
	forward(n * spacing)
	left(set_angle)
	if colour_debug == True:
		print(f'Colour = {C}')
		print(f'Colour pointer = Pointing to: {c_select}')
	if pattern_debug == True:
		print(f'Iteration = MAX_ITERATION: {max_iteration}, CURRENT_ITERATION: {n}, RAINBOW_MODE: {rainbow_mode}, COLOUR_DEBUG: {colour_debug}, PATTERN_DEBUG: {pattern_debug}, HIDE TURTLE: {hide_turtle}, SPACING: {spacing}, SET_ANGLE: {set_angle}')
print('dun')
terminate: bool = is_str_yes_or_no(YES, NO, 'Exit? (Y/n): ')
if terminate == True:
	quit()
bgcolor(background_colour)

for i in range(max_iteration):
	forward(i * spacing)
	left(set_angle)
	color(C[c_select])
	if rainbow_mode == True: #If you changed the booleen variable 'multi_colour' to 'False', it will select the first string on the list 'c'
		for x in range(6):
			c_select += 1
			if c_select == 6: c_select = -1
	if colour_debug == True:
		print(f'Colour = {C}')
		print(f'Colour pointer = Pointing to: {c_select}')
	if pattern_debug == True:
		print(f'Iteration = MAX_ITERATION: {max_iteration}, CURRENT_ITERATION: {i}, RAINBOW_MODE: {rainbow_mode}, COLOUR_DEBUG: {colour_debug}, PATTERN_DEBUG: {pattern_debug}, HIDE TURTLE: {hide_turtle}, SPACING: {spacing}, SET_ANGLE: {set_angle}')

print('dun')
terminate: bool = is_str_yes_or_no(YES, NO, 'Exit? (Y/n): ')
if terminate == True:
	quit()
