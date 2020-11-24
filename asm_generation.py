
from templates import asm_declare

def delta_finder(input_file, start_search, end_search):
    start = input_file.find(start_search) + len(start_search)
    end = input_file.find(end_search)
    return input_file[start:end]


def fill_markers(input_file, markers):
    pairs = [['DATA START', 'TEXT START'], ['TEXT START', '-1']]
    for pair in pairs:
        markers[pair[0]] = delta_finder(input_file, pair[0], pair[1])
    
    return markers

def main(inter_code):

    complete_assembly = ""

    markers = {}
    markers = fill_markers(inter_code, markers)

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


    extlibs_assembly = external_libs(markers)
    complete_assembly += extlibs_assembly

    find_main(markers)

    return complete_assembly

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

    # test
    print(unmain_list)
    print(main_list)

        


