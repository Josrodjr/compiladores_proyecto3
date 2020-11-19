comparisons = {
    '<': 'blt',
    '<=': 'ble',
    '>': 'bgt',
    '>=': 'bge',
    '==': 'beq',
    '!=': 'bne'
}

conditions = {
    '==': 'eq',
    '!=': 'ne',
    '>': 'gt',
    '<': 'lt',
    '>=': 'ge',
    '<=': 'le'
}    

contrary_conditions = {
    'eq': 'ne',
    'ne': 'eq',
    'gt': 'le',
    'le': 'gt',
    'lt': 'ge',
    'ge': 'lt'
}

if_options = {
    'if_else': 'cmp $reg1, $reg2\n$comp $t_true\nb $t_false',
    'only_if': 'cmp $reg1, $reg2\n$comp $t_true'
}

# requires: reg1, reg2, comp, temp, contr, t_false
if_complex = {
    'if_false': 'cmp $reg1, $reg2\nite $comp\nstr$comp r0, [$temp]\nb$contr $t_false\n'
}

while_options = {
    'while': 'cmp $reg1, $reg2\n$comp $t_true'
}

declaration_options = {
    'char': '.balign 4\n$name: .asciz "$value"',
    'int': '.balign 4\n$name: .word $value',
    'boolean': '.balign 4\n$name: .word $value'
}

address_options = {
    'char': 'address_of_$name: .word $name',
    'int': 'address_of_$name: .word $name',
    'boolean': 'address_of_$name: .word $name'
}