# LUDO_GAME
This is 2D Ludo game for four player. Its game rules are similar with the real world game. At the end of the game a message is display about the winner. This game support gif format images.
## FUNTIONS
### Turn:
Display whose turn is it on the root window.
### Roll:
Rolling function that rolls a dice, goes again if it’s a six and display it on root window
### Clear:
Clears all the variable prior to next player's turn
### MoveCheck:
Check if the player can make a move and check if the player have three 6 in their turn their move will discarded
### Kill
Function that determines if the other's piece of different color can be killed
### Doublecheck:
If we have two same pieces then they make it double like one on the top of other
### Main:
This function creates all the necessary list of co-ordinates of all the colored boxes, excluding home and
stop, home positions for the objects of classes (BOX, YBOX, GBOX, BBOX). Place all the pieces at their
home position. Also Populates list of home boxes, colored boxes, game pieces and white boxes.
### Instruction:
It display all the rules for the user when user click the button.
### main_RED:
This function allows the red payer to play.
### Main_YELLOW:
This function allows the yellow player to play.
### Main_GREEN:
This function allows the green player to play.
### mouse_pointer:
It contain a formula that returns the x,y co-ordinates of the mouse pointer.
### Left Click:
It calls the main_RED, main_BLUES,main_YELLOW, main_GREEN, funtion and pass the x,y coordinates of where the mouse clicked on window.
### Display_menu:
This function the menu.
## CLASSES:
### BOX , YBOX , GBOX, BBOX
This classes contain the information about positions of the pieces, either the pieces are double on each
other or not and do swap when it is required.
