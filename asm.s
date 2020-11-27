
.balign 4
tobinary_temp: .word 0
.balign 4
tobinary_printer: .word 0
.balign 4
main_n: .word 0
.balign 4
main_result: .word 0
.global main

main:
	ldr r4, main_n
	b tobinary
	ldr r3, [r0]
	str r3, main_result
	/* Exit procedures after main */
	mov r0, #0
	mov r7, #1
	swi 0
tobinary:
	ldr r10, main_n
	mov r1, r10, lsr #1
	cmp r1, #0
	movne r1, #1
	cmp r1, #1
	beq label_1
label_1:
	ldr r10, n
	mov r2, r10, lsr #1
	b tobinary
	ldr r1, [r0]
	ldr r10, main_n
	mov r1, r10, lsr #1
	str r1, tobinary_temp
	b printf
	ldr r2, [r0]
	str r2, tobinary_printer

.global printf
.global scanf
