# _________________________________________
#|                                         |
#|     Created by Idiot Industries© LLC    |
#|     2024-2025 Justin Ho                 |
#|                                         |
#|_________________________________________|

from turtle import *

def check_cond_str(true_cond, false_cond, input_str):
  while True:
    inputs = input(input_str)
    if inputs.lower() not in true_cond.union(false_cond):
      continue
    return True if inputs in true_cond else False
def check_cond_str_out(true_cond, input_str):
  while True:
    inputs = input(input_str)
    if inputs.lower() not in true_cond:
      continue
    return inputs
def check_cond_int(input_str1):
  while True:
    try:
      inputs_int = int(input(input_str1))
    except:
      continue
    return inputs_int
def check_cond_float(input_str2):
  while True:
    try:
      inputs_float = float(input(input_str2))
    except:
      continue
    return inputs_float


c = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
c_select = 0
speed(check_cond_int('Speed (0 = No animations, 1 = slowest, 10 = fastest with animations): '))
colour_debug = check_cond_str({'yes', '', 'y'}, {'no', 'n'}, 'Colour debug? (Y/n): ')
pattern_debug = check_cond_str({'yes', '', 'y'}, {'no', 'n'}, 'Pattern_debug? (Y/n): ')
hide_turtle = check_cond_str({'yes', '', 'y'}, {'no', 'n'}, 'Hide turtle? (Y/n): ')
max_iteration = check_cond_int('Max iteration: ')
pattern_debug = check_cond_str({'yes', '', 'y'}, {'no', 'n'}, 'Pattern debug on? (Y/n): ')
spacing = check_cond_float('Spacing (Sensitive): ')
set_angle = check_cond_int('Angle (u should have learned this by now): ')
start_pos_x = check_cond_int('Starting position (x): ')
start_pos_y = check_cond_int('Starting position (y): ')
penup()
goto(start_pos_x, start_pos_y)
pendown()
background_colour = check_cond_str_out({'white', 'white smoke', 'gainsbro', 'light gray', 'silver', 'dark gray', 'gray', 'dim gray', 'black',
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
}, 'Background colour (Here are all the colours: White, White Smoke, Gainsbro, Light Gray, Silver, Dark Gray, Gray, Dim Gray, Black, Light Slate Gray, Slate Gray, Alice Blue, Light Steel Blue, Cornflower Blue, Royal Blue, Blue, Medium Blue, Navy, Dark Blue, Midnight Blue, Light Blue, Deep Sky Blue, Dodger Blue, Powder Blue, Sky Blue, Light Sky Blue, Steel Blue, Azure, Light Cyan, Cyan, Pale Turquoise, Dark Turquoise, Turquoise, Meduim Turquoise, Light Sea Green, Cadet Blue, Dark Cyan, Teal, Dark Slate Gray, Mint Cream, Aquamarine, Medium Aquamarine, Dark Sea Green, Medium Sea Green, Sea Green, Honedew, Pale Green, Light Green, Medium Spring Green, Spring Green, Lime Green, green, Forest Green, Dark Green, Green Yellow, Chartreuse, Lawn Green, Lime, Yellow Green, Olive Drab, Beige, Dark Khaki, Olive, Dark Olive Green, Pale Goldenrod, Khaki, Ivory, Light Yellow, Light Goldenrod Yellow, Cornsilk, Lemon Chiffon, Yellow, Gold, Goldenrod, Dark Goldenrod, Wheat, Tan, Burlywood, Peru, Sienna, Saddle Brown, Floral White, Old Lace, Navajo White, Moccasin, Sandy Brown, Orange, Dark Orange, Chocolate, Firebrick, Brown, Dark Red, Maroon, Antique White, Papaya Whip, Blanched Almond, Bisque, Peach Puff, Light Salmon, Coral, Tomato, Orange Red, Red, Crimson, Dark Salmon, Salmon, Light Coral, Indian Red, Rosy Brown, Linen, Seashell, Misty Rose, Pink, Light Pink, Hot Pink, Deep Pink, Snow, Lavender Blush, Pale Violet Red, Violet Red, Medium Violet Red, Purple, Dark Magenta, Violet, Magenta, Thistle, Plum, Orchid, Medium Orchid, Dark Orchid, Dark Violet, Blue Violet, Medium Purple, Rebecca Purple, Indigo, Ghost White, Lavender, Light Slate Blue, Medium Slate Blue, Slate Blue, Dark Slate Blue): ')
rainbow_mode = check_cond_str({'yes', '', 'y'}, {'no', 'n'}, 'RAINBOW MODE?!! (Y/n): ')
if hide_turtle == True:
  hideturtle()
else:
  pass
