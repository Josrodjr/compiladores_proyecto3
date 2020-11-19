
# a simple [comp] consists of: [A] [type comparison] [B]
# if ([comp] ([AND/OR] [comp])*) {
#   [target if true]
# }
# else {
#   [target if false]
# }

from string import Template

# import the constants trings from the asm files
from utils.asm_constants import comparisons, conditions, contrary_conditions, if_options, if_complex

# stack implementation
from pythonds.basic import Stack

# the class will recive an array of comparisons [comp] ORDERED from outside to inside
# the class will recive an array of [AND/OR] or rather [||/&&]
# the clss will recive an array postfix of the operations required for the true if and the false if

# the logic is this
# reserve a registry with the value of the up to now executed code
# if it suceeds save the 1 or 0

operands = ["<=", ">=", ">", "<", "==", "=!", "&&", "||"]
rel_eq_op = ["<=", ">=", ">", "<" , "=="]

class ASM_COMPLEX_IF():
    args_list = []
    reserved_bool1 = 0
    reserved_bool2 = 0
    stack_args = ''
    list_completed = []
    formed_code = ''
    target_if_true = ''
    target_if_false = ''

    def __init__(self, args_list, target_if_true, target_if_false):
        self.args_list = args_list
        self.target_if_true = target_if_true
        self.target_if_false = target_if_false
        # init a empty stack
        self.stack_args = Stack()
        # insert each value in the args list into the stack
        for item in self.args_list[::-1]:
            self.stack_args.push(item)

    def detect_conditions(self, cmp):
        return conditions[cmp]

    def detect_contrary(self, cmp):
        return contrary_conditions[cmp]

    def detect_bool_available(self):
        if self.reserved_bool1 == 0:
            self.reserved_bool1 = 1
            return 'r_bool_1'
        if self.reserved_bool2 == 0:
            self.reserved_bool2 = 1
            return 'r_bool_1'

    def get_params(self):
        # peek the value in the stack
        temp_op1 = ''
        temp_op2 = ''

        while self.stack_args.size() > 0:
            # peek the value found in stack
            curr_val = self.stack_args.peek()

            if curr_val not in operands:
                if temp_op1 == '':
                    temp_op1 = self.stack_args.pop()
                if temp_op2 == '':
                    temp_op2 = self.stack_args.pop()
            else:
                # FOUND A OPERAND
                op = self.stack_args.pop()
                # generate the if code based on the operand
                if op in rel_eq_op:
                    # get the type of comparison and contrary
                    cond = self.detect_conditions(op)
                    contr = self.detect_contrary(cond)
                    temp = self.detect_bool_available()
                    # generate the template
                    template = Template(if_complex['if_false'])
                    # if reserved bool
                    # replace the values in template
                    template = template.safe_substitute(reg1 = temp_op1, reg2 = temp_op2, comp = cond, temp = temp, contr = contr, t_false = self.target_if_false)
                    # append to the completed code
                    self.formed_code = self.formed_code + template

                # IF IN CASE NOT IN THE BASIC OPERANDS IT IS && OR ||
                else:
                    # DOESNT DO ANYTHING UP TO NOW
                   op = 0  
                    

                    

# test area
# a = ASM_COMPLEX_IF(['r2', 'r1', '>', 'r1', 'r2', '==', '&&', 'sucasa', 'ddfa', '>', '||'])
# a.get_params()