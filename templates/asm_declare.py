# a declaration in ARM assembly for raspberry pi looks like this

# .balign 4
# [NAME_OF_VAR]: .[word/asciz/] [value]

# at end of file
# addr for calling the vars

# addr_[NAME_OF_VAR]: .[word/asciz/] [NAME_OF_VAR]

from string import Template
# import the constants trings from the asm files
from templates.utils.asm_constants import declaration_options, address_options

class ASM_DECLARE():
    # params for declaration
    declare_name = ''
    declare_type = ''
    declare_value = ''
    formed_code = ''
    formed_address = ''

    def __init__(self, declare_name, declare_type, declare_value):
        self.declare_name = declare_name
        self.declare_type = declare_type
        self.declare_value = declare_value

    def detect_type(self):
        if self.declare_type == 'char':
            self.formed_code = declaration_options['char']
        if self.declare_type == 'int':
            self.formed_code = declaration_options['int']
        if self.declare_type == 'boolean':
            self.formed_code = declaration_options['boolean']

    def get_address(self):
        if self.declare_type == 'char':
            self.formed_address = address_options['char']
        if self.declare_type == 'int':
            self.formed_address = address_options['int']
        if self.declare_type == 'boolean':
            self.formed_address = address_options['boolean']

    def build_template(self):
        # call the detect type
        self.detect_type()
        # generate the template based on the avail variabels
        temp = Template(self.formed_code)
        temp = temp.safe_substitute(name = self.declare_name, value = self.declare_value)
        # replace in the formed code
        self.formed_code = temp

        # BUILD THE ADDRESS
        self.get_address()
        # generate the addr
        temp2 = Template(self.formed_address)
        temp2 = temp2.safe_substitute(name = self.declare_name)
        # replace tehe addr 
        self.formed_address = temp2
    
# test
# a = ASM_DECLARE('my_int', 'int', 5)
# a = ASM_DECLARE('my_char', 'char', 'welp')
# a = ASM_DECLARE('my_bool', 'boolean', 0)

# a.build_template()
# print(a.formed_code)
# print(a.formed_address)