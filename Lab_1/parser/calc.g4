grammar calc;
options {
    language = 'Python3';
}
prog : expr * EOF ;
expr
    : left=expr (op=POW right=expr)                       # Pow
    | left=expr op=(DIV|MUL) right=expr                 # DivMul
    | left=expr op=(ADD|SUB) right=expr                 # AddSub
    | LPAR expr RPAR                                    # ParS
    | sign=(SUB|ADD) expr                               # USign
    | DECIMAL                                           # Dec
    | NUMBER                                            # Num
    ;




POW: '^';
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
NUMBER: [0-9]+;

fragment SEP_DOT: '.';
COMA: ',';

DECIMAL: [0-9]* SEP_DOT [0-9]+;

LPAR: '(';
RPAR: ')';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines