from rply import ParserGenerator


class Parser:
    def __init__(self):

        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB', 'MULT', 'DIV', 'POT', 'RESTO'],
            precedence=[
                ("left", ['SUM', 'SUB']),
                ('left', ['MULT', 'DIV'])
                        ]
        )
        self.file = open("codigo.asm", "w")
        self.file.write(".data\n")
        self.file.write(".text\n")
        self.file.write(".global main\n")
        self.file.write("main:\n")
        print("\"codigo\" compilado com sucesso para \"./".__add__(self.file.name).__add__("\""))

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            self.file.write("\tmove $a0, $t1\n")
            self.file.write("\tli $v0, 1\n")
            self.file.write("\tsyscall\n")
            self.file.write("\tli $v0, 10\n")
            self.file.write("\tsyscall\n")
            self.file.write(".end main")

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression POT expression')
        @self.pg.production('expression : expression RESTO expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                flag = 0
                if left:
                    if right:
                        self.file.write("\tli $t1, ".__add__(str(left)).__add__("\n"))
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))
                        flag = 1

                if flag == 0:
                    if left:
                        self.file.write("\tli $t2, ".__add__(str(left)).__add__("\n"))
                    if right:
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))

                self.file.write("\tadd $t1, $t1, $t2\n")

            elif operator.gettokentype() == 'SUB':
                flag = 0
                if left:
                    if right:
                        self.file.write("\tli $t1, ".__add__(str(left)).__add__("\n"))
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))
                        flag = 1

                if flag == 0:
                    if left:
                        self.file.write("\tli $t2, ".__add__(str(left)).__add__("\n"))
                    if right:
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))

                self.file.write("\tsub $t1, $t1, $t2\n")

            elif operator.gettokentype() == 'MULT':
                flag = 0
                if left:
                    if right:
                        self.file.write("\tli $t1, ".__add__(str(left)).__add__("\n"))
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))
                        flag = 1

                if flag == 0:
                    if left:
                        self.file.write("\tli $t2, ".__add__(str(left)).__add__("\n"))
                    if right:
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))

                self.file.write("\tmul $t1, $t1, $t2\n")

            elif operator.gettokentype() == 'DIV':
                flag = 0
                if left:
                    if right:
                        self.file.write("\tli $t1, ".__add__(str(left)).__add__("\n"))
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))
                        flag = 1

                if flag == 0:
                    if left:
                        self.file.write("\tli $t2, ".__add__(str(left)).__add__("\n"))
                    if right:
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))

                self.file.write("\tdiv $t1, $t1, $t2\n")

            elif operator.gettokentype() == 'POT':# Not finished
                aux_x = left
                aux_y = int(right) - 1
                while aux_y > 0:
                    self.file.write("\tli $t2, ".__add__(str(aux_x)).__add__("\n"))
                    self.file.write("\tmul $t1, $t2, $t2\n")
                    aux_y = aux_y - 1

            elif operator.gettokentype() == 'RESTO':
                flag = 0
                interator = 1
                if left:
                    if right:
                        self.file.write("\tli $t1, ".__add__(str(left)).__add__("\n"))
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))
                        flag = 1

                if flag == 0:
                    if left:
                        self.file.write("\tli $t2, ".__add__(str(left)).__add__("\n"))
                    if right:
                        self.file.write("\tli $t2, ".__add__(str(right)).__add__("\n"))

                self.file.write("li $t1_aux, $t1 \n")
                self.file.write("li $t2_aux, $t2\n")
                self.file.write("li $interator, 0\n")

                self.file.write("loop:")
                self.file.write("\tadd $interator, interator, 1\n")
                self.file.write("\tadd $t1_aux, $t1_aux, $t2_aux\n")
                #FIXME testar condição de parada $t1_aux > t2_aux and goto loop if false
                self.file.write("fimLoop:\n")

                self.file.write("mul $t1_aux, $interator, $t2\n")
                self.file.write("sub $t1, $t1, $t1_aux\n")

        @self.pg.production('expression : NUMBER')
        def number(p):
            return p[0].value

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
