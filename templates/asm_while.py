# while ([A] [type comparison] [B]) {
#   [target if true]
# }

from string import Template

# import the constants trings from the asm files
from utils.asm_constants import comparisons, while_options

class ASM_SIMPLE_WHILE():
    # PARAMS FOR WHILE
    avail_registry_A = ''
    avail_registry_B = ''
    type_comparison = ''
    target_if_true = ''
    formed_code = ''

    def __init__(self, avail_registry_A, avail_registry_B, type_comparison, target_if_true):
        self.avail_registry_A = avail_registry_A
        self.avail_registry_B = avail_registry_B
        self.type_comparison = type_comparison
        self.target_if_true = target_if_true


    def get_init_string(self):
        self.formed_code = while_options['while']

    def detect_comparison(self):
        self.type_comparison = comparisons[self.type_comparison]

    def build_template(self):
        # change type of comparison to ASM
        self.detect_comparison()
        # init the string
        self.get_init_string()
        # change the params 

        temp = Template(self.formed_code)
        temp = temp.safe_substitute(reg1 = self.avail_registry_A, reg2 = self.avail_registry_B, comp = self.type_comparison, t_true = self.target_if_true)
        # replace in the formed code
        self.formed_code = temp


# test area
a = ASM_SIMPLE_WHILE('r1', 'r2', '>=', 'miloop')

# build
a.build_template()

# print
print(a.formed_code)
    