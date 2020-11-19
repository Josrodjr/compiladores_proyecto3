
# if ([A] [type comparison] [B]) {
#   [target if true]
# }
# else {
#   [target if false]
# }

from string import Template

# import the constants trings from the asm files
from utils.asm_constants import comparisons, if_options


class ASM_SIMPLE_IF():
    # PARAMS FOR IF
    avail_registry_A = ''
    avail_registry_B = ''
    type_comparison = ''
    target_if_true = ''
    target_if_false = ''
    formed_code = ''

    def __init__(self, avail_registry_A, avail_registry_B, type_comparison, target_if_true, target_if_false):
        self.avail_registry_A = avail_registry_A
        self.avail_registry_B = avail_registry_B
        self.type_comparison = type_comparison
        self.target_if_true = target_if_true
        self.target_if_false = target_if_false

    def detect_type_if(self):
        if self.target_if_false == '':
            self.formed_code = if_options['only_if']
        else:
            self.formed_code = if_options['if_else']

    def detect_comparison(self):
        self.type_comparison = comparisons[self.type_comparison]

    def build_template(self):
        # change type of comparison to ASM
        self.detect_comparison()
        # detect type of if
        self.detect_type_if()
        # change the params 
        if self.target_if_false == '':
            temp = Template(self.formed_code)
            temp = temp.safe_substitute(reg1 = self.avail_registry_A, reg2 = self.avail_registry_B, comp = self.type_comparison, t_true = self.target_if_true)
            # replace in the formed code
            self.formed_code = temp
        else:
            temp = Template(self.formed_code)
            temp = temp.safe_substitute(reg1 = self.avail_registry_A, reg2 = self.avail_registry_B, comp = self.type_comparison, t_true = self.target_if_true, t_false = self.target_if_false)
            # replace in the formed code
            self.formed_code = temp


# testing area
# a = ASM_SIMPLE_IF('r1', 'r2', '<', 'true_target', '')
a = ASM_SIMPLE_IF('r1', 'r2', '>=', 'true_target', 'false_target')

# ask for build
a.build_template()

# print result
print(a.formed_code)