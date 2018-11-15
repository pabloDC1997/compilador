.data
.text
.global main
main:
	li $t1, 2
	li $t1, 4
	mul $t1, $t1, $t2
	li $t1, 3
	add $t1, $t1, $t2
	move $a0, $t1
	li $v0, 1
	syscall
	li $v0, 10
	syscall
.end main