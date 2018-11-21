.data
.text
.global main
main:
	li $t1, 10
	li $t2, 2
	mul $t1, $t1, $t2
	li $t2, 10
	add $t1, $t1, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 10
	mul $t1, $t2, $t2
	li $t2, 5
	div $t1, $t1, $t2
	add $t1, $t1, $t2
	move $a0, $t1
	li $v0, 1
	syscall
	li $v0, 10
	syscall
.end main