if rainbow_mode == False:
  colour = check_cond_str_out({'white', 'white smoke', 'gainsbro', 'light gray', 'silver', 'dark gray', 'gray', 'dim gray', 'black',
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
  }, 'Colour (Here are all the colours: White, White Smoke, Gainsbro, Light Gray, Silver, Dark Gray, Gray, Dim Gray, Black, Light Slate Gray, Slate Gray, Alice Blue, Light Steel Blue, Cornflower Blue, Royal Blue, Blue, Medium Blue, Navy, Dark Blue, Midnight Blue, Light Blue, Deep Sky Blue, Dodger Blue, Powder Blue, Sky Blue, Light Sky Blue, Steel Blue, Azure, Light Cyan, Cyan, Pale Turquoise, Dark Turquoise, Turquoise, Meduim Turquoise, Light Sea Green, Cadet Blue, Dark Cyan, Teal, Dark Slate Gray, Mint Cream, Aquamarine, Medium Aquamarine, Dark Sea Green, Medium Sea Green, Sea Green, Honedew, Pale Green, Light Green, Medium Spring Green, Spring Green, Lime Green, green, Forest Green, Dark Green, Green Yellow, Chartreuse, Lawn Green, Lime, Yellow Green, Olive Drab, Beige, Dark Khaki, Olive, Dark Olive Green, Pale Goldenrod, Khaki, Ivory, Light Yellow, Light Goldenrod Yellow, Cornsilk, Lemon Chiffon, Yellow, Gold, Goldenrod, Dark Goldenrod, Wheat, Tan, Burlywood, Peru, Sienna, Saddle Brown, Floral White, Old Lace, Navajo White, Moccasin, Sandy Brown, Orange, Dark Orange, Chocolate, Firebrick, Brown, Dark Red, Maroon, Antique White, Papaya Whip, Blanched Almond, Bisque, Peach Puff, Light Salmon, Coral, Tomato, Orange Red, Red, Crimson, Dark Salmon, Salmon, Light Coral, Indian Red, Rosy Brown, Linen, Seashell, Misty Rose, Pink, Light Pink, Hot Pink, Deep Pink, Snow, Lavender Blush, Pale Violet Red, Violet Red, Medium Violet Red, Purple, Dark Magenta, Violet, Magenta, Thistle, Plum, Orchid, Medium Orchid, Dark Orchid, Dark Violet, Blue Violet, Medium Purple, Rebecca Purple, Indigo, Ghost White, Lavender, Light Slate Blue, Medium Slate Blue, Slate Blue, Dark Slate Blue): ')
  bgcolor(background_colour)
  color(colour)
  for n in range(max_iteration):
    forward(n *spacing)
    left(set_angle)
    if colour_debug == True:
      print('Colour = ' + str(c))
      print('Colour pointer = ' + 'Pointing to:' + str(c_select))
    if pattern_debug == True:
      print('Iteration = ' + 'MAX_ITERATION: ' + str(max_iteration) + ', CURRENT_ITERATION: ' + str(n) + ', RAINBOW_MODE: ' + str(rainbow_mode) + ', COLOUR_DEBUG: '+ str(colour_debug) + ', PATTERN_DEBUG: '+ str(pattern_debug) + ', HIDE TURTLE: ' + str(hide_turtle) + ', SPACING: ' + str(spacing) + ', SET_ANGLE: ' + str(set_angle))
  print('dun')
  terminate = check_cond_str({'exit', ''}, {''}, 'Exit? (Type Exit to terminate, not case sensitive): ')
  if terminate == True:
    quit()
else:
  pass

bgcolor(background_colour)

for i in range(max_iteration):
  forward(i *spacing)
  left(set_angle)
  color(c[c_select])
  if rainbow_mode == True: #If you changed the booleen variable 'multi_colour' to 'False', it will select the first string on the list 'c'
    for x in range(6):
      c_select += 1
      if c_select == 6:
        c_select = -1
  if colour_debug == True:
    print('Colour = ' + str(c))
    print('Colour pointer = ' + 'Pointing to:' + str(c_select))
  if pattern_debug == True:
    print('Iteration = ' + 'MAX_ITERATION: ' + str(max_iteration) + ', CURRENT_ITERATION: ' + str(i) + ', RAINBOW_MODE: ' + str(rainbow_mode) + ', COLOUR_DEBUG: '+ str(colour_debug) + ', PATTERN_DEBUG: '+ str(pattern_debug) + ', HIDE TURTLE: ' + str(hide_turtle) + ', SPACING: ' + str(spacing) + ', SET_ANGLE: ' + str(set_angle))

print('dun')
terminate = check_cond_str({'exit', ''}, {''}, 'Exit? (Type Exit to terminate, not case sensitive): ')
if terminate == True:
  quit()
