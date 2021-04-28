def print_function(one='na',two='na',three='na',four='na',five='na',six='na',seven='na',eight='na',nine='na') :
    type_1_space = '                      '
    type_2_leftmid_blank = '          |'
    type_2_leftmid_circle_line1 = '    +--+  |'
    type_2_leftmid_circle_line2 = '    |  |  |'
    type_2_leftmid_circle_line3 = '    +--+  |'
    type_2_leftmid_cross_line1 = '     \/   |'
    type_2_leftmid_cross_line2 = '     /\   |'
    type_3_right_blank = '          '
    type_3_right_circle_line1 = '    +--+  '
    type_3_right_circle_line2 = '    |  |  '
    type_3_right_circle_line3 = '    +--+  '
    type_3_right_cross_line1 = '     \/   '
    type_3_right_cross_line2 = '     /\   '
    line_two = True
    line_three = True
    line_four = True
    line_seven = True
    line_eight = True
    line_nine = True
    line_twelve = True
    line_thirteen = True
    line_fourteen = True
    print()
    print('-------------------------------------------------------------------')
    print()
    print('                      1.        |2.        |3.        ')
    while line_two :
        if one == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if one == '0' or one == 'o' or one == 'O' :
            print(type_1_space,type_2_leftmid_circle_line1,sep='',end='')
        if one == 'x' or one == 'X' :
            print(type_1_space,type_2_leftmid_cross_line1,sep='',end='')
        if two == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if two == '0' or two == 'o' or two == 'O' :
            print(type_2_leftmid_circle_line1,sep='',end='')
        if two == 'x' or two == 'X' :
            print(type_2_leftmid_cross_line1,sep='',end='')
        if three == 'na' :
            print(type_3_right_blank,sep='')
        if three == '0' or three == 'o' or three == 'O' :
            print(type_3_right_circle_line1,sep='')
        if three == 'x' or three == 'X' :
            print(type_3_right_cross_line1,sep='')
        line_two = False
    while line_three :
        if one == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if one == '0' or one == 'o' or one == 'O' :
            print(type_1_space,type_2_leftmid_circle_line2,sep='',end='')
        if one == 'x' or one == 'X' :
            print(type_1_space,type_2_leftmid_cross_line2,sep='',end='')
        if two == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if two == '0' or two == 'o' or two == 'O' :
            print(type_2_leftmid_circle_line2,sep='',end='')
        if two == 'x' or two == 'X' :
            print(type_2_leftmid_cross_line2,sep='',end='')
        if three == 'na' :
            print(type_3_right_blank,sep='')
        if three == '0' or three == 'o' or three == 'O' :
            print(type_3_right_circle_line2,sep='')
        if three == 'x' or three == 'X' :
            print(type_3_right_cross_line2,sep='')
        line_three = False
    while line_four :
        if one == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if one == '0' or one == 'o' or one == 'O' :
            print(type_1_space,type_2_leftmid_circle_line3,sep='',end='')
        if one == 'x' or one == 'X' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if two == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if two == '0' or two == 'o' or two == 'O' :
            print(type_2_leftmid_circle_line3,sep='',end='')
        if two == 'x' or two == 'X' :
            print(type_2_leftmid_blank,sep='',end='')
        if three == 'na' :
            print(type_3_right_blank,sep='')
        if three == '0' or three == 'o' or three == 'O' :
            print(type_3_right_circle_line3,sep='')
        if three == 'x' or three == 'X' :
            print(type_3_right_blank,sep='')
        line_four = False
    print('                      ==========+==========+==========')
    print('                      4.        |5.        |6.        ')
    while line_seven :
        if four == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if four == '0' or four == 'o' or four == 'O' :
            print(type_1_space,type_2_leftmid_circle_line1,sep='',end='')
        if four == 'x' or four == 'X' :
            print(type_1_space,type_2_leftmid_cross_line1,sep='',end='')
        if five == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if five == '0' or five == 'o' or five == 'O' :
            print(type_2_leftmid_circle_line1,sep='',end='')
        if five == 'x' or five == 'X' :
            print(type_2_leftmid_cross_line1,sep='',end='')
        if six == 'na' :
            print(type_3_right_blank,sep='')
        if six == '0' or six == 'o' or six == 'O' :
            print(type_3_right_circle_line1,sep='')
        if six == 'x' or six == 'X' :
            print(type_3_right_cross_line1,sep='')
        line_seven = False
    while line_eight :
        if four == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if four == '0' or four == 'o' or four == 'O' :
            print(type_1_space,type_2_leftmid_circle_line2,sep='',end='')
        if four == 'x' or four == 'X' :
            print(type_1_space,type_2_leftmid_cross_line2,sep='',end='')
        if five == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if five == '0' or five == 'o' or five == 'O' :
            print(type_2_leftmid_circle_line2,sep='',end='')
        if five == 'x' or five == 'X' :
            print(type_2_leftmid_cross_line2,sep='',end='')
        if six == 'na' :
            print(type_3_right_blank,sep='')
        if six == '0' or six == 'o' or six == 'O' :
            print(type_3_right_circle_line2,sep='')
        if six == 'x' or six == 'X' :
            print(type_3_right_cross_line2,sep='')
        line_eight = False
    while line_nine :
        if four == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if four == '0' or four == 'o' or four == 'O' :
            print(type_1_space,type_2_leftmid_circle_line3,sep='',end='')
        if four == 'x' or four == 'X' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if five == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if five == '0' or five == 'o' or five == 'O' :
            print(type_2_leftmid_circle_line3,sep='',end='')
        if five == 'x' or five == 'X' :
            print(type_2_leftmid_blank,sep='',end='')
        if six == 'na' :
            print(type_3_right_blank,sep='')
        if six == '0' or six == 'o' or six == 'O' :
            print(type_3_right_circle_line3,sep='')
        if six == 'x' or six == 'X' :
            print(type_3_right_blank,sep='')
        line_nine = False
    print('                      ==========+==========+==========')
    print('                      7.        |8.        |9.        ')
    while line_twelve :
        if seven == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if seven == '0' or seven == 'o' or seven == 'O' :
            print(type_1_space,type_2_leftmid_circle_line1,sep='',end='')
        if seven == 'x' or seven == 'X' :
            print(type_1_space,type_2_leftmid_cross_line1,sep='',end='')
        if eight == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if eight == '0' or eight == 'o' or eight == 'O' :
            print(type_2_leftmid_circle_line1,sep='',end='')
        if eight == 'x' or eight == 'X' :
            print(type_2_leftmid_cross_line1,sep='',end='')
        if nine == 'na' :
            print(type_3_right_blank,sep='')
        if nine == '0' or nine == 'o' or nine == 'O' :
            print(type_3_right_circle_line1,sep='')
        if nine == 'x' or nine == 'X' :
            print(type_3_right_cross_line1,sep='')
        line_twelve = False
    while line_thirteen :
        if seven == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if seven == '0' or seven == 'o' or seven == 'O' :
            print(type_1_space,type_2_leftmid_circle_line2,sep='',end='')
        if seven == 'x' or seven == 'X' :
            print(type_1_space,type_2_leftmid_cross_line2,sep='',end='')
        if eight == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if eight == '0' or eight == 'o' or eight == 'O' :
            print(type_2_leftmid_circle_line2,sep='',end='')
        if eight == 'x' or eight == 'X' :
            print(type_2_leftmid_cross_line2,sep='',end='')
        if nine == 'na' :
            print(type_3_right_blank,sep='')
        if nine == '0' or nine == 'o' or nine == 'O' :
            print(type_3_right_circle_line2,sep='')
        if nine == 'x' or nine == 'X' :
            print(type_3_right_cross_line2,sep='')
        line_thirteen = False
    while line_fourteen :
        if seven == 'na' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if seven == '0' or seven == 'o' or seven == 'O' :
            print(type_1_space,type_2_leftmid_circle_line3,sep='',end='')
        if seven == 'x' or seven == 'X' :
            print(type_1_space,type_2_leftmid_blank,sep='',end='')
        if eight == 'na' :
            print(type_2_leftmid_blank,sep='',end='')
        if eight == '0' or eight == 'o' or eight == 'O' :
            print(type_2_leftmid_circle_line3,sep='',end='')
        if eight == 'x' or eight == 'X' :
            print(type_2_leftmid_blank,sep='',end='')
        if nine == 'na' :
            print(type_3_right_blank,sep='')
        if nine == '0' or nine == 'o' or nine == 'O' :
            print(type_3_right_circle_line3,sep='')
        if nine == 'x' or nine == 'X' :
            print(type_3_right_blank,sep='')
        print()
        print('-------------------------------------------------------------------')
        print()
        line_fourteen = False
def input_function() :
    userinput = input()
    return userinput
