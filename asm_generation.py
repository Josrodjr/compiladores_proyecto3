
from templates import asm_declare

avail_registers = ['r1','r2','r3','r4','r5','r6','r7','r8','r9']

def delta_finder(input_file, start_search, end_search):
    start = input_file.find(start_search) + len(start_search)
    end = input_file.find(end_search)
    return input_file[start:end]


def fill_markers(input_file, markers):
    pairs = [['DATA START', 'TEXT START'], ['TEXT START', '6af6c941-2b97-4163-9053-5b787a723261']]
    for pair in pairs:
        markers[pair[0]] = delta_finder(input_file, pair[0], pair[1])
    return markers

def main(inter_code):

    complete_assembly = ""

    markers = {}
    markers = fill_markers(inter_code, markers)

    # generate a list of main and unmain functions inside the text
    main_list = 0
    unmain_list = 0

    # delimit by enters
    markers['DATA START'] = markers['DATA START'].split('\n') 
    # remove empty spaces
    markers['DATA START'] = list(filter(None, markers['DATA START']))
    
    # same for the functions
    markers['TEXT START'] = markers['TEXT START'].split('\n') 
    # remove empty spaces
    markers['TEXT START'] = list(filter(None, markers['TEXT START']))


    # start by doing the declarations
    declr_assembly = declarations(markers)
    complete_assembly += declr_assembly

    # text functions split
    main_list = find_main(markers)
    unmain_list = find_unmain(markers)

    # test the processing of functions
    complete_assembly += '\n.global main\n'
    complete_assembly += process_main(main_list)

    # do the standard exit
    complete_assembly += do_exit()

    complete_assembly += process_unmain(unmain_list)

    complete_assembly += '\n'

    extlibs_assembly = external_libs(markers)
    complete_assembly += extlibs_assembly

    find_main(markers)

    return complete_assembly

def do_exit():
    generated_exit_asm = '\n\t/* Exit procedures after main */'
    generated_exit_asm += '\n\tmov r0, #0'
    generated_exit_asm += '\n\tmov r7, #1'
    generated_exit_asm += '\n\tswi 0'

    return generated_exit_asm

def declarations(markers):
    # iterate over the declarations
    decl_gen_code = ""
    for declaration in markers['DATA START']:
        temp = declaration.split(':')

        t_value = 0

        if temp[1] == 'int':
            t_value = 0

        if temp[1] == 'char':
            t_value = ""

        if temp[1] == 'boolean':
            t_value = 0

        temporary_gen = asm_declare.ASM_DECLARE(temp[0], temp[1], t_value)
        temporary_gen.build_template()
        # append to the final string

        
        decl_gen_code += temporary_gen.formed_code

    return decl_gen_code


def external_libs(markers):
    external_code_libs = ""

    external_code_libs += '\n.global printf'
    external_code_libs += '\n.global scanf'

    return external_code_libs


def find_main(markers):
    main_list = []
    unmain_list = []

    main_found = 0
    for term in markers['TEXT START']:

        if term == "main:":
            main_found = 1

        if main_found == 1:
            if term == "func end":
                main_list.append(term)
                # change flag
                main_found = 0
            else:
                main_list.append(term)

        # else if flag and not in main just append to the unmain list
        else:
            unmain_list.append(term)

    # return main list
    return main_list

def find_unmain(markers):
    main_list = []
    unmain_list = []

    main_found = 0
    for term in markers['TEXT START']:

        if term == "main:":
            main_found = 1

        if main_found == 1:
            if term == "func end":
                main_list.append(term)
                # change flag
                main_found = 0
            else:
                main_list.append(term)

        # else if flag and not in main just append to the unmain list
        else:
            unmain_list.append(term)

    # return main list
    return unmain_list

    
