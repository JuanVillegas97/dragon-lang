
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSGREATEREQUALSNOTEQUALLESSTHANGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightASSIGNAND ASSIGN BOOLEAN CHAR COLON COMMA COMMENT CTEB CTEC CTEF CTEI CTES DECRYPT DIVIDE DO ECDSA ECDSAKEY ELSE ENCRYPT END EQUALS FLOAT FOR FROM FUNCTION GENKEY GREATER GREATERTHAN HMAC ID IF INT LBRACE LBRACK LESS LESSTHAN LPAREN MAIN MINUS NOT NOTEQUAL OR PLUS PRINT PROGRAM RANDOM_SALT RBRACE RBRACK READ RETURN RPAREN SEMICOLON SHA_256 SPECIAL STRING THEN TIMES VARIABLE VOID WHILE\n    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END\n    \n    global_scope : empty\n    \n    functions : functions function\n                    | function\n                    | empty\n    \n    function : FUNCTION function_signature block\n    \n    function_signature : simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n                    | VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n    \n    return : RETURN expressions SEMICOLON\n    \n    function_1 : empty\n    \n    main : MAIN LPAREN RPAREN main_scope var_declarations block\n    \n    main_scope : empty\n    \n    var_declarations : var_declaration_list\n                    | empty\n    \n    var_declaration_list : var_declaration var_declarations\n    \n    var_declaration : VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration\n    \n    open_var_declaration : empty\n    \n    close_var_declaration : empty\n    \n    variables : variable \n            | variable COMMA variables\n    \n    variable : ID\n            | ID LBRACK expression RBRACK\n            | ID LBRACK expression RBRACK LBRACK expression RBRACK\n    \n    parameters : parameters  COMMA parameter\n    | parameter\n    | empty\n    \n    parameter : simple_type ID \n    \n    block : LBRACE block2 RBRACE\n    \n    block2 : block3\n           | empty\n    \n    block3 : statement block2\n    \n    statement : special_func \n    | assingation\n    | for\n    | do_while\n    | while\n    | if_else\n    | invocation\n    | if\n    | print\n    | read \n    \n    special_func : gen_key\n                | encrypt\n                | decrypt\n                | sha_256\n                | random_salt\n                | hmac\n                | ecdsa\n                | ecdsa_key\n    \n    ecdsa_key : ECDSAKEY LPAREN RPAREN SPECIAL ID SEMICOLON\n    \n    ecdsa : ECDSA LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON\n    \n    hmac : HMAC LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON\n    \n    random_salt : RANDOM_SALT LPAREN CTEI RPAREN SPECIAL ID SEMICOLON\n    \n    sha_256 : SHA_256 LPAREN ID RPAREN SPECIAL ID SEMICOLON\n    \n    gen_key : GENKEY LPAREN RPAREN SPECIAL ID SEMICOLON\n    \n    encrypt : ENCRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON\n    \n    decrypt : DECRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON\n    \n    read : READ LPAREN ID RPAREN SEMICOLON\n    \n    assing_to_call : variable ASSIGN invocation\n    \n    do_while : DO breadcrumb block WHILE LPAREN expression RPAREN gotot SEMICOLON \n    \n    for : FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO block for_4\n    \n    for_1 : empty\n    \n    for_2 : empty\n    \n    for_3 : empty\n    \n    for_4 : empty\n    \n    while : WHILE breadcrumb LPAREN expression RPAREN gotof block\n    \n    breadcrumb : empty\n    \n    if : IF LPAREN expression  RPAREN gotof block\n    \n    if_else : IF LPAREN  expression  RPAREN  gotof block  ELSE goto block\n    \n    gotot : empty\n    \n    goto : empty\n    \n    gotof : empty\n    \n    variable_list : variable\n                  | variable_list COMMA variable\n    \n    invocation : ID invocation_1 LPAREN  invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6 \n    \n    invocation_1 : empty\n    \n    invocation_2 : empty\n    \n    invocation_3 : empty\n    \n    invocation_4 : empty\n    \n    invocation_5 : empty\n    \n    invocation_6 : empty\n    \n    expressions : expressions COMMA invocation_4 expression invocation_3\n                | expression invocation_3\n                | empty\n    \n    expression : t_expression \n                | NOT t_expression\n    \n    print : PRINT LPAREN print_arguments RPAREN SEMICOLON\n    \n    print_arguments : print_argument\n                    | print_arguments COMMA print_argument\n    \n    print_argument : CTES\n                    | expression\n    \n    assingation : variable ASSIGN expression SEMICOLON\n    \n    t_expression : g_expression \n                | t_expression boolean_operator g_expression\n    \n    g_expression : m_expression \n                | g_expression comparison_operator m_expression\n    \n    m_expression : term \n                |  m_expression addition_operator term\n    \n    term : factor \n        |  term multiplication_operator factor\n    \n    factor : variable\n            | cte\n            | invocation\n            | expression_parenthesis\n    \n    expression_parenthesis : LPAREN expression RPAREN \n    \n    comparison_operator : LESS\n                        | GREATER\n                        | EQUALS\n                        | NOTEQUAL\n                        | GREATERTHAN\n                        | LESSTHAN\n    \n    addition_operator : PLUS\n                    | MINUS\n    \n    boolean_operator : AND\n                    | OR\n    \n    multiplication_operator : TIMES\n                            | DIVIDE\n    \n    simple_type : INT\n                | FLOAT\n                | CHAR\n                | BOOLEAN\n                | STRING\n    \n    cte : CTEI\n        | CTEF\n        | CTEC\n        | CTEB\n        | CTES\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,31,],[0,-1,]),'ID':([2,23,24,25,26,27,28,29,30,34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,83,84,87,89,90,96,97,98,100,101,102,104,105,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,172,175,176,181,183,184,185,188,189,190,191,196,202,206,210,212,216,217,228,233,234,241,250,251,253,255,256,257,258,259,260,263,264,275,276,278,279,280,281,282,283,288,289,290,],[3,35,36,-118,-119,-120,-121,-122,39,65,65,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,39,112,-28,112,132,112,112,141,143,144,145,147,148,112,112,-128,112,112,-114,-115,112,-106,-107,-108,-109,-110,-111,112,-112,-113,112,-116,-117,-92,112,-77,112,213,214,215,218,219,220,221,112,112,112,-87,-58,237,238,-128,-68,-55,-50,112,-79,-66,270,271,-54,-53,272,273,112,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'SEMICOLON':([3,37,38,39,111,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,131,152,156,180,182,197,198,199,200,201,213,220,227,237,238,245,248,249,252,264,266,267,270,271,272,273,275,276,],[4,82,-19,-21,-20,-21,-85,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,172,-22,-86,210,212,-94,-96,-98,-100,-105,234,241,-128,257,258,-23,264,-80,-128,-128,278,-70,280,281,282,283,-75,-81,]),'VARIABLE':([4,5,6,10,40,82,85,86,109,110,242,244,],[-128,11,-2,11,-128,-128,11,-12,-16,-18,11,11,]),'FUNCTION':([4,5,6,7,8,9,10,12,13,14,16,20,33,82,87,109,110,],[-128,-128,-2,15,-13,-14,-128,15,-4,-5,-15,-3,-6,-128,-28,-16,-18,]),'MAIN':([4,5,6,7,8,9,10,12,13,14,16,20,33,82,87,109,110,],[-128,-128,-2,-128,-13,-14,-128,21,-4,-5,-15,-3,-6,-128,-28,-16,-18,]),'LBRACE':([8,9,10,16,22,40,66,82,85,86,93,94,109,110,130,179,207,208,209,232,242,244,254,261,262,268,269,287,],[-13,-14,-128,-15,34,-128,-128,-128,-128,-12,34,-67,-16,-18,34,-128,-128,34,-72,34,-128,-128,-128,-7,-8,34,-71,34,]),'INT':([11,15,17,18,107,108,150,151,223,],[-128,25,25,-17,-128,-128,25,25,25,]),'FLOAT':([11,15,17,18,107,108,150,151,223,],[-128,26,26,-17,-128,-128,26,26,26,]),'CHAR':([11,15,17,18,107,108,150,151,223,],[-128,27,27,-17,-128,-128,27,27,27,]),'BOOLEAN':([11,15,17,18,107,108,150,151,223,],[-128,28,28,-17,-128,-128,28,28,28,]),'STRING':([11,15,17,18,107,108,150,151,223,],[-128,29,29,-17,-128,-128,29,29,29,]),'VOID':([15,],[24,]),'COMMA':([18,38,39,107,108,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,133,137,138,139,140,143,144,147,148,150,151,152,156,175,176,192,193,194,195,197,198,199,200,201,203,204,205,211,221,229,230,243,245,264,265,275,276,277,],[-17,83,-21,-128,-128,-21,-85,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-128,181,-88,-90,-91,184,185,188,189,-128,-128,-22,-86,-128,-77,223,-25,-26,223,-94,-96,-98,-100,-105,228,-128,-84,-89,-27,-83,-78,-24,-23,-128,-128,-75,-81,-82,]),'RPAREN':([18,32,99,106,107,108,110,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,137,138,139,140,141,145,146,150,151,152,156,170,175,176,178,192,193,194,195,197,198,199,200,201,203,204,205,211,214,215,218,219,221,222,224,229,230,231,243,245,264,265,274,275,276,277,],[-17,40,142,149,-128,-128,-18,-21,-85,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-128,179,180,-88,-90,-91,182,186,187,-128,-128,-22,-86,201,-128,-77,207,-128,-25,-26,-128,-94,-96,-98,-100,-105,227,-128,-84,-89,235,236,239,240,-27,242,244,-83,-78,252,-24,-23,-128,-128,284,-75,-81,-82,]),'END':([19,87,171,],[31,-28,-11,]),'LPAREN':([21,35,36,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,91,92,94,95,96,97,112,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,177,181,196,202,206,228,250,251,263,],[32,-128,-128,90,-128,-128,96,97,98,99,100,101,102,103,104,105,106,107,-10,108,129,129,133,-76,-67,135,129,129,-128,129,129,-128,129,129,-114,-115,129,-106,-107,-108,-109,-110,-111,129,-112,-113,129,-116,-117,129,-77,206,129,129,129,129,-128,129,-79,129,]),'RBRACE':([34,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,88,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[-128,87,-29,-30,-128,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-31,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'FOR':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[64,64,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'DO':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,284,285,286,288,289,290,],[66,66,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,287,-64,-128,-61,-65,]),'WHILE':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,134,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[67,67,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,177,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'IF':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[68,68,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'PRINT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[69,69,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'READ':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[70,70,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'GENKEY':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[71,71,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'ENCRYPT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[72,72,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'DECRYPT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[73,73,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'SHA_256':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[74,74,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'RANDOM_SALT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[75,75,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'HMAC':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[76,76,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'ECDSA':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[77,77,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'ECDSAKEY':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,87,172,210,212,233,234,241,253,257,258,264,275,276,278,279,280,281,282,283,288,289,290,],[78,78,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-28,-92,-87,-58,-68,-55,-50,-66,-54,-53,-128,-75,-81,-60,-69,-56,-57,-52,-51,-128,-61,-65,]),'LBRACK':([39,65,112,152,],[84,84,84,196,]),'ASSIGN':([63,65,132,152,173,174,245,],[89,-21,-128,-22,202,-62,-23,]),'NOT':([84,89,96,97,129,133,135,175,176,181,196,202,206,228,250,251,263,],[115,115,115,115,115,-128,115,115,-77,115,115,115,115,-128,115,-79,115,]),'CTEI':([84,89,96,97,103,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,181,196,202,206,228,250,251,263,],[124,124,124,124,146,124,124,-128,124,124,-114,-115,124,-106,-107,-108,-109,-110,-111,124,-112,-113,124,-116,-117,124,-77,124,124,124,124,-128,124,-79,124,]),'CTEF':([84,89,96,97,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,181,196,202,206,228,250,251,263,],[125,125,125,125,125,125,-128,125,125,-114,-115,125,-106,-107,-108,-109,-110,-111,125,-112,-113,125,-116,-117,125,-77,125,125,125,125,-128,125,-79,125,]),'CTEC':([84,89,96,97,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,181,196,202,206,228,250,251,263,],[126,126,126,126,126,126,-128,126,126,-114,-115,126,-106,-107,-108,-109,-110,-111,126,-112,-113,126,-116,-117,126,-77,126,126,126,126,-128,126,-79,126,]),'CTEB':([84,89,96,97,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,181,196,202,206,228,250,251,263,],[127,127,127,127,127,127,-128,127,127,-114,-115,127,-106,-107,-108,-109,-110,-111,127,-112,-113,127,-116,-117,127,-77,127,127,127,127,-128,127,-79,127,]),'CTES':([84,89,96,97,115,129,133,135,153,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,181,196,202,206,228,250,251,263,],[128,128,128,139,128,128,-128,128,128,-114,-115,128,-106,-107,-108,-109,-110,-111,128,-112,-113,128,-116,-117,128,-77,139,128,128,128,-128,128,-79,128,]),'ELSE':([87,233,],[-28,254,]),'TIMES':([112,118,119,120,121,122,123,124,125,126,127,128,139,152,199,200,201,245,264,275,276,],[-21,168,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,168,-100,-105,-23,-128,-75,-81,]),'DIVIDE':([112,118,119,120,121,122,123,124,125,126,127,128,139,152,199,200,201,245,264,275,276,],[-21,169,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,169,-100,-105,-23,-128,-75,-81,]),'PLUS':([112,117,118,119,120,121,122,123,124,125,126,127,128,139,152,198,199,200,201,245,264,275,276,],[-21,165,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,165,-98,-100,-105,-23,-128,-75,-81,]),'MINUS':([112,117,118,119,120,121,122,123,124,125,126,127,128,139,152,198,199,200,201,245,264,275,276,],[-21,166,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,166,-98,-100,-105,-23,-128,-75,-81,]),'LESS':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,158,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,158,-96,-98,-100,-105,-23,-128,-75,-81,]),'GREATER':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,159,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,159,-96,-98,-100,-105,-23,-128,-75,-81,]),'EQUALS':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,160,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,160,-96,-98,-100,-105,-23,-128,-75,-81,]),'NOTEQUAL':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,161,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,161,-96,-98,-100,-105,-23,-128,-75,-81,]),'GREATERTHAN':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,162,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,162,-96,-98,-100,-105,-23,-128,-75,-81,]),'LESSTHAN':([112,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,197,198,199,200,201,245,264,275,276,],[-21,163,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,163,-96,-98,-100,-105,-23,-128,-75,-81,]),'AND':([112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,156,197,198,199,200,201,245,264,275,276,],[-21,154,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,154,-94,-96,-98,-100,-105,-23,-128,-75,-81,]),'OR':([112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,139,152,156,197,198,199,200,201,245,264,275,276,],[-21,155,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-127,-22,155,-94,-96,-98,-100,-105,-23,-128,-75,-81,]),'RBRACK':([112,113,114,116,117,118,119,120,121,122,123,124,125,126,127,128,152,156,197,198,199,200,201,225,245,264,275,276,],[-21,152,-85,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-22,-86,-94,-96,-98,-100,-105,245,-23,-128,-75,-81,]),'FROM':([112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,152,156,197,198,199,200,201,226,245,246,247,264,275,276,],[-21,-85,-93,-95,-97,-99,-101,-102,-103,-104,-123,-124,-125,-126,-127,-22,-86,-94,-96,-98,-100,-105,-128,-23,263,-63,-128,-75,-81,]),'SPECIAL':([142,149,186,187,235,236,239,240,],[183,190,216,217,255,256,259,260,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global_scope':([4,],[5,]),'empty':([4,5,7,10,11,34,35,36,40,44,65,66,67,82,85,107,108,112,132,133,150,151,175,179,192,195,204,207,226,227,228,242,244,252,254,264,265,284,288,],[6,9,14,9,18,43,80,80,86,43,92,94,94,110,9,18,18,92,174,176,194,194,205,209,110,110,230,209,247,249,251,9,9,267,269,276,230,286,290,]),'var_declarations':([5,10,85,242,244,],[7,16,130,261,262,]),'var_declaration_list':([5,10,85,242,244,],[8,8,8,8,8,]),'var_declaration':([5,10,85,242,244,],[10,10,10,10,10,]),'functions':([7,],[12,]),'function':([7,12,],[13,20,]),'open_var_declaration':([11,107,108,],[17,150,151,]),'main':([12,],[19,]),'function_signature':([15,],[22,]),'simple_type':([15,17,150,151,223,],[23,30,191,191,191,]),'block':([22,93,130,208,232,268,287,],[33,134,171,233,253,279,288,]),'variables':([30,83,],[37,111,]),'variable':([30,34,44,83,84,89,96,97,115,129,135,153,157,164,167,175,181,196,202,206,250,263,],[38,63,63,38,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,]),'block2':([34,44,],[41,88,]),'block3':([34,44,],[42,42,]),'statement':([34,44,],[44,44,]),'special_func':([34,44,],[45,45,]),'assingation':([34,44,],[46,46,]),'for':([34,44,],[47,47,]),'do_while':([34,44,],[48,48,]),'while':([34,44,],[49,49,]),'if_else':([34,44,],[50,50,]),'invocation':([34,44,84,89,96,97,115,129,135,153,157,164,167,175,181,196,202,206,250,263,],[51,51,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,]),'if':([34,44,],[52,52,]),'print':([34,44,],[53,53,]),'read':([34,44,],[54,54,]),'gen_key':([34,44,],[55,55,]),'encrypt':([34,44,],[56,56,]),'decrypt':([34,44,],[57,57,]),'sha_256':([34,44,],[58,58,]),'random_salt':([34,44,],[59,59,]),'hmac':([34,44,],[60,60,]),'ecdsa':([34,44,],[61,61,]),'ecdsa_key':([34,44,],[62,62,]),'function_1':([35,36,],[79,81,]),'main_scope':([40,],[85,]),'invocation_1':([65,112,],[91,91,]),'breadcrumb':([66,67,],[93,95,]),'close_var_declaration':([82,192,195,],[109,222,224,]),'expression':([84,89,96,97,129,135,175,181,196,202,206,250,263,],[113,131,136,140,170,178,204,140,225,226,231,265,274,]),'t_expression':([84,89,96,97,115,129,135,175,181,196,202,206,250,263,],[114,114,114,114,156,114,114,114,114,114,114,114,114,114,]),'g_expression':([84,89,96,97,115,129,135,153,175,181,196,202,206,250,263,],[116,116,116,116,116,116,116,197,116,116,116,116,116,116,116,]),'m_expression':([84,89,96,97,115,129,135,153,157,175,181,196,202,206,250,263,],[117,117,117,117,117,117,117,117,198,117,117,117,117,117,117,117,]),'term':([84,89,96,97,115,129,135,153,157,164,175,181,196,202,206,250,263,],[118,118,118,118,118,118,118,118,118,199,118,118,118,118,118,118,118,]),'factor':([84,89,96,97,115,129,135,153,157,164,167,175,181,196,202,206,250,263,],[119,119,119,119,119,119,119,119,119,119,200,119,119,119,119,119,119,119,]),'cte':([84,89,96,97,115,129,135,153,157,164,167,175,181,196,202,206,250,263,],[121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,]),'expression_parenthesis':([84,89,96,97,115,129,135,153,157,164,167,175,181,196,202,206,250,263,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,]),'print_arguments':([97,],[137,]),'print_argument':([97,181,],[138,211,]),'boolean_operator':([114,156,],[153,153,]),'comparison_operator':([116,197,],[157,157,]),'addition_operator':([117,198,],[164,164,]),'multiplication_operator':([118,199,],[167,167,]),'for_1':([132,],[173,]),'invocation_2':([133,],[175,]),'parameters':([150,151,],[192,195,]),'parameter':([150,151,223,],[193,193,243,]),'expressions':([175,],[203,]),'gotof':([179,207,],[208,232,]),'invocation_3':([204,265,],[229,277,]),'for_2':([226,],[246,]),'invocation_5':([227,],[248,]),'invocation_4':([228,],[250,]),'gotot':([252,],[266,]),'goto':([254,],[268,]),'invocation_6':([264,],[275,]),'for_3':([284,],[285,]),'for_4':([288,],[289,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON global_scope var_declarations functions main END','program',8,'p_program','grammar.py',29),
  ('global_scope -> empty','global_scope',1,'p_global_scope','grammar.py',35),
  ('functions -> functions function','functions',2,'p_functions','grammar.py',51),
  ('functions -> function','functions',1,'p_functions','grammar.py',52),
  ('functions -> empty','functions',1,'p_functions','grammar.py',53),
  ('function -> FUNCTION function_signature block','function',3,'p_function','grammar.py',58),
  ('function_signature -> simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',71),
  ('function_signature -> VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',72),
  ('return -> RETURN expressions SEMICOLON','return',3,'p_return','grammar.py',79),
  ('function_1 -> empty','function_1',1,'p_function_1','grammar.py',92),
  ('main -> MAIN LPAREN RPAREN main_scope var_declarations block','main',6,'p_main','grammar.py',111),
  ('main_scope -> empty','main_scope',1,'p_main_scope','grammar.py',121),
  ('var_declarations -> var_declaration_list','var_declarations',1,'p_var_declarations','grammar.py',134),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','grammar.py',135),
  ('var_declaration_list -> var_declaration var_declarations','var_declaration_list',2,'p_var_declaration_list','grammar.py',141),
  ('var_declaration -> VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration','var_declaration',6,'p_var_declaration','grammar.py',149),
  ('open_var_declaration -> empty','open_var_declaration',1,'p_open_var_declaration','grammar.py',159),
  ('close_var_declaration -> empty','close_var_declaration',1,'p_close_var_declaration','grammar.py',165),
  ('variables -> variable','variables',1,'p_variables','grammar.py',172),
  ('variables -> variable COMMA variables','variables',3,'p_variables','grammar.py',173),
  ('variable -> ID','variable',1,'p_variable','grammar.py',186),
  ('variable -> ID LBRACK expression RBRACK','variable',4,'p_variable','grammar.py',187),
  ('variable -> ID LBRACK expression RBRACK LBRACK expression RBRACK','variable',7,'p_variable','grammar.py',188),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','grammar.py',197),
  ('parameters -> parameter','parameters',1,'p_parameters','grammar.py',198),
  ('parameters -> empty','parameters',1,'p_parameters','grammar.py',199),
  ('parameter -> simple_type ID','parameter',2,'p_parameter','grammar.py',205),
  ('block -> LBRACE block2 RBRACE','block',3,'p_block','grammar.py',219),
  ('block2 -> block3','block2',1,'p_block2','grammar.py',225),
  ('block2 -> empty','block2',1,'p_block2','grammar.py',226),
  ('block3 -> statement block2','block3',2,'p_block3','grammar.py',232),
  ('statement -> special_func','statement',1,'p_statement','grammar.py',240),
  ('statement -> assingation','statement',1,'p_statement','grammar.py',241),
  ('statement -> for','statement',1,'p_statement','grammar.py',242),
  ('statement -> do_while','statement',1,'p_statement','grammar.py',243),
  ('statement -> while','statement',1,'p_statement','grammar.py',244),
  ('statement -> if_else','statement',1,'p_statement','grammar.py',245),
  ('statement -> invocation','statement',1,'p_statement','grammar.py',246),
  ('statement -> if','statement',1,'p_statement','grammar.py',247),
  ('statement -> print','statement',1,'p_statement','grammar.py',248),
  ('statement -> read','statement',1,'p_statement','grammar.py',249),
  ('special_func -> gen_key','special_func',1,'p_special_func','grammar.py',257),
  ('special_func -> encrypt','special_func',1,'p_special_func','grammar.py',258),
  ('special_func -> decrypt','special_func',1,'p_special_func','grammar.py',259),
  ('special_func -> sha_256','special_func',1,'p_special_func','grammar.py',260),
  ('special_func -> random_salt','special_func',1,'p_special_func','grammar.py',261),
  ('special_func -> hmac','special_func',1,'p_special_func','grammar.py',262),
  ('special_func -> ecdsa','special_func',1,'p_special_func','grammar.py',263),
  ('special_func -> ecdsa_key','special_func',1,'p_special_func','grammar.py',264),
  ('ecdsa_key -> ECDSAKEY LPAREN RPAREN SPECIAL ID SEMICOLON','ecdsa_key',6,'p_ecdsa_key','grammar.py',269),
  ('ecdsa -> ECDSA LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON','ecdsa',9,'p_ecdsa','grammar.py',285),
  ('hmac -> HMAC LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON','hmac',9,'p_hmac','grammar.py',306),
  ('random_salt -> RANDOM_SALT LPAREN CTEI RPAREN SPECIAL ID SEMICOLON','random_salt',7,'p_random_salt','grammar.py',327),
  ('sha_256 -> SHA_256 LPAREN ID RPAREN SPECIAL ID SEMICOLON','sha_256',7,'p_sha_256','grammar.py',347),
  ('gen_key -> GENKEY LPAREN RPAREN SPECIAL ID SEMICOLON','gen_key',6,'p_gen_key','grammar.py',366),
  ('encrypt -> ENCRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON','encrypt',9,'p_encrypt','grammar.py',382),
  ('decrypt -> DECRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON','decrypt',9,'p_decrypt','grammar.py',403),
  ('read -> READ LPAREN ID RPAREN SEMICOLON','read',5,'p_read','grammar.py',424),
  ('assing_to_call -> variable ASSIGN invocation','assing_to_call',3,'p_assing_to_call','grammar.py',436),
  ('do_while -> DO breadcrumb block WHILE LPAREN expression RPAREN gotot SEMICOLON','do_while',9,'p_do_while','grammar.py',442),
  ('for -> FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO block for_4','for',14,'p_for','grammar.py',447),
  ('for_1 -> empty','for_1',1,'p_for_1','grammar.py',452),
  ('for_2 -> empty','for_2',1,'p_for_2','grammar.py',465),
  ('for_3 -> empty','for_3',1,'p_for_3','grammar.py',493),
  ('for_4 -> empty','for_4',1,'p_for_4','grammar.py',529),
  ('while -> WHILE breadcrumb LPAREN expression RPAREN gotof block','while',7,'p_while','grammar.py',573),
  ('breadcrumb -> empty','breadcrumb',1,'p_breadcrumb','grammar.py',579),
  ('if -> IF LPAREN expression RPAREN gotof block','if',6,'p_if','grammar.py',585),
  ('if_else -> IF LPAREN expression RPAREN gotof block ELSE goto block','if_else',9,'p_if_else','grammar.py',592),
  ('gotot -> empty','gotot',1,'p_gotot','grammar.py',599),
  ('goto -> empty','goto',1,'p_goto','grammar.py',605),
  ('gotof -> empty','gotof',1,'p_gotof','grammar.py',611),
  ('variable_list -> variable','variable_list',1,'p_variable_list','grammar.py',621),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','grammar.py',622),
  ('invocation -> ID invocation_1 LPAREN invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6','invocation',9,'p_invocation','grammar.py',632),
  ('invocation_1 -> empty','invocation_1',1,'p_invocation_1','grammar.py',640),
  ('invocation_2 -> empty','invocation_2',1,'p_invocation_2','grammar.py',648),
  ('invocation_3 -> empty','invocation_3',1,'p_invocation_3','grammar.py',656),
  ('invocation_4 -> empty','invocation_4',1,'p_invocation_4','grammar.py',664),
  ('invocation_5 -> empty','invocation_5',1,'p_invocation_5','grammar.py',672),
  ('invocation_6 -> empty','invocation_6',1,'p_invocation_6','grammar.py',678),
  ('expressions -> expressions COMMA invocation_4 expression invocation_3','expressions',5,'p_expressions','grammar.py',686),
  ('expressions -> expression invocation_3','expressions',2,'p_expressions','grammar.py',687),
  ('expressions -> empty','expressions',1,'p_expressions','grammar.py',688),
  ('expression -> t_expression','expression',1,'p_expression','grammar.py',693),
  ('expression -> NOT t_expression','expression',2,'p_expression','grammar.py',694),
  ('print -> PRINT LPAREN print_arguments RPAREN SEMICOLON','print',5,'p_print','grammar.py',706),
  ('print_arguments -> print_argument','print_arguments',1,'p_print_arguments','grammar.py',713),
  ('print_arguments -> print_arguments COMMA print_argument','print_arguments',3,'p_print_arguments','grammar.py',714),
  ('print_argument -> CTES','print_argument',1,'p_print_argument','grammar.py',726),
  ('print_argument -> expression','print_argument',1,'p_print_argument','grammar.py',727),
  ('assingation -> variable ASSIGN expression SEMICOLON','assingation',4,'p_assingation','grammar.py',753),
  ('t_expression -> g_expression','t_expression',1,'p_t_expression','grammar.py',767),
  ('t_expression -> t_expression boolean_operator g_expression','t_expression',3,'p_t_expression','grammar.py',768),
  ('g_expression -> m_expression','g_expression',1,'p_g_expression','grammar.py',778),
  ('g_expression -> g_expression comparison_operator m_expression','g_expression',3,'p_g_expression','grammar.py',779),
  ('m_expression -> term','m_expression',1,'p_m_expression','grammar.py',789),
  ('m_expression -> m_expression addition_operator term','m_expression',3,'p_m_expression','grammar.py',790),
  ('term -> factor','term',1,'p_term','grammar.py',800),
  ('term -> term multiplication_operator factor','term',3,'p_term','grammar.py',801),
  ('factor -> variable','factor',1,'p_factor','grammar.py',811),
  ('factor -> cte','factor',1,'p_factor','grammar.py',812),
  ('factor -> invocation','factor',1,'p_factor','grammar.py',813),
  ('factor -> expression_parenthesis','factor',1,'p_factor','grammar.py',814),
  ('expression_parenthesis -> LPAREN expression RPAREN','expression_parenthesis',3,'p_expression_parenthesis','grammar.py',825),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','grammar.py',832),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','grammar.py',833),
  ('comparison_operator -> EQUALS','comparison_operator',1,'p_comparison_operator','grammar.py',834),
  ('comparison_operator -> NOTEQUAL','comparison_operator',1,'p_comparison_operator','grammar.py',835),
  ('comparison_operator -> GREATERTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',836),
  ('comparison_operator -> LESSTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',837),
  ('addition_operator -> PLUS','addition_operator',1,'p_addition_operator','grammar.py',843),
  ('addition_operator -> MINUS','addition_operator',1,'p_addition_operator','grammar.py',844),
  ('boolean_operator -> AND','boolean_operator',1,'p_boolean_operator','grammar.py',850),
  ('boolean_operator -> OR','boolean_operator',1,'p_boolean_operator','grammar.py',851),
  ('multiplication_operator -> TIMES','multiplication_operator',1,'p_multiplication_operator','grammar.py',857),
  ('multiplication_operator -> DIVIDE','multiplication_operator',1,'p_multiplication_operator','grammar.py',858),
  ('simple_type -> INT','simple_type',1,'p_simple_type','grammar.py',864),
  ('simple_type -> FLOAT','simple_type',1,'p_simple_type','grammar.py',865),
  ('simple_type -> CHAR','simple_type',1,'p_simple_type','grammar.py',866),
  ('simple_type -> BOOLEAN','simple_type',1,'p_simple_type','grammar.py',867),
  ('simple_type -> STRING','simple_type',1,'p_simple_type','grammar.py',868),
  ('cte -> CTEI','cte',1,'p_cte','grammar.py',874),
  ('cte -> CTEF','cte',1,'p_cte','grammar.py',875),
  ('cte -> CTEC','cte',1,'p_cte','grammar.py',876),
  ('cte -> CTEB','cte',1,'p_cte','grammar.py',877),
  ('cte -> CTES','cte',1,'p_cte','grammar.py',878),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',886),
]