def computer_vs_player() :
    import random
    from time import sleep
    loop_1 = True
    loop_2 = True
    loop_3 = True
    loop_4 = True
    loop_5 = True
    loop_6 = True
    loop_7 = True
    print('               =============================================')
    print('               |  1st Move           |       ____ 2nd Move |')
    print('               |          /|         |           |         |')
    print('               |         / |    <-- OR -->    ___|         |')
    print('               |           |         |       |             |')
    print('               |         __|__       |       |____         |')
    print('               =============================================')
    print()
    sleep(1)
    while loop_1 :
        print('>> Press 1 to play FRIST move | Press 2 to play after COMPUTER : ',end='')
        userinput_1 = input_function()
        if userinput_1 != '1' and userinput_1 != '2' :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
        else :
            loop_1 = False
    if userinput_1 == '1' :
        print()
        print()
        sleep(1)
        print('               =============================================')
        print('               |            Select One of These            |')
        print('               |      \  /          |        +-----+       |')
        print('               |       \/           |        |     |       |')
        print('               |       /\      <-- OR -->    |     |       |')
        print('               |      /  \          |        +-----+       |')
        print('               =============================================')
        print()
        sleep(1)
    while loop_2 and userinput_1 != '2' :
        print('>> Press x to play with cross | Press o to play Circle : ',end='')
        userinput_2 = input_function()
        if userinput_2 != 'x' and userinput_2 != 'o' :
            if userinput_2 == 'X' :
                print()
                print('         >>>>  WRONG INPUT ! Please enter small x  <<<<')
                print()
            elif userinput_2 == 'O' :
                print()
                print('         >>>>  WRONG INPUT ! Please enter small o  <<<<')
                print()
            elif userinput_2 == '0' :
                print()
                print('         >>>>  WRONG INPUT ! Please enter o, not zero  <<<<')
                print()
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        else :
            loop_2 = False
    if userinput_1 == '2' :
        # box_3==computer_move 1,box_9==computer_move 2,box_7==computer_move 3,box_1==computer_move 4 and computer_choice 2 == x,computer_choice 1 == o or O or 0
        box_1 = 'na'
        box_2 = 'na'
        box_3 = 'na'
        box_4 = 'na'
        box_5 = 'na'
        box_6 = 'na'
        box_7 = 'na'
        box_8 = 'na'
        box_9 = 'na'
        # 1st move
        computer_choice = random.randrange(1,3)
        computer_move = random.randrange(1,5)
        if computer_move == 1 :
            if computer_choice == 2 :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else:
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif computer_move == 2 :
            if computer_choice == 2 :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif computer_move == 3 :
            if computer_choice == 2 :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        else :
            if computer_choice == 2 :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        # 2nd move
        while loop_3 :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_3 = input_function()
            print()
            if userinput_3 == '1' and box_1 == 'na' :
                if computer_choice == 2 :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '2' and box_2 == 'na' :
                if computer_choice == 2 :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '3' and box_3 == 'na' :
                if computer_choice == 2 :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '4' and box_4 == 'na' :
                if computer_choice == 2 :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '5' and box_5 == 'na' :
                if computer_choice == 2 :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '6' and box_6 == 'na' :
                if computer_choice == 2 :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '7' and box_7 == 'na' :
                if computer_choice == 2 :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '8' and box_8 == 'na' :
                if computer_choice == 2 :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '9' and box_9 == 'na' :
                if computer_choice == 2 :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # 3rd move
        if userinput_3 == '1' :
            sleep(2)
            if computer_move == 1 :
                computer_move = random.randrange(1,3)
                # 1==box_9,2==box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                computer_move = random.randrange(1,3)
                # 1==box_3 and 2==box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1==box_3 and 2==box_9
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '2' :
            sleep(2)
            if computer_move == 1 :
                if computer_choice == 2 :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                computer_move = random.randrange(1,3)
                # computer_move 1 == box_3 and computer_move 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                if computer_choice == 2 :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                if computer_choice == 2 :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '3' :
            sleep(2)
            if computer_move == 2 :
                computer_move = random.randrange(1,3)
                # 1 == box_7 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '4' :
            sleep(2)
            if computer_move == 1 :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                if computer_choice == 2 :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                if computer_choice == 2 :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '5' :
            sleep(2)
            if computer_move == 1 :
                if computer_choice == 2 :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                if computer_choice == 2 :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                if computer_choice == 2 :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                if computer_choice == 2 :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '6' :
            sleep(2)
            if computer_move == 1 :
                if computer_choice == 2 :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                if computer_choice == 2 :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '7' :
            sleep(2)
            if computer_move == 1 :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_9
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        elif userinput_3 == '8' :
            sleep(2)
            if computer_move == 1 :
                computer_move = random.randrange(1,3)
                # 1 == box_9 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                if computer_choice == 2 :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                if computer_choice == 2 :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        else :
            sleep(2)
            if computer_move == 1 :
                computer_move = random.randrange(1,3)
                # 1 == box_7 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_1
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                computer_move = random.randrange(1,3)
                # 1 == box_3 and 2 == box_7
                if computer_move == 1 :
                    if computer_choice == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if computer_choice == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        # 4th move
        while loop_4 :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_4 = input_function()
            print()
            if userinput_4 == '1' and box_1 == 'na' :
                if computer_choice == 2 :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '2' and box_2 == 'na' :
                if computer_choice == 2 :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '3' and box_3 == 'na' :
                if computer_choice == 2 :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '4' and box_4 == 'na' :
                if computer_choice == 2 :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '5' and box_5 == 'na' :
                if computer_choice == 2 :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '6' and box_6 == 'na' :
                if computer_choice == 2 :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '7' and box_7 == 'na' :
                if computer_choice == 2 :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '8' and box_8 == 'na' :
                if computer_choice == 2 :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '9' and box_9 == 'na' :
                if computer_choice == 2 :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # After 4th move(user move), CODE for 5th move(computer move).
        if computer_choice == 2 :
            sleep(2)
            if box_1 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'o' and box_3 == 'x' and box_7 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'o' and box_9 == 'x' and box_3 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'o' and box_7 == 'x' and box_3 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'o' and box_7 == 'x' and box_9 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'o' and box_9 == 'x' and box_3 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'o' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o' and box_9 == 'x' and box_1 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o' and box_7 == 'x' and box_9 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o'  and box_1 == 'x' and box_9 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'o' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_9 == 'x' and box_3 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_7 == 'x' and box_9 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == '0' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'o' and box_9 == 'x' and box_7 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'o' and box_7 == 'x' and box_9 == 'x' :
                if box_8 == 'na' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'o' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_9 == 'x' and box_3 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_9 == 'x' and box_1 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'o' and box_1 == 'x' and box_9 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_9 == 'x' and box_3 == 'x' :
                if box_6 == 'na' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'o' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_3 == 'x' and box_7 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_7 == 'x' and box_3 == 'x' :
                if box_5 == 'na' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'na' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'o' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'na' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
        else :
            sleep(2)
            if box_1 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'x' and box_3 == 'o' and box_7 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'x' and box_9 == 'o' and box_3 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'x' and box_7 == 'o' and box_3 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_1 == 'x' and box_7 == 'o' and box_9 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'x' and box_9 == 'o' and box_3 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_2 == 'x' and box_1 == 'o' and box_7 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x' and box_9 == 'o' and box_1 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x' and box_7 == 'o' and box_9 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x'  and box_1 == 'o' and box_9 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_3 == 'x' and box_1 == 'o' and box_7 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_3 == 'o' and box_1 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_9 == 'o' and box_3 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_7 == 'o' and box_9 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_4 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_5 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_3 == 'o' and box_1 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_9 == 'o' and box_7 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_7 == 'o' and box_9 == 'o' :
                if box_8 == 'na' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_8 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_6 == 'x' and box_1 == 'o' and box_7 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_3 == 'o' and box_1 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_9 == 'o' and box_3 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_9 == 'o' and box_1 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_7 == 'x' and box_1 == 'o' and box_9 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_3 == 'o' and box_9 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_3 == 'o' and box_1 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_9 == 'o' and box_3 == 'o' :
                if box_6 == 'na' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_8 == 'x' and box_1 == 'o' and box_7 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_3 == 'o' and box_7 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_3 == 'o' and box_1 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_7 == 'o' and box_3 == 'o' :
                if box_5 == 'na' :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_5 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_7 == 'o' and box_1 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_1 == 'o' and box_3 == 'o' :
                if box_2 == 'na' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_2 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
            elif box_9 == 'x' and box_1 == 'o' and box_7 == 'o' :
                if box_4 == 'na' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    if box_4 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        win = False
        # code for 6th move (user move).
        while loop_5 and not win :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_5 = input_function()
            print()
            if userinput_5 == '1' and box_1 == 'na' :
                if computer_choice == 2 :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '2' and box_2 == 'na' :
                if computer_choice == 2 :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '3' and box_3 == 'na' :
                if computer_choice == 2 :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '4' and box_4 == 'na' :
                if computer_choice == 2 :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '5' and box_5 == 'na' :
                if computer_choice == 2 :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '6' and box_6 == 'na' :
                if computer_choice == 2 :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '7' and box_7 == 'na' :
                if computer_choice == 2 :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '8' and box_8 == 'na' :
                if computer_choice == 2 :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '9' and box_9 == 'na' :
                if computer_choice == 2 :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # After 6th move(user move), CODE for 7th move(computer move).
        if computer_choice == 2 and win == False :
            sleep(2)
            if box_1 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_7 == 'x' :
                if box_5 == 'o':
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_1 == 'o' and box_5 == 'o' and box_3 == 'x' and box_7 == 'x' and box_9 == 'x' :
                if box_6 == 'o':
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_1 == 'o' and box_6 == 'o' and box_9 == 'x' and box_3 == 'x' and box_7 == 'x' :
                if box_5 == 'o' :
                    box_8 ='x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_1 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_3 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_1 == 'o' and box_5 == 'o' and box_7 == 'x' and box_3 == 'x' and box_9 == 'x' :
                if box_6 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_1 == 'o' and box_8 == 'o' and box_7 == 'x' and box_9 == 'x' and box_3 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_2 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_7 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_2 == 'o' and box_6 == 'o' and box_9 == 'x' and box_3 == 'x' and box_7 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_2 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_5 == 'x' :
                if box_1 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_3 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_3
                    if computer_move == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_2 == 'o' and box_4 == 'o' and box_7 == 'x' and box_1 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_2 == 'o' and box_4 == 'o' and box_1 == 'x' and box_7 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_5 == 'o' and box_9 == 'x' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_8 == 'o' and box_7 == 'x' and box_9 == 'x' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_choice == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_4 == 'o' and box_7 == 'x' and box_1 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_5 == 'o' and box_1 == 'x' and box_9 == 'x' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_3 == 'o' and box_4 == 'o' and box_1 == 'x' and box_7 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_8 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_5 == 'x' :
                if box_1 == 'o' :
                    box_7 = 'x'
                    print_finction(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_7 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_2 == 'o' and box_3 == 'x' and box_1 == 'x' and box_5 == 'x' :
                if box_9 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_9 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_6 == 'o' and box_9 == 'x' and box_3 == 'x' and box_5 == 'x' :
                if box_7 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_1 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_7 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_3 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_8 == 'o' and box_7 == 'x' and box_9 == 'x' and box_5 == 'x' :
                if box_3 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_1 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_4 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_5 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_4 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_2 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_choice == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_4 == 'o' and box_7 == 'x' and box_1 == 'x' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_8 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_2 == 'o' and box_3 == 'x' and box_1 == 'x' and box_5 == 'x' :
                if box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_9 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_6 == 'o' and box_8 == 'o' and box_9 == 'x' and box_7 == 'x' and box_5 == 'x' :
                if box_1 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_3 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_6 == 'o' and box_8 == 'o' and box_7 == 'x' and box_9 == 'x' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_6 == 'o' and box_4 == 'o' and box_7 == 'x' and box_1 == 'x' and box_5 == 'x' :
                if box_3 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_6 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_6 == 'o' and box_4 == 'o' and box_1 == 'x' and box_7 == 'x' and box_5 == 'x' :
                if box_3 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_7 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_7 == 'o' and box_2 == 'o' and box_3 == 'x' and box_1 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_7 == 'o' and box_6 == 'o' and box_9 == 'x' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_7 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_9 == 'x' :
                if box_5 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_5 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_7 == 'o' and box_5 == 'o' and box_1 == 'x' and box_9 == 'x' and box_3 == 'x' :
                if box_2 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_6 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_6
                    if computer_choice == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_6 == 'o' and box_3 == 'x' and box_9 == 'x' and box_5 == 'x' :
                if box_1 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_7 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_2 == 'o' and box_3 == 'x' and box_1 == 'x' and box_5 == 'x' :
                if box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_9 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_6 == 'o' and box_9 == 'x' and box_3 == 'x' and box_5 == 'x' :
                if box_1 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_7 and 2 == box_1
                    if computer_move == 2 :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_4 == 'o' and box_7 == 'x' and box_3 == 'x' and box_5 == 'x' :
                if box_3 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_5 == 'x' :
                if box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_9 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_8 == 'o' and box_4 == 'o' and box_1 == 'x' and box_7 == 'x' and box_5 == 'x' :
                if box_3 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_9 == 'o' and box_5 == 'o' and box_3 == 'x' and box_7 == 'x' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_4 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_9 == 'o' and box_2 == 'o' and box_3 == 'x' and box_1 == 'x' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_9 == 'o' and box_5 == 'o' and box_7 == 'x' and box_3 == 'x' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_4 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_9 == 'o' and box_4 == 'o' and box_7 == 'x' and box_1 == 'x' and box_3 == 'x' :
                if box_2 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            elif box_9 == 'o' and box_2 == 'o' and box_1 == 'x' and box_3 == 'x' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_5 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_5
                    if computer_move == 2 :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            else :
                if box_9 == 'o' and box_4 == 'o' and box_1 == 'x' and box_7 == 'x' and box_3 == 'x' :
                    if box_2 == 'o' :
                        box_5 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
        # condition 2 for 7 th move
        else :
            if computer_choice == 1 and win == False :
                sleep(2)
                if box_1 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_7 == 'o' :
                    if box_5 == 'x':
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_1 == 'x' and box_5 == 'x' and box_3 == 'o' and box_7 == 'o' and box_9 == 'o' :
                    if box_6 == 'x':
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_6 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_1 == 'x' and box_6 == 'x' and box_9 == 'o' and box_3 == 'o' and box_7 == 'o' :
                    if box_5 == 'x' :
                        box_8 ='o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_1 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_3 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_1 == 'x' and box_5 == 'x' and box_7 == 'o' and box_3 == 'o' and box_9 == 'o' :
                    if box_6 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_6 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_1 == 'x' and box_8 == 'x' and box_7 == 'o' and box_9 == 'o' and box_3 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_2 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_7 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_2 == 'x' and box_6 == 'x' and box_9 == 'o' and box_3 == 'o' and box_7 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_2 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_5 == 'o' :
                    if box_1 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_3 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_1 and 2 == box_3
                        if computer_move == 2 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_2 == 'x' and box_4 == 'x' and box_7 == 'o' and box_1 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_2 == 'x' and box_4 == 'x' and box_1 == 'o' and box_7 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_1 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_5 == 'x' and box_9 == 'o' and box_1 == 'o' and box_7 == 'o' :
                    if box_4 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_8 == 'x' and box_7 == 'o' and box_9 == 'o' and box_1 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_choice == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_4 == 'x' and box_7 == 'o' and box_1 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_5 == 'x' and box_1 == 'o' and box_9 == 'o' and box_7 == 'o' :
                    if box_4 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_3 == 'x' and box_4 == 'x' and box_1 == 'o' and box_7 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_8 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_4 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_5 == 'o' :
                    if box_1 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_7 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_7 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_4 == 'x' and box_2 == 'x' and box_3 == 'o' and box_1 == 'o' and box_5 == 'o' :
                    if box_9 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_7 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_9 and 2 == box_7
                        if computer_move == 2 :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_4 == 'x' and box_6 == 'x' and box_9 == 'o' and box_3 == 'o' and box_5 == 'o' :
                    if box_7 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_1 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_7 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            sleep(1)
                            win = True
                elif box_4 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_3 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_4 == 'x' and box_8 == 'x' and box_7 == 'o' and box_9 == 'o' and box_5 == 'o' :
                    if box_3 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_1 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_4 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_5 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_4 == 'o' :
                    if box_2 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_2 == 'o' :
                    if box_4 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_6
                        if computer_choice == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'x' and box_4 == 'x' and box_7 == 'o' and box_1 == 'o' and box_6 == 'o' :
                    if box_2 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_8
                        if computer_move == 2 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_8 == 'o' :
                    if box_4 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' and box_2 == 'x' and box_3 == 'o' and box_1 == 'o' and box_5 == 'o' :
                    if box_7 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_9 and 2 == box_7
                        if computer_move == 2 :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_6 == 'x' and box_8 == 'x' and box_9 == 'o' and box_7 == 'o' and box_5 == 'o' :
                    if box_1 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_3 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_6 == 'x' and box_8 == 'x' and box_7 == 'o' and box_9 == 'o' and box_1 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_6 == 'x' and box_4 == 'x' and box_7 == 'o' and box_1 == 'o' and box_5 == 'o' :
                    if box_3 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_9
                        if computer_move == 2 :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_6 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_7 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_6 == 'x' and box_4 == 'x' and box_1 == 'o' and box_7 == 'o' and box_5 == 'o' :
                    if box_3 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_9
                        if computer_move == 2 :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_7 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_1 == 'o' :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_7 == 'x' and box_2 == 'x' and box_3 == 'o' and box_1 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_7 == 'x' and box_6 == 'x' and box_9 == 'o' and box_3 == 'o' and box_1 == 'o' :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_7 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_9 == 'o' :
                    if box_5 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_5 and 2 == box_6
                        if computer_move == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_7 == 'x' and box_5 == 'x' and box_1 == 'o' and box_9 == 'o' and box_3 == 'o' :
                    if box_2 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_6 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_6
                        if computer_choice == 2 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            sleep(1)
                            win = True
                elif box_8 == 'x' and box_6 == 'x' and box_3 == 'o' and box_9 == 'o' and box_5 == 'o' :
                    if box_1 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_7 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_7 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_8 == 'x' and box_2 == 'x' and box_3 == 'o' and box_1 == 'o' and box_5 == 'o' :
                    if box_7 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_9 and 2 == box_7
                        if computer_move == 2 :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_8 == 'x' and box_6 == 'x' and box_9 == 'o' and box_3 == 'o' and box_5 == 'o' :
                    if box_1 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_7 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_7 and 2 == box_1
                        if computer_move == 2 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_8 == 'x' and box_4 == 'x' and box_7 == 'o' and box_3 == 'o' and box_5 == 'o' :
                    if box_3 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_9
                        if computer_move == 2 :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_8 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_5 == 'o' :
                    if box_7 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_9 and 2 == box_7
                        if computer_move == 2 :
                            box_7 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_8 == 'x' and box_4 == 'x' and box_1 == 'o' and box_7 == 'o' and box_5 == 'o' :
                    if box_3 == 'x' :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_3 and 2 == box_9
                        if computer_move == 2 :
                            box_9 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_9 == 'x' and box_5 == 'x' and box_3 == 'o' and box_7 == 'o' and box_1 == 'o' :
                    if box_2 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_4 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_4
                        if computer_move == 2 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_9 == 'x' and box_2 == 'x' and box_3 == 'o' and box_1 == 'o' and box_7 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_9 == 'x' and box_5 == 'x' and box_7 == 'o' and box_3 == 'o' and box_1 == 'o' :
                    if box_2 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_4 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_4
                        if computer_move == 2 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_9 == 'x' and box_4 == 'x' and box_7 == 'o' and box_1 == 'o' and box_3 == 'o' :
                    if box_2 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                elif box_9 == 'x' and box_2 == 'x' and box_1 == 'o' and box_3 == 'o' and box_7 == 'o' :
                    if box_4 == 'x' :
                        box_5 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    elif box_5 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        computer_move = random.randrange(1,3)
                        # 1 == box_4 and 2 == box_5
                        if computer_move == 2 :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                else :
                    if box_9 == 'x' and box_4 == 'x' and box_1 == 'o' and box_7 == 'o' and box_3 == 'o' :
                        if box_2 == 'x' :
                            box_5 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        elif box_5 == 'x' :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
                        else :
                            computer_move = random.randrange(1,3)
                            # 1 == box_2 and 2 == box_5
                            if computer_move == 2 :
                                box_5 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                                sleep(1)
                                print('                             >>>>   YOU LOSE !   <<<<')
                                win = True
                            else :
                                box_2 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                                sleep(1)
                                print('                             >>>>   YOU LOSE !   <<<<')
                                win = True
        # code for 8th move (user move).
        while loop_6 and not win :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_6 = input_function()
            print()
            if userinput_6 == '1' and box_1 == 'na' :
                if computer_choice == 2 :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '2' and box_2 == 'na' :
                if computer_choice == 2 :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '3' and box_3 == 'na' :
                if computer_choice == 2 :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '4' and box_4 == 'na' :
                if computer_choice == 2 :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '5' and box_5 == 'na' :
                if computer_choice == 2 :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '6' and box_6 == 'na' :
                if computer_choice == 2 :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '7' and box_7 == 'na' :
                if computer_choice == 2 :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '8' and box_8 == 'na' :
                if computer_choice == 2 :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '9' and box_9 == 'na' :
                if computer_choice == 2 :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # After 8th move(user move), CODE for 9th move(computer move).
        # condition 1 for 9th move
        if computer_choice == 2 and win == False :
            sleep(2)
            # 1.6
            if box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_2 == 'x' and box_7 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_2 == 'x' and box_1 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_2 == 'x' and box_8 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_8 == 'o' and box_2 == 'x' and box_7 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            # 1.12
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_8 == 'x' and box_2 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_8 == 'x' and box_7 == 'o' :
                box_2 == 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_8 == 'x' and box_1 == 'o' :
                box_2 == 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_2 == 'o' and box_8 == 'x' and box_1 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            # 2.6
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_4 == 'x' and box_3 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_4 == 'x' and box_1 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_4 == 'x' and box_6 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_6 == 'o' and box_4 == 'x' and box_3 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            # 2.12
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_6 == 'x' and box_3 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_6 == 'x' and box_4 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_6 == 'x' and box_1 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' and box_6 == 'x' and box_1 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            # 3.6
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_2 == 'x' and box_9 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_2 == 'x' and box_3 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_2 == 'x' and box_8 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_8 == 'o' and box_2 == 'x' and box_9 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            # 3.12
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_2 == 'o' and box_8 == 'x' and box_3 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_3 == 'x' and box_4 == 'o' and box_6 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_8 == 'x' and box_2 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_8 == 'x' and box_9 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_8 == 'x' and box_3 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            # 4.6
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_6 == 'o' and box_4 == 'x' and box_9 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_4 == 'x' and box_6 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_4 == 'x' and box_7 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_4 == 'x' and box_9 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            # 4.16
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_4 == 'o' and box_6 == 'x' and box_7 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_6 == 'x' and box_4 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   YOU LOSE !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_6 == 'x' and box_9 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_6 == 'x' and box_7 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                sleep(1)
                print('                             >>>>   GAME DRAW !   <<<<')
        # condition 2 for 9th move
        else :
            if computer_choice == 1 and win == False :
                sleep(2)
                # 1.6
                if box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_2 == 'o' and box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_8 == 'x' and box_2 == 'o' and box_7 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                # 1.12
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_8 == 'o' and box_7 == 'x' :
                    box_2 == 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_8 == 'o' and box_1 == 'x' :
                    box_2 == 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_2 == 'x' and box_8 == 'o' and box_1 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                # 2.6
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_4 == 'o' and box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_6 == 'x' and box_4 == 'o' and box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                # 2.12
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_6 == 'o' and box_3 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_6 == 'o' and box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' and box_6 == 'o' and box_1 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                # 3.6
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_2 == 'o' and box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_2 == 'o' and box_3 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_8 == 'x' and box_2 == 'o' and box_9 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                # 3.12
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_2 == 'x' and box_8 == 'o' and box_3 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_3 == 'o' and box_4 == 'x' and box_6 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_8 == 'o' and box_9 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_8 == 'o' and box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                # 4.6
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_6 == 'x' and box_4 == 'o' and box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_4 == 'o' and box_7 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_4 == 'o' and box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                # 4.16
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_4 == 'x' and box_6 == 'o' and box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_6 == 'o' and box_9 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_6 == 'o' and box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
    # If player plays 1st move.
    else :
        box_1 = 'na'
        box_2 = 'na'
        box_3 = 'na'
        box_4 = 'na'
        box_5 = 'na'
        box_6 = 'na'
        box_7 = 'na'
        box_8 = 'na'
        box_9 = 'na'
        # 1st move (player move)
        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        while loop_3 :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_3 = input_function()
            print()
            if userinput_3 == '1' and box_1 == 'na' :
                if userinput_2 == 'x' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '2' and box_2 == 'na' :
                if userinput_2 == 'x' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '3' and box_3 == 'na' :
                if userinput_2 == 'x' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '4' and box_4 == 'na' :
                if userinput_2 == 'x' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '5' and box_5 == 'na' :
                if userinput_2 == 'x' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '6' and box_6 == 'na' :
                if userinput_2 == 'x' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '7' and box_7 == 'na' :
                if userinput_2 == 'x' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '8' and box_8 == 'na' :
                if userinput_2 == 'x' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            elif userinput_3 == '9' and box_9 == 'na' :
                if userinput_2 == 'x' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_3 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # 2nd move (computer move)
        if userinput_3 == '5' :
            sleep(2)
            computer_move = random.randrange(1,5)
            # 1 == box_3 and 2 == box_9 and 3 == box_7 and 4 == box_1
            if computer_move == 1 :
                if userinput_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 2 :
                if userinput_2 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif computer_move == 3 :
                if userinput_2 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                if userinput_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        else :
            sleep(2)
            if userinput_2 == 'x' :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        # 3rd move (Player move)
        while loop_4 :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_4 = input_function()
            print()
            if userinput_4 == '1' and box_1 == 'na' :
                if userinput_2 == 'x' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '2' and box_2 == 'na' :
                if userinput_2 == 'x' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '3' and box_3 == 'na' :
                if userinput_2 == 'x' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '4' and box_4 == 'na' :
                if userinput_2 == 'x' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '5' and box_5 == 'na' :
                if userinput_2 == 'x' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '6' and box_6 == 'na' :
                if userinput_2 == 'x' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '7' and box_7 == 'na' :
                if userinput_2 == 'x' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '8' and box_8 == 'na' :
                if userinput_2 == 'x' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            elif userinput_4 == '9' and box_9 == 'na' :
                if userinput_2 == 'x' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_4 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # 4th move (computer move)
        # 1st condition
        if userinput_2 == 'x' :
            sleep(2)
            # 1.7
            if box_1 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 2.7
            elif box_2 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 3.7
            elif box_3 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 4.7
            elif box_4 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.7
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_3 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_6 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_7 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_8 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_9 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.14
            elif box_5 == 'x' and box_3 == 'o' and box_1 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_4 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_7 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_8 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_9 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.21
            elif box_5 == 'x' and box_7 == 'o' and box_1 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_2 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_3 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_6 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_9 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28
            elif box_5 == 'x' and box_9 == 'o' and box_1 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_2 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_3 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_4 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_7 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.7
            elif box_6 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.7
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.7
            elif box_8 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'x' and box_5 == 'o' and box_9 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.7
            elif box_9 == 'x' and box_5 == 'o' and box_1 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_2 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_3 == 'x' :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_4 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_6 == 'x' :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'x' and box_5 == 'o' and box_8 == 'x' :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        # 4th move (computer move)
        # 2nd condition
        else :
            sleep(2)
            # 1.7
            if box_1 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 2.7
            elif box_2 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 3.7
            elif box_3 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 4.7
            elif box_4 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.7
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_3 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_6 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_7 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_8 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_9 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.14
            elif box_5 == 'o' and box_3 == 'x' and box_1 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_4 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_7 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_8 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_3 == 'x' and box_9 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.21
            elif box_5 == 'o' and box_7 == 'x' and box_1 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_2 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_3 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_6 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_7 == 'x' and box_9 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28
            elif box_5 == 'o' and box_9 == 'x' and box_1 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_2 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_3 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_4 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_7 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.7
            elif box_6 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_6 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.7
            elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_7 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.7
            elif box_8 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_8 == 'o' and box_5 == 'x' and box_9 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.7
            elif box_9 == 'o' and box_5 == 'x' and box_1 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_2 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_3 == 'o' :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_4 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_6 == 'o' :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_9 == 'o' and box_5 == 'x' and box_8 == 'o' :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
        # 5rd move (Player move)
        while loop_5 :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_5 = input_function()
            print()
            if userinput_5 == '1' and box_1 == 'na' :
                if userinput_2 == 'x' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '2' and box_2 == 'na' :
                if userinput_2 == 'x' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '3' and box_3 == 'na' :
                if userinput_2 == 'x' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '4' and box_4 == 'na' :
                if userinput_2 == 'x' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '5' and box_5 == 'na' :
                if userinput_2 == 'x' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '6' and box_6 == 'na' :
                if userinput_2 == 'x' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '7' and box_7 == 'na' :
                if userinput_2 == 'x' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '8' and box_8 == 'na' :
                if userinput_2 == 'x' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            elif userinput_5 == '9' and box_9 == 'na' :
                if userinput_2 == 'x' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_5 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # 6th move (computer move)
        # 1st condition
        if userinput_2 == 'x' :
            sleep(2)
            win = False
            # 1.7
            if box_1 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_7 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_9 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 2.7
            elif box_2 == 'x' and box_5 == 'o' and box_1 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_3 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_7 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_8 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_9 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 3.7
            elif box_3 == 'x' and box_5 == 'o' and box_1 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_7 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_8 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 4.7
            elif box_4 == 'x' and box_5 == 'o' and box_1 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_3 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_6 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_7 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.7
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_1 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_1 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.14
            elif box_5 == 'x' and box_3 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_9 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_3 == 'o' and box_7 == 'x' and box_9 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_3 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_3 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.21
            elif box_5 == 'x' and box_7 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_7 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_9 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_7 == 'o' and box_3 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_7 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.28
            elif box_5 == 'x' and box_9 == 'o' and box_1 == 'x' and box_3 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_9 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_9 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_9 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_9 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.7
            elif box_6 == 'x' and box_5 == 'o' and box_1 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_3 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_7 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_8 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_6 == 'x' and box_5 == 'o' and box_9 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.7
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_3 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_8 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_7 == 'x' and box_5 == 'o' and box_9 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.7
            elif box_8 == 'x' and box_5 == 'o' and box_1 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_3 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_7 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_8 == 'x' and box_5 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.7
            elif box_9 == 'x' and box_5 == 'o' and box_1 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_3 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_9 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
        # 2nd condition
        else :
            if userinput_2 == 'o' :
                sleep(2)
                win = False
                # 1.7
                if box_1 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' :
                    if box_8 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_7 == 'o' and box_4 == 'x' :
                    if box_6 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_1 == 'o' and box_5 == 'x' and box_9 == 'o' and box_4 == 'x' :
                    if box_6 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 2.7
                elif box_2 == 'o' and box_5 == 'x' and box_1 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_3 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_7 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_8 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_2 == 'o' and box_5 == 'x' and box_9 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 3.7
                elif box_3 == 'o' and box_5 == 'x' and box_1 == 'o' and box_2 == 'x' :
                    if box_8 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_7 == 'o' and box_2 == 'x' :
                    if box_8 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_8 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' :
                    if box_4 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 4.7
                elif box_4 == 'o' and box_5 == 'x' and box_1 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_3 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_6 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_7 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_4 == 'o' and box_5 == 'x' and box_9 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 5.7
                elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_1 == 'x' and box_3 == 'o' and box_7 == 'x' :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    if box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_7 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_1 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    if box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_1 == 'x' and box_7 == 'o' and box_3 == 'x' :
                    if box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_1 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    if box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 5.14
                elif box_5 == 'o' and box_3 == 'x' and box_1 == 'o' and box_9 == 'x' :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_7 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_3 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_7 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_3 == 'x' and box_7 == 'o' and box_9 == 'x' :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_3 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_3 == 'x' and box_9 == 'o' and box_1 == 'x' :
                    if box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 5.21
                elif box_5 == 'o' and box_7 == 'x' and box_1 == 'o' and box_9 == 'x' :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_7 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_7 == 'x' and box_3 == 'o' and box_1 == 'x' :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_7 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    if box_1 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_9 == 'o' :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_7 == 'x' and box_9 == 'o' and box_1 == 'x' :
                    if box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 5.28
                elif box_5 == 'o' and box_9 == 'x' and box_1 == 'o' and box_3 == 'x' :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_9 == 'x' and box_2 == 'o' and box_8 == 'x' :
                    if box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_9 == 'x' and box_3 == 'o' and box_7 == 'x' :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_9 == 'x' and box_4 == 'o' and box_6 == 'x' :
                    if box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' :
                    if box_1 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_2 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_8 == 'o' :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_5 == 'o' and box_9 == 'x' and box_7 == 'o' and box_3 == 'x' :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' :
                    if box_1 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_3 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_4 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    elif box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if box_7 == 'o' :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                # 6.7
                elif box_6 == 'o' and box_5 == 'x' and box_1 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_3 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_7 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_8 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_6 == 'o' and box_5 == 'x' and box_9 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 7.7
                elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' :
                    if box_6 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_3 == 'o' and box_4 == 'x' :
                    if box_6 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_8 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_7 == 'o' and box_5 == 'x' and box_9 == 'o' and box_8 == 'x' :
                    if box_2 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 8.7
                elif box_8 == 'o' and box_5 == 'x' and box_1 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' :
                    if box_9 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_3 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_7 == 'o' and box_9 == 'x' :
                    if box_1 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_8 == 'o' and box_5 == 'x' and box_9 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                # 9.7
                elif box_9 == 'o' and box_5 == 'x' and box_1 == 'o' and box_6 == 'x' :
                    if box_4 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_3 == 'o' and box_6 == 'x' :
                    if box_4 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' :
                    if box_7 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' :
                    if box_2 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                elif box_9 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' :
                    if box_3 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
        # 7rd move (Player move)
        while loop_6 and win == False :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_6 = input_function()
            print()
            if userinput_6 == '1' and box_1 == 'na' :
                if userinput_2 == 'x' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '2' and box_2 == 'na' :
                if userinput_2 == 'x' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '3' and box_3 == 'na' :
                if userinput_2 == 'x' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '4' and box_4 == 'na' :
                if userinput_2 == 'x' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '5' and box_5 == 'na' :
                if userinput_2 == 'x' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '6' and box_6 == 'na' :
                if userinput_2 == 'x' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '7' and box_7 == 'na' :
                if userinput_2 == 'x' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '8' and box_8 == 'na' :
                if userinput_2 == 'x' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            elif userinput_6 == '9' and box_9 == 'na' :
                if userinput_2 == 'x' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    loop_6 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
        # 8th move (computer move)
        # 1st condition
        if userinput_2 == 'x' and win == False :
            sleep(2)
            # 1.7
            if box_1 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' and box_7 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_8 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' and box_3 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' and box_7 == 'x' and box_4 == 'o' :
                if box_2 == 'x' or box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' and box_3 == 'x' and box_2 == 'o' :
                if box_4 == 'x' or box_6 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'x' and box_5 == 'o' and box_9 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 2.7
            elif box_2 == 'x' and box_5 == 'o' and box_1 == 'x' and box_3 == 'o' and box_7 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_3 == 'x' and box_1 == 'o' and box_9 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' and box_7 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_7 == 'x' and box_1 == 'o' and box_9 == 'x' and box_8 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'x' and box_5 == 'o' and box_8 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'x' and box_5 == 'o' and box_9 == 'x' and box_3 == 'o' and box_7 == 'x' and box_8 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 3.7
            elif box_3 == 'x' and box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' and box_1 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_7 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'x' and box_5 == 'o' and box_8 == 'x' and box_9 == 'o' and box_1 == 'x' and box_2 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'x' and box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 4.7
            elif box_4 == 'x' and box_5 == 'o' and box_1 == 'x' and box_7 == 'o' and box_3 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_3 == 'x' and box_1 == 'o' and box_9 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'x' and box_5 == 'o' and box_6 == 'x' and box_1 == 'o' and box_9 == 'x' and box_3 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_7 == 'x' and box_1 == 'o' and box_9 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' and box_3 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'x' and box_5 == 'o' and box_9 == 'x' and box_7 == 'o' and box_3 == 'x' and box_6 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.7
            # 5.1.1
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.1.1
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.1.2
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_4 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.1.3
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.1.4
            elif box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_4 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.2
            elif box_5 == 'x' and box_1 == 'o' and box_3 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.3.1
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_2 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 2 == box_9 and 1 == box_2
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.3.2
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.3.3
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.3.4
            elif box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.4
            elif box_5 == 'x' and box_1 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.5
            elif box_5 == 'x' and box_1 == 'o' and box_7 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.6
            elif box_5 == 'x' and box_1 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.7
            elif box_5 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.14
            # 5.8
            elif box_5 == 'x' and box_3 == 'o' and box_1 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.9
            # 5.9.1
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_6 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.9.2
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_9 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.9.3
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.9.4
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_6 == 'o' :
                if box_9 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.9.5
            elif box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.10
            elif box_5 == 'x' and box_3 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11
            # 5.11.1
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.11.2
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.11.3
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11.4
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11.5
            elif box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.12
            elif box_5 == 'x' and box_3 == 'o' and box_7 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.13
            elif box_5 == 'x' and box_3 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.14
            elif box_5 == 'x' and box_3 == 'o' and box_9 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.15
            elif box_5 == 'x' and box_7 == 'o' and box_1 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.16
            elif box_5 == 'x' and box_7 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.17
            elif box_5 == 'x' and box_7 == 'o' and box_3 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.18.1
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.2
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_9 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.3
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_9 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.4
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.18.5
            elif box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.19
            elif box_5 == 'x' and box_7 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.1
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' :
                if box_3 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.20.2
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.3
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.20.4
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.5
            elif box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_9 == 'x' and box_1 == 'o' :
                if box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.21
            elif box_5 == 'x' and box_7 == 'o' and box_9 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.22
            elif box_5 == 'x' and box_9 == 'o' and box_1 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.23
            elif box_5 == 'x' and box_9 == 'o' and box_2 == 'x' and box_8 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.24
            elif box_5 == 'x' and box_9 == 'o' and box_3 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.25
            elif box_5 == 'x' and box_9 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.1
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_1 == 'x' and box_7 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.2
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_2 == 'x' and box_8 == 'o' :
                if box_7 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.3
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_8 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.4
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.26.5
            elif box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_8 == 'x' and box_2 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.27
            elif box_5 == 'x' and box_9 == 'o' and box_7 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        box_2 = 'o'
            # 5.28.1
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_1 == 'x' and box_3 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.28.2
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_3 == 'x' and box_7 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28.3
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' and box_6 == 'o' :
                if box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.28.4
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_6 == 'x' and box_4 == 'o' :
                if box_1 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28.5
            elif box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_7 == 'x' and box_3 == 'o' :
                if box_6 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.1
            elif box_6 == 'x' and box_5 == 'o' and box_1 == 'x' and box_3 == 'o' and box_7 == 'x' and box_4 == 'o' :
                if box_2 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_8 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_8 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_8 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.2
            elif box_6 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' and box_7 == 'x' and box_1 == 'o' :
                if box_9 == 'x' :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.3
            elif box_6 == 'x' and box_5 == 'o' and box_3 == 'x' and box_9 == 'o' and box_1 == 'x' and box_2 == 'o' :
                if box_8 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.4
            elif box_6 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        if computer_move == 1 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
            # 6.5
            elif box_6 == 'x' and box_5 == 'o' and box_7 == 'x' and box_9 == 'o' and box_1 == 'x' and box_4 == 'o' :
                if box_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_3
                        if computer_move == 2 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_2 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.6
            elif box_6 == 'x' and box_5 == 'o' and box_8 == 'x' and box_3 == 'o' and box_7 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.7
            elif box_6 == 'x' and box_5 == 'o' and box_9 == 'x' and box_3 == 'o' and box_7 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.1
            elif box_7 == 'x' and box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.2
            elif box_7 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' and box_8 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        box_1 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.3
            elif box_7 == 'x' and box_5 == 'o' and box_3 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.4
            elif box_7 == 'x' and box_5 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.5
            elif box_7 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' and box_1 == 'x' and box_4 == 'o' :
                if box_2 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_3
                        if computer_move == 2 :
                            box_3 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_2 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.6
            elif box_7 == 'x' and box_5 == 'o' and box_8 == 'x' and box_9 == 'o' and box_1 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_3
                    if computer_move == 2 :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.7
            elif box_7 == 'x' and box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.1
            elif box_8 == 'x' and box_5 == 'o' and box_1 == 'x' and box_7 == 'o' and box_3 == 'x' and box_2 == 'o' :
                if box_4 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_6 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'x' :
                        box_6 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.2
            elif box_8 == 'x' and box_5 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.3
            elif box_8 == 'x' and box_5 == 'o' and box_3 == 'x' and box_9 == 'o' and box_1 == 'x' and box_2 == 'o' :
                if box_4 == 'x' :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'x' :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.4
            elif box_8 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' and box_3 == 'x' and box_9 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.5
            elif box_8 == 'x' and box_5 == 'o' and box_6 == 'x' and box_9 == 'o' and box_1 == 'x' and box_3 == 'o' :
                if box_7 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.6
            elif box_8 == 'x' and box_5 == 'o' and box_7 == 'x' and box_9 == 'o' and box_1 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_3
                    if computer_move == 2 :
                        box_3 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.7
            elif box_8 == 'x' and box_5 == 'o' and box_9 == 'x' and box_7 == 'o' and box_3 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_2
                    if computer_move == 2 :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.1
            elif box_9 == 'x' and box_5 == 'o' and box_1 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' :
                if box_3 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.2
            elif box_9 == 'x' and box_5 == 'o' and box_2 == 'x' and box_3 == 'o' and box_7 == 'x' and box_8 == 'o' :
                if box_1 == 'x' :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'x' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_1 and 2 == box_4
                        if computer_move == 2 :
                            box_4 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_1 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.3
            elif box_9 == 'x' and box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.4
            elif box_9 == 'x' and box_5 == 'o' and box_4 == 'x' and box_7 == 'o' and box_3 == 'x' and box_6 == 'o' :
                if box_1 == 'x' :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'x' :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'x' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_1 and 2 == box_2
                        if computer_move == 2 :
                            box_2 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_1 = 'o'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.5
            elif box_9 == 'x' and box_5 == 'o' and box_6 == 'x' and box_3 == 'o' and box_7 == 'x' and box_8 == 'o' :
                if box_2 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.6
            elif box_9 == 'x' and box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' :
                if box_6 == 'x' :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.7
            elif box_9 == 'x' and box_5 == 'o' and box_8 == 'x' and box_7 == 'o' and box_3 == 'x' and box_6 == 'o' :
                if box_4 == 'x' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_2
                    if computer_move == 2 :
                        box_2 = 'o'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'o'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
        # 8th move (computer move)
        # 2st condition
        if userinput_2 == 'o' and win == False :
            sleep(2)
            # 1.7
            if box_1 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' and box_7 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_8 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'o' and box_5 == 'x' and box_3 == 'o' and box_2 == 'x' and box_8 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' and box_3 == 'o' and box_2 == 'x' :
                if box_8 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' and box_7 == 'o' and box_4 == 'x' :
                if box_2 == 'o' or box_8 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_7 == 'o' and box_4 == 'x' and box_6 == 'o' and box_2 == 'x' :
                if box_8 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_1 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' and box_3 == 'o' and box_2 == 'x' :
                if box_4 == 'o' or box_6 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_1 == 'o' and box_5 == 'x' and box_9 == 'o' and box_4 == 'x' and box_6 == 'o' and box_3 == 'x' :
                if box_7 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 2.7
            elif box_2 == 'o' and box_5 == 'x' and box_1 == 'o' and box_3 == 'x' and box_7 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'o' and box_5 == 'x' and box_3 == 'o' and box_1 == 'x' and box_9 == 'o' and box_6 == 'x' :
                if box_4 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' and box_7 == 'o' and box_9 == 'x' :
                if box_1 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'o' and box_5 == 'x' and box_7 == 'o' and box_1 == 'x' and box_9 == 'o' and box_8 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_2 == 'o' and box_5 == 'x' and box_8 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_2 == 'o' and box_5 == 'x' and box_9 == 'o' and box_3 == 'x' and box_7 == 'o' and box_8 == 'x' :
                if box_1 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 3.7
            elif box_3 == 'o' and box_5 == 'x' and box_1 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' :
                if box_4 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' and box_6 == 'x' :
                if box_4 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' and box_1 == 'o' and box_2 == 'x' :
                if box_8 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'o' and box_5 == 'x' and box_7 == 'o' and box_2 == 'x' and box_8 == 'o' and box_9 == 'x' :
                if box_1 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_3 == 'o' and box_5 == 'x' and box_8 == 'o' and box_9 == 'x' and box_1 == 'o' and box_2 == 'x' :
                if box_4 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_3 == 'o' and box_5 == 'x' and box_9 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 4.7
            elif box_4 == 'o' and box_5 == 'x' and box_1 == 'o' and box_7 == 'x' and box_3 == 'o' and box_2 == 'x' :
                if box_8 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'o' and box_5 == 'x' and box_3 == 'o' and box_1 == 'x' and box_9 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_4 == 'o' and box_5 == 'x' and box_6 == 'o' and box_1 == 'x' and box_9 == 'o' and box_3 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'o' and box_5 == 'x' and box_7 == 'o' and box_1 == 'x' and box_9 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' and box_3 == 'o' and box_1 == 'x' :
                if box_9 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            elif box_4 == 'o' and box_5 == 'x' and box_9 == 'o' and box_7 == 'x' and box_3 == 'o' and box_6 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.7
            # 5.1.1
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.1.1
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_7 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.1.2
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.1.3
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.1.4
            elif box_5 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_4 == 'x' :
                if box_7 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.2
            elif box_5 == 'o' and box_1 == 'x' and box_3 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.3.1
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_2 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_9 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 2 == box_9 and 1 == box_2
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.3.2
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.3.3
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.3.4
            elif box_5 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_7 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.4
            elif box_5 == 'o' and box_1 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.5
            elif box_5 == 'o' and box_1 == 'x' and box_7 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.6
            elif box_5 == 'o' and box_1 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.7
            elif box_5 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.14
            # 5.8
            elif box_5 == 'o' and box_3 == 'x' and box_1 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.9
            # 5.9.1
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_6 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                elif box_7 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
            # 5.9.2
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_9 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.9.3
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.9.4
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_6 == 'x' :
                if box_9 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.9.5
            elif box_5 == 'o' and box_3 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.10
            elif box_5 == 'o' and box_3 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11
            # 5.11.1
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.11.2
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.11.3
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_2 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11.4
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.11.5
            elif box_5 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.12
            elif box_5 == 'o' and box_3 == 'x' and box_7 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.13
            elif box_5 == 'o' and box_3 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.14
            elif box_5 == 'o' and box_3 == 'x' and box_9 == 'o' and box_1 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.15
            elif box_5 == 'o' and box_7 == 'x' and box_1 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.16
            elif box_5 == 'o' and box_7 == 'x' and box_2 == 'o' and box_8 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.17
            elif box_5 == 'o' and box_7 == 'x' and box_3 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.18.1
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.2
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_9 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.3
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_9 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.18.4
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.18.5
            elif box_5 == 'o' and box_7 == 'x' and box_4 == 'o' and box_6 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.19
            elif box_5 == 'o' and box_7 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.1
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_9 == 'x' :
                if box_3 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.20.2
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.3
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.20.4
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_1 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.20.5
            elif box_5 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' and box_9 == 'o' and box_1 == 'x' :
                if box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.21
            elif box_5 == 'o' and box_7 == 'x' and box_9 == 'o' and box_1 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.22
            elif box_5 == 'o' and box_9 == 'x' and box_1 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_7 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.23
            elif box_5 == 'o' and box_9 == 'x' and box_2 == 'o' and box_8 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.24
            elif box_5 == 'o' and box_9 == 'x' and box_3 == 'o' and box_7 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.25
            elif box_5 == 'o' and box_9 == 'x' and box_4 == 'o' and box_6 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.1
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_1 == 'o' and box_7 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.2
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_2 == 'o' and box_8 == 'x' :
                if box_7 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.3
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_8 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.26.4
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.26.5
            elif box_5 == 'o' and box_9 == 'x' and box_6 == 'o' and box_4 == 'x' and box_8 == 'o' and box_2 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.27
            elif box_5 == 'o' and box_9 == 'x' and box_7 == 'o' and box_3 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_8
                    if computer_move == 2 :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        box_2 = 'x'
            # 5.28.1
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_1 == 'o' and box_3 == 'x' :
                if box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.28.2
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_3 == 'o' and box_7 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28.3
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_4 == 'o' and box_6 == 'x' :
                if box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 5.28.4
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_6 == 'o' and box_4 == 'x' :
                if box_1 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 5.28.5
            elif box_5 == 'o' and box_9 == 'x' and box_8 == 'o' and box_2 == 'x' and box_7 == 'o' and box_3 == 'x' :
                if box_6 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.1
            elif box_6 == 'o' and box_5 == 'x' and box_1 == 'o' and box_3 == 'x' and box_7 == 'o' and box_4 == 'x' :
                if box_2 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_8 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_8 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_8 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_8 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.2
            elif box_6 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' and box_7 == 'o' and box_1 == 'x' :
                if box_9 == 'o' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.3
            elif box_6 == 'o' and box_5 == 'x' and box_3 == 'o' and box_9 == 'x' and box_1 == 'o' and box_2 == 'x' :
                if box_8 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.4
            elif box_6 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' and box_3 == 'x' :
                if box_7 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        sleep(1)
                        print('                             >>>>   YOU LOSE !   <<<<')
                        win = True
                    else :
                        if computer_move == 1 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                            sleep(1)
                            print('                             >>>>   YOU LOSE !   <<<<')
                            win = True
            # 6.5
            elif box_6 == 'o' and box_5 == 'x' and box_7 == 'o' and box_9 == 'x' and box_1 == 'o' and box_4 == 'x' :
                if box_2 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_3
                        if computer_move == 2 :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_2 = 'x'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 6.6
            elif box_6 == 'o' and box_5 == 'x' and box_8 == 'o' and box_3 == 'x' and box_7 == 'o' and box_9 == 'x' :
                if box_1 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 6.7
            elif box_6 == 'o' and box_5 == 'x' and box_9 == 'o' and box_3 == 'x' and box_7 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.1
            elif box_7 == 'o' and box_5 == 'x' and box_1 == 'o' and box_4 == 'x' and box_6 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.2
            elif box_7 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' and box_8 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        box_1 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.3
            elif box_7 == 'o' and box_5 == 'x' and box_3 == 'o' and box_4 == 'x' and box_6 == 'o' and box_9 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.4
            elif box_7 == 'o' and box_5 == 'x' and box_4 == 'o' and box_1 == 'x' and box_9 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_3 and 2 == box_6
                    if computer_move == 2 :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.5
            elif box_7 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' and box_1 == 'o' and box_4 == 'x' :
                if box_2 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_2 and 2 == box_3
                        if computer_move == 2 :
                            box_3 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_2 = 'x'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 7.6
            elif box_7 == 'o' and box_5 == 'x' and box_8 == 'o' and box_9 == 'x' and box_1 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_3
                    if computer_move == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 7.7
            elif box_7 == 'o' and box_5 == 'x' and box_9 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.1
            elif box_8 == 'o' and box_5 == 'x' and box_1 == 'o' and box_7 == 'x' and box_3 == 'o' and box_2 == 'x' :
                if box_4 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_6 and 2 == box_9
                    if computer_move == 2 :
                        box_9 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_6 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_9 == 'o' :
                        box_6 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.2
            elif box_8 == 'o' and box_5 == 'x' and box_2 == 'o' and box_1 == 'x' and box_9 == 'o' and box_7 == 'x' :
                if box_3 == 'o' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.3
            elif box_8 == 'o' and box_5 == 'x' and box_3 == 'o' and box_9 == 'x' and box_1 == 'o' and box_2 == 'x' :
                if box_4 == 'o' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_6 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_4 and 2 == box_7
                    if computer_move == 2 :
                        box_7 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_7 == 'o' :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 8.4
            elif box_8 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' and box_3 == 'o' and box_9 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.5
            elif box_8 == 'o' and box_5 == 'x' and box_6 == 'o' and box_9 == 'x' and box_1 == 'o' and box_3 == 'x' :
                if box_7 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.6
            elif box_8 == 'o' and box_5 == 'x' and box_7 == 'o' and box_9 == 'x' and box_1 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_2 and 2 == box_3
                    if computer_move == 2 :
                        box_3 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 8.7
            elif box_8 == 'o' and box_5 == 'x' and box_9 == 'o' and box_7 == 'x' and box_3 == 'o' and box_6 == 'x' :
                if box_4 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_2
                    if computer_move == 2 :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.1
            elif box_9 == 'o' and box_5 == 'x' and box_1 == 'o' and box_6 == 'x' and box_4 == 'o' and box_7 == 'x' :
                if box_3 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.2
            elif box_9 == 'o' and box_5 == 'x' and box_2 == 'o' and box_3 == 'x' and box_7 == 'o' and box_8 == 'x' :
                if box_1 == 'o' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_4 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_6 == 'o' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_1 and 2 == box_4
                        if computer_move == 2 :
                            box_4 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_1 = 'x'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.3
            elif box_9 == 'o' and box_5 == 'x' and box_3 == 'o' and box_6 == 'x' and box_4 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.4
            elif box_9 == 'o' and box_5 == 'x' and box_4 == 'o' and box_7 == 'x' and box_3 == 'o' and box_6 == 'x' :
                if box_1 == 'o' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                elif box_2 == 'o' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    if box_8 == 'o' :
                        computer_move = random.randrange(1,3)
                        # 1 == box_1 and 2 == box_2
                        if computer_move == 2 :
                            box_2 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                        else :
                            if computer_move == 1 :
                                box_1 = 'x'
                                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
            # 9.5
            elif box_9 == 'o' and box_5 == 'x' and box_6 == 'o' and box_3 == 'x' and box_7 == 'o' and box_8 == 'x' :
                if box_2 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_4
                    if computer_move == 2 :
                        box_4 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.6
            elif box_9 == 'o' and box_5 == 'x' and box_7 == 'o' and box_8 == 'x' and box_2 == 'o' and box_4 == 'x' :
                if box_6 == 'o' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
            # 9.7
            elif box_9 == 'o' and box_5 == 'x' and box_8 == 'o' and box_7 == 'x' and box_3 == 'o' and box_6 == 'x' :
                if box_4 == 'o' :
                    computer_move = random.randrange(1,3)
                    # 1 == box_1 and 2 == box_2
                    if computer_move == 2 :
                        box_2 = 'x'
                        print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    else :
                        if computer_move == 1 :
                            box_1 = 'x'
                            print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                else :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   YOU LOSE !   <<<<')
                    win = True
        # 9rd move (Player move)
        while loop_7 and win == False :
            print('>> Please enter the Square box number to Play your move : ',end='')
            userinput_7 = input_function()
            print()
            if userinput_7 == '1' and box_1 == 'na' :
                if userinput_2 == 'x' :
                    box_1 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_1 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '2' and box_2 == 'na' :
                if userinput_2 == 'x' :
                    box_2 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_2 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '3' and box_3 == 'na' :
                if userinput_2 == 'x' :
                    box_3 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_3 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '4' and box_4 == 'na' :
                if userinput_2 == 'x' :
                    box_4 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_4 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '5' and box_5 == 'na' :
                if userinput_2 == 'x' :
                    box_5 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_5 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '6' and box_6 == 'na' :
                if userinput_2 == 'x' :
                    box_6 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_6 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '7' and box_7 == 'na' :
                if userinput_2 == 'x' :
                    box_7 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_7 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '8' and box_8 == 'na' :
                if userinput_2 == 'x' :
                    box_8 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_8 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            elif userinput_7 == '9' and box_9 == 'na' :
                if userinput_2 == 'x' :
                    box_9 = 'x'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
                else :
                    box_9 = 'o'
                    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                    sleep(1)
                    print('                             >>>>   GAME DRAW !   <<<<')
                    loop_7 = False
            else :
                print()
                print('                    >>>> WRONG INPUT ! <<<<')
                print()
def player_vs_player() :
    import random
    from time import sleep
    box_1 = 'na'
    box_2 = 'na'
    box_3 = 'na'
    box_4 = 'na'
    box_5 = 'na'
    box_6 = 'na'
    box_7 = 'na'
    box_8 = 'na'
    box_9 = 'na'
    win = False
    loop_1 = True
    loop_2 = True
    loop_3 = True
    loop_4 = True
    loop_5 = True
    loop_6 = True
    loop_7 = True
    loop_8 = True
    loop_9 = True
    tool = random.randrange(1,3)
    if tool == 2 :
        player1_tool = 'o'
        player2_tool = 'x'
        print('                 *-----------------------------------------*')
        print('                   >>   PLAYER 1 has O  |  PLAYER 2 has X')
        print('                 *-----------------------------------------*')
    else :
        if tool == 1 :
            player1_tool = 'x'
            player2_tool = 'o'
            print('                 *-----------------------------------------*')
            print('                   >>   PLAYER 1 has X  |  PLAYER 2 has O')
            print('                 *-----------------------------------------*')
    print()
    print()
    sleep(1)
    input('>>  PRESS Enter To Start :')
    print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
    sleep(1)
    # 1st move
    while loop_1 :
        print('>> PLAYER 1, Please enter the Square box number to Play : ',end='')
        userinput_1 = input_function()
        print()
        if userinput_1 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        elif userinput_1 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
            else :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_1 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    sleep(1)
    # 2nd move
    while loop_2 :
        print('>> PLAYER 2, Please enter the Square box number to Play : ',end='')
        userinput_2 = input_function()
        print()
        if userinput_2 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        elif userinput_2 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
            else :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_2 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    sleep(1)
    # 3rd move
    while loop_3 :
        print('>> PLAYER 1, Please enter the Square box number to Play : ',end='')
        userinput_3 = input_function()
        print()
        if userinput_3 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        elif userinput_3 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
            else :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_3 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    sleep(1)
    # 4th move
    while loop_4 :
        print('>> PLAYER 2, Please enter the Square box number to Play : ',end='')
        userinput_4 = input_function()
        print()
        if userinput_4 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        elif userinput_4 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
            else :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_4 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    sleep(1)
    # 5th move
    while loop_5 :
        print('>> PLAYER 1, Please enter the Square box number to Play : ',end='')
        userinput_5 = input_function()
        print()
        if userinput_5 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        elif userinput_5 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
            else :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_5 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    # winner check after 5th move
    # box_1 and box_2 and box_3
    if box_1 == box_2 and box_2 == box_3 and box_1 != 'na' :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_4 and box_5 and box_6
    elif box_4 == box_5 and box_5 == box_6 and box_4 != 'na' :
        if box_4 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_4 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_7 and box_8 and box_9
    elif box_7 == box_8 and box_8 == box_9 and box_7 != 'na' :
        if box_7 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_7 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_4 and box_7
    elif box_1 == box_4 and box_4 == box_7 and box_1 != 'na' :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_2 and box_5 and box_8
    elif box_2 == box_5 and box_5 == box_8 and box_2 != 'na' :
        if box_2 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_2 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_6 and box_9
    elif box_3 == box_6 and box_6 == box_9 and box_3 != 'na' :
        if box_3 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_3 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_5 and box_9
    elif box_1 == box_5 and box_5 == box_9 and box_1 != 'na' :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_5 and box_7
    else :
        if box_3 == box_5 and box_5 == box_7 and box_3 != 'na' :
            if box_3 == 'x' :
                if player1_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
                else :
                    if player2_tool == 'x' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
            else :
                if box_3 == 'o' :
                    if player1_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 1 Wins !  <<<<')
                        win = True
                else :
                    if player2_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
    sleep(1)
    # 6th move
    while loop_6 and win == False :
        print('>> PLAYER 2, Please enter the Square box number to Play : ',end='')
        userinput_6 = input_function()
        print()
        if userinput_6 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        elif userinput_6 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
            else :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_6 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    # winner check after 6th move
    # box_1 and box_2 and box_3
    if box_1 == box_2 and box_2 == box_3 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_4 and box_5 and box_6
    elif box_4 == box_5 and box_5 == box_6 and box_4 != 'na' and win == False :
        if box_4 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_4 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_7 and box_8 and box_9
    elif box_7 == box_8 and box_8 == box_9 and box_7 != 'na' and win == False :
        if box_7 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_7 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_4 and box_7
    elif box_1 == box_4 and box_4 == box_7 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_2 and box_5 and box_8
    elif box_2 == box_5 and box_5 == box_8 and box_2 != 'na' and win == False :
        if box_2 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_2 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_6 and box_9
    elif box_3 == box_6 and box_6 == box_9 and box_3 != 'na' and win == False :
        if box_3 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_3 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_5 and box_9
    elif box_1 == box_5 and box_5 == box_9 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_5 and box_7
    else :
        if box_3 == box_5 and box_5 == box_7 and box_3 != 'na' and win == False :
            if box_3 == 'x' :
                if player1_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
                else :
                    if player2_tool == 'x' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
            else :
                if box_3 == 'o' :
                    if player1_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 1 Wins !  <<<<')
                        win = True
                else :
                    if player2_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
    sleep(1)
    # 7th move
    while loop_7 and win == False :
        print('>> PLAYER 1, Please enter the Square box number to Play : ',end='')
        userinput_7 = input_function()
        print()
        if userinput_7 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        elif userinput_7 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
            else :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_7 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    # winner check after 7th move
    # box_1 and box_2 and box_3
    if box_1 == box_2 and box_2 == box_3 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_4 and box_5 and box_6
    elif box_4 == box_5 and box_5 == box_6 and box_4 != 'na' and win == False :
        if box_4 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_4 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_7 and box_8 and box_9
    elif box_7 == box_8 and box_8 == box_9 and box_7 != 'na' and win == False :
        if box_7 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_7 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_4 and box_7
    elif box_1 == box_4 and box_4 == box_7 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_2 and box_5 and box_8
    elif box_2 == box_5 and box_5 == box_8 and box_2 != 'na' and win == False :
        if box_2 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_2 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_6 and box_9
    elif box_3 == box_6 and box_6 == box_9 and box_3 != 'na' and win == False :
        if box_3 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_3 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_5 and box_9
    elif box_1 == box_5 and box_5 == box_9 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_5 and box_7
    else :
        if box_3 == box_5 and box_5 == box_7 and box_3 != 'na' and win == False :
            if box_3 == 'x' :
                if player1_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
                else :
                    if player2_tool == 'x' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
            else :
                if box_3 == 'o' :
                    if player1_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 1 Wins !  <<<<')
                        win = True
                else :
                    if player2_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
    sleep(1)
    # 8th move
    while loop_8 and win == False :
        print('>> PLAYER 2, Please enter the Square box number to Play : ',end='')
        userinput_8 = input_function()
        print()
        if userinput_8 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        elif userinput_8 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
            else :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_8 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    # winner check after 8th move
    # box_1 and box_2 and box_3
    if box_1 == box_2 and box_2 == box_3 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_4 and box_5 and box_6
    elif box_4 == box_5 and box_5 == box_6 and box_4 != 'na' and win == False :
        if box_4 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_4 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_7 and box_8 and box_9
    elif box_7 == box_8 and box_8 == box_9 and box_7 != 'na' and win == False :
        if box_7 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_7 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_4 and box_7
    elif box_1 == box_4 and box_4 == box_7 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_2 and box_5 and box_8
    elif box_2 == box_5 and box_5 == box_8 and box_2 != 'na' and win == False :
        if box_2 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_2 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_6 and box_9
    elif box_3 == box_6 and box_6 == box_9 and box_3 != 'na' and win == False :
        if box_3 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_3 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_5 and box_9
    elif box_1 == box_5 and box_5 == box_9 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_5 and box_7
    else :
        if box_3 == box_5 and box_5 == box_7 and box_3 != 'na' and win == False :
            if box_3 == 'x' :
                if player1_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
                else :
                    if player2_tool == 'x' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
            else :
                if box_3 == 'o' :
                    if player1_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 1 Wins !  <<<<')
                        win = True
                else :
                    if player2_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
    sleep(1)
    # 9th move
    while loop_9 and win == False :
        print('>> PLAYER 1, Please enter the Square box number to Play : ',end='')
        userinput_9 = input_function()
        print()
        if userinput_9 == '1' and box_1 == 'na' :
            if tool == 2 :
                box_1 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_1 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '2' and box_2 == 'na' :
            if tool == 2 :
                box_2 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_2 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '3' and box_3 == 'na' :
            if tool == 2 :
                box_3 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_3 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '4' and box_4 == 'na' :
            if tool == 2 :
                box_4 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_4 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '5' and box_5 == 'na' :
            if tool == 2 :
                box_5 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_5 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '6' and box_6 == 'na' :
            if tool == 2 :
                box_6 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_6 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '7' and box_7 == 'na' :
            if tool == 2 :
                box_7 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_7 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '8' and box_8 == 'na' :
            if tool == 2 :
                box_8 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_8 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        elif userinput_9 == '9' and box_9 == 'na' :
            if tool == 2 :
                box_9 = 'o'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
            else :
                box_9 = 'x'
                print_function(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)
                loop_9 = False
        else :
            print()
            print('                    >>>> WRONG INPUT ! <<<<')
            print()
    # winner check after 9th move
    # box_1 and box_2 and box_3
    if box_1 == box_2 and box_2 == box_3 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_4 and box_5 and box_6
    elif box_4 == box_5 and box_5 == box_6 and box_4 != 'na' and win == False :
        if box_4 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_4 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_7 and box_8 and box_9
    elif box_7 == box_8 and box_8 == box_9 and box_7 != 'na' and win == False :
        if box_7 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_7 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_4 and box_7
    elif box_1 == box_4 and box_4 == box_7 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_2 and box_5 and box_8
    elif box_2 == box_5 and box_5 == box_8 and box_2 != 'na' and win == False :
        if box_2 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_2 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_6 and box_9
    elif box_3 == box_6 and box_6 == box_9 and box_3 != 'na' and win == False :
        if box_3 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_3 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_1 and box_5 and box_9
    elif box_1 == box_5 and box_5 == box_9 and box_1 != 'na' and win == False :
        if box_1 == 'x' :
            if player1_tool == 'x' :
                sleep(1)
                print('                            >>>>  Player 1 Wins !  <<<<')
                win = True
            else :
                if player2_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
        else :
            if box_1 == 'o' :
                if player1_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
            else :
                if player2_tool == 'o' :
                    sleep(1)
                    print('                            >>>>  Player 2 Wins !  <<<<')
                    win = True
    # box_3 and box_5 and box_7
    else :
        if box_3 == box_5 and box_5 == box_7 and box_3 != 'na' and win == False :
            if box_3 == 'x' :
                if player1_tool == 'x' :
                    sleep(1)
                    print('                            >>>>  Player 1 Wins !  <<<<')
                    win = True
                else :
                    if player2_tool == 'x' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
            else :
                if box_3 == 'o' :
                    if player1_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 1 Wins !  <<<<')
                        win = True
                else :
                    if player2_tool == 'o' :
                        sleep(1)
                        print('                            >>>>  Player 2 Wins !  <<<<')
                        win = True
    # Game DRAW condition
    if win == False :
        sleep(1)
        print('                          >>>>   GAME DRAW !   <<<<')
loop01 = True
from time import sleep
print()
sleep(1)
print('=========================================================================')
sleep(1)
print('                    \/      UNBEATABLE TIC-TAC-TOE      +--+             ')
print('                    /\                                  |__|             ')
print()
sleep(2)
print('   -->  GAME Developed By -: VIVEK KUMAR | GitHub -: vivek07kumar  <--')
sleep(0.5)
print('=========================================================================')
print()
print()
sleep(1)
while loop01 :
    loop02 = True
    loop03 = True
    print()
    print('              ================================================')
    print('              |   ____                |                      |')
    print('              |  | .. |       (._.)   |   (._.)       (._.)  |')
    print('              |  |____|   VS   <|>    |    <|>   VS    <|>   |')
    print('              |  \_____\      _/\_    |   _/\_        _/\_   |')
    print('              |                       |                      |')
    print('              | Computer  VS  Player  |  Player  VS   Player |')
    print('              |                       |                      |')
    print('              |                  <-- OR -->                  |')
    print('              ================================================')
    print()
    sleep(1)
    while loop03 :
        userinput02 = input('>> Press 1 to play against Computer | Press 2 to play against other Player : ')
        if userinput02 == '1' :
            print()
            print()
            computer_vs_player()
            print()
            loop03 = False
        elif userinput02 == '2' :
            print()
            print()
            print()
            print()
            player_vs_player()
            print()
            loop03 = False
        else :
            print('                               >>>> WRONG INPUT ! <<<<')
            print()
    sleep(1)
    while loop02 :
        print()
        userinput01 = input('>>  Press P to Play Again or Press E to Exit : ')
        if userinput01 == 'p' or userinput01 == 'P' or userinput01 == 'play again' or userinput01 == 'Play Again' or userinput01 == 'PLAY AGAIN' :
            loop02 = False
            print()
        elif userinput01 == 'e' or userinput01 == 'E' or userinput01 == 'exit' or userinput01 == 'EXIT' or userinput01 == 'Exit' :
            loop02 = False
            loop01 = False
            print()
            print()
        else :
            print()
            print('                               >>>> WRONG INPUT ! <<<<')
