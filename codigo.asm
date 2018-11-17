.data
.text
.global main
main:
	li $t2, 2
	mul $t1, $t2, $t2
	li $t2, 2
	mul $t1, $t2, $t2
	move $a0, $t1
	li $v0, 1
	syscall
	li $v0, 10
	syscall
.end main