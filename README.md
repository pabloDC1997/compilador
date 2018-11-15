## compilador
simples compilador utilizando RPLY, que gera uma arquivo .asm no padrão MIPS.

### entrada
No arquivo "codigo.txt" entre com uma expressão que siga a gramatica abaixo:
```
  programa  -> print(expressao)
  expressao -> expressao + expressao
            -> expressao - expressao
            -> expressao * expressao
            -> expressao / expressao
            -> expressao ^ expressao
            -> expressao % expressao
            -> numero
```       
### Como executar
  + pip install rply
  + run main.py

### Saída
  A execução irá gerar o "codigo.asm" que pode ser testado no simulador [<u>MARS</u>](http://courses.missouristate.edu/KenVollmar/mars/)