def process_main(main_list):
    # tab status para saber si tengo que colocar el tab character '\t' en el label
    tab_status = 0
    tab_character = '\t'

    formed_function = ''

    for i in range(len(main_list)):
    # for value in main_list:
        if main_list[i] =='main:':
            # add to formed function
            formed_function += '\n' + str(main_list[i])
            # change the tab status
            tab_status = 1

        else:
            # else if not the tag main:
            # could be the end or the beginning
            if main_list[i] == 'func start':
                tab_status = 1
            if main_list[i] == 'func end':
                tab_status = 0

            # could be anyting else
            # IF
            if 'if' in main_list[i]:
                # its an if remove the starting 3
                temp = main_list[i][3:]
                # split based on the jump
                temp = temp.split(' jump ')
                # temp1 has the register temp2 has the location
                formed_function += '\n' + tab_status*tab_character + 'cmp ' + temp[0] + ', #1'
                formed_function += '\n' + tab_status*tab_character + 'beq ' + temp[1]

            # its an assigment
            if '=' in main_list[i]:
                # could be an assigment of a function
                if 'func_call' in main_list[i]:
                    # split
                    temp = main_list[i].split(' func_call ')

                    # temp1 has the register and =, temp2 has the function
                    formed_function += '\n' + tab_status*tab_character + 'b ' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'ldr ' + temp[0][:-1] + ', [r0]'
                    continue

                # division
                if '/' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('/')
                    # temporal load for the division
                    formed_function += '\n' + tab_status*tab_character + 'ldr r10, ' + without_div[0]
                    formed_function += '\n' + tab_status*tab_character + 'mov ' + temp[0] + ', ' + 'r10' + ', lsr #1'
                    continue

                if '%' in main_list[i]:
                #     # split by the equal
                #     temp = main_list[i].split('=')
                #     without_div = temp[1].split('%')
                #     # temporal load for the module
                #     formed_function += '\n' + tab_status*tab_character + 'ldr r10, ' + without_div[0]
                #     formed_function += '\n' + tab_status*tab_character + 'mov ' + temp[0] + ', r10,' + ' mod #'+ without_div[1]
                    continue

                if '+' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('+')
                    formed_function += '\n' + tab_status*tab_character + 'add ' + temp[0] + ', ' + without_div[0] + ', #'+ without_div[1]
                    continue

                if '-' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('-')
                    formed_function += '\n' + tab_status*tab_character + 'sub ' + temp[0] + ', ' + without_div[0] + ', #'+ without_div[1]
                    continue

                if '!=' in main_list[i]:
                    temp = main_list[i].split('!=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1]+ ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movne ' + left_right[0] + ', #1'
                    continue

                if '==' in main_list[i]:
                    temp = main_list[i].split('==')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'moveq ' + left_right[0] + ', #1'
                    continue

                if '>' in main_list[i]:
                    temp = main_list[i].split('>')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1]  + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movgt ' + left_right[0] + ', #1'
                    continue

                if '<' in main_list[i]:
                    temp = main_list[i].split('<')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movlt ' + left_right[0] + ', #1'
                    continue

                if '>=' in main_list[i]:
                    temp = main_list[i].split('>=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movge ' + left_right[0] + ', #1'
                    continue

                if '<=' in main_list[i]:
                    temp = main_list[i].split('<=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movle ' + left_right[0] + ', #1'
                    continue

                # ASIGNACION si completo todo lo demas
                temp = main_list[i].split('=')
                op_type = ''
                if temp[0] in avail_registers:
                    op_type = 'ldr '
                    right = temp[1]
                    # fix bug of assignment of function
                    if temp[1] == '0':
                        # go back one iteration and retrieve the left side of the equation
                        prev_func = main_list[i-1].split('=')
                        right = prev_func[0]
                    formed_function += '\n' + tab_status*tab_character + op_type + temp[0] + ', ' + right

                else:
                    op_type = 'str '
                    right = temp[1]
                    # fix bug of assignment of function
                    if temp[1] == '0':
                        # go back one iteration and retrieve the left side of the equation
                        prev_func = main_list[i-1].split('=')
                        right = prev_func[0]
                    
                    if right in avail_registers:
                        formed_function += '\n' + tab_status*tab_character + op_type + right + ', ' + temp[0]
                    else:
                        formed_function += '\n' + tab_status*tab_character + op_type + '#' + right + ', ' + temp[0]

    return formed_function


def process_unmain(main_list):
    # tab status para saber si tengo que colocar el tab character '\t' en el label
    tab_status = 0
    tab_character = '\t'

    formed_function = ''

    for i in range(len(main_list)):
    # for value in main_list:
        if ':' in main_list[i]:
            # add to formed function
            formed_function += '\n' + str(main_list[i])
            # change the tab status
            tab_status = 1

        else:
            # else if not the tag main:
            # could be the end or the beginning
            if main_list[i] == 'func start':
                tab_status = 1
            if main_list[i] == 'func end':
                tab_status = 0

            # could be anyting else
            # IF
            if 'if' in main_list[i]:
                # its an if remove the starting 3
                temp = main_list[i][3:]
                # split based on the jump
                temp = temp.split(' jump ')
                # temp1 has the register temp2 has the location
                formed_function += '\n' + tab_status*tab_character + 'cmp ' + temp[0] + ', #1'
                formed_function += '\n' + tab_status*tab_character + 'beq ' + temp[1]

            # its an assigment
            if '=' in main_list[i]:
                # could be an assigment of a function
                if 'func_call' in main_list[i]:
                    # split
                    temp = main_list[i].split(' func_call ')

                    # temp1 has the register and =, temp2 has the function
                    formed_function += '\n' + tab_status*tab_character + 'b ' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'ldr ' + temp[0][:-1] + ', [r0]'
                    continue

                # division
                if '/' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('/')
                    # temporal load for the division
                    formed_function += '\n' + tab_status*tab_character + 'ldr r10, ' + without_div[0]
                    formed_function += '\n' + tab_status*tab_character + 'mov ' + temp[0] + ', ' + 'r10' + ', lsr #1'
                    continue

                if '%' in main_list[i]:
                #     # split by the equal
                #     temp = main_list[i].split('=')
                #     without_div = temp[1].split('%')
                #     # temporal load for the module
                #     formed_function += '\n' + tab_status*tab_character + 'ldr r10, ' + without_div[0]
                #     formed_function += '\n' + tab_status*tab_character + 'mov ' + temp[0] + ', r10,' + ' mod #'+ without_div[1]
                    continue

                if '+' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('+')
                    formed_function += '\n' + tab_status*tab_character + 'add ' + temp[0] + ', ' + without_div[0] + ', #'+ without_div[1]
                    continue

                if '-' in main_list[i]:
                    # split by the equal
                    temp = main_list[i].split('=')
                    without_div = temp[1].split('-')
                    formed_function += '\n' + tab_status*tab_character + 'sub ' + temp[0] + ', ' + without_div[0] + ', #'+ without_div[1]
                    continue

                if '!=' in main_list[i]:
                    temp = main_list[i].split('!=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1]+ ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movne ' + left_right[0] + ', #1'
                    continue

                if '==' in main_list[i]:
                    temp = main_list[i].split('==')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'moveq ' + left_right[0] + ', #1'
                    continue

                if '>' in main_list[i]:
                    temp = main_list[i].split('>')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1]  + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movgt ' + left_right[0] + ', #1'
                    continue

                if '<' in main_list[i]:
                    temp = main_list[i].split('<')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movlt ' + left_right[0] + ', #1'
                    continue

                if '>=' in main_list[i]:
                    temp = main_list[i].split('>=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movge ' + left_right[0] + ', #1'
                    continue

                if '<=' in main_list[i]:
                    temp = main_list[i].split('<=')
                    # temp0 has the left side and temp1 the left side of the inequity
                    left_right = temp[0].split('=')
                    #
                    formed_function += '\n' + tab_status*tab_character + 'cmp ' + left_right[1] + ', #' + temp[1]
                    formed_function += '\n' + tab_status*tab_character + 'movle ' + left_right[0] + ', #1'
                    continue

                # ASIGNACION si completo todo lo demas
                temp = main_list[i].split('=')
                op_type = ''

                if temp[0] in avail_registers:
                    op_type = 'ldr '
                    right = temp[1]
                    # fix bug of assignment of function
                    if temp[1] == '0':
                        # go back one iteration and retrieve the left side of the equation
                        prev_func = main_list[i-1].split('=')
                        right = prev_func[0]
                    formed_function += '\n' + tab_status*tab_character + op_type + temp[0] + ', ' + right

                else:
                    op_type = 'str '
                    right = temp[1]
                    # fix bug of assignment of function
                    if temp[1] == '0':
                        # go back one iteration and retrieve the left side of the equation
                        prev_func = main_list[i-1].split('=')
                        right = prev_func[0]

                    if right in avail_registers:
                        formed_function += '\n' + tab_status*tab_character + op_type + right + ', ' + temp[0]
                    else:
                        formed_function += '\n' + tab_status*tab_character + op_type + '#' + right + ', ' + temp[0]


                
    return formed_function
