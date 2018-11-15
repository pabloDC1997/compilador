## compilador
    Simples compilador utilizando RPLY, que gera um arquivo .asm no padrão MIPS.

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
  + pip install [rply.](https://pypi.org/project/rply/)
  + run main.py

### Saída
    A execução irá gerar um arquivo "codigo.asm" que pode ser testado no simulador [MARS.](http://courses.missouristate.edu/KenVollmar/mars/)
