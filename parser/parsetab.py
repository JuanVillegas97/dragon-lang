
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSGREATEREQUALSNOTEQUALLESSTHANGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightASSIGNAND ASSIGN BOOLEAN CHAR COLON COMMA COMMENT CTEB CTEC CTEF CTEI CTES DIVIDE DO ELSE END EQUALS FLOAT FOR FROM FUNCTION GREATER GREATERTHAN ID IF INT LBRACE LBRACK LESS LESSTHAN LPAREN MAIN MINUS NOT NOTEQUAL OR PLUS PRINT PROGRAM RBRACE RBRACK READ RETURN RPAREN SEMICOLON STRING THEN TIMES VARIABLE VOID WHILE\n    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END\n    \n    global_scope : empty\n    \n    functions : functions function\n                    | function\n                    | empty\n    \n    function : FUNCTION function_signature function_body\n    \n    function_signature : simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n                    | VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n    \n    function_body : LBRACE statements return RBRACE\n                | LBRACE statements RBRACE\n    \n    function_1 : empty\n    \n    main : MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE\n    \n    main_scope : empty\n    \n    var_declarations : var_declaration_list\n                    | empty\n    \n    var_declaration_list : var_declaration var_declarations\n    \n    var_declaration : VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration\n    \n    open_var_declaration : empty\n    \n    close_var_declaration : empty\n    \n    variables : variable \n            | variable COMMA variables\n    \n    variable : ID\n            | ID LBRACK expression RBRACK\n            | ID LBRACK expression RBRACK LBRACK expression RBRACK\n    \n    parameters : parameters  COMMA parameter\n    | parameter\n    | empty\n    \n    parameter : simple_type ID \n    \n    statements : statements statement\n    | statement\n    | empty\n    \n    statement : read \n    | assing_to_call\n    | assingation\n    | for\n    | do_while\n    | while\n    | if_else\n    | invocation\n    | if\n    | return\n    | print\n    \n    assing_to_call : variable ASSIGN invocation\n    \n    do_while : DO breadcrumb LBRACE statements RBRACE WHILE LPAREN expression RPAREN gotot SEMICOLON \n    \n    for : FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO LBRACE statements RBRACE for_4\n    \n    for_1 : empty\n    \n    for_2 : empty\n    \n    for_3 : empty\n    \n    for_4 : empty\n    \n    while : WHILE breadcrumb LPAREN expression RPAREN gotof LBRACE statements RBRACE\n    \n    breadcrumb : empty\n    \n    if : IF LPAREN expression  RPAREN gotof LBRACE statements RBRACE\n    \n    if_else : IF LPAREN  expression  RPAREN  gotof LBRACE statements RBRACE  ELSE goto LBRACE statements RBRACE\n    \n    gotot : empty\n    \n    goto : empty\n    \n    gotof : empty\n    \n    return : RETURN expression SEMICOLON\n    \n    read : READ LPAREN variable_list RPAREN SEMICOLON\n    \n    variable_list : variable\n                  | variable_list COMMA variable\n    \n    invocation : ID invocation_1 LPAREN  invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6    \n    invocation_1 : empty\n    \n    invocation_2 : empty\n    \n    invocation_3 : empty\n    \n    invocation_4 : empty\n    \n    invocation_5 : empty\n    \n    invocation_6 : empty\n    \n    expressions : expressions COMMA invocation_4 expression invocation_3\n                | expression invocation_3\n                | empty\n    \n    expression : t_expression \n                | NOT t_expression\n    \n    print : PRINT LPAREN print_arguments RPAREN SEMICOLON\n    \n    print_arguments : print_argument\n                    | print_arguments COMMA print_argument\n    \n    print_argument : CTES\n                    | expression\n    \n    assingation : variable ASSIGN expression SEMICOLON\n    \n    t_expression : g_expression \n                | t_expression boolean_operator g_expression\n    \n    g_expression : m_expression \n                | g_expression comparison_operator m_expression\n    \n    m_expression : term \n                |  m_expression addition_operator term\n    \n    term : factor \n        |  term multiplication_operator factor\n    \n    factor : variable\n            | cte\n            | expression_parenthesis\n    \n    expression_parenthesis : LPAREN expression RPAREN \n    \n    comparison_operator : LESS\n                        | GREATER\n                        | EQUALS\n                        | NOTEQUAL\n                        | GREATERTHAN\n                        | LESSTHAN\n    \n    addition_operator : PLUS\n                    | MINUS\n    \n    boolean_operator : AND\n                    | OR\n    \n    multiplication_operator : TIMES\n                            | DIVIDE\n    \n    simple_type : INT\n                | FLOAT\n                | CHAR\n                | BOOLEAN\n    \n    cte : CTEI\n        | CTEF\n        | CTEC\n        | CTEB\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,30,],[0,-1,]),'ID':([2,23,24,25,26,27,28,29,33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,61,67,68,71,73,74,75,76,82,85,97,98,109,112,113,114,116,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,142,144,145,148,149,150,159,160,165,166,167,169,177,187,192,201,202,203,204,205,208,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[3,34,35,-103,-104,-105,-106,38,57,57,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,38,38,38,-41,-29,38,57,111,38,38,38,38,-43,-111,57,38,-57,38,-99,-100,38,-91,-92,-93,-94,-95,-96,38,-97,-98,38,-101,-102,57,38,-78,38,-63,57,38,179,38,57,-58,38,-73,-111,57,38,-65,38,57,57,38,-111,57,-52,-61,-67,-50,-44,57,57,57,-53,57,-111,-45,-49,]),'SEMICOLON':([3,36,37,38,57,83,84,86,87,88,89,90,91,92,93,94,95,96,103,110,120,141,143,153,154,155,156,157,158,186,196,199,200,218,222,223,],[4,66,-20,-22,-22,116,-71,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-21,145,-72,-23,167,-80,-82,-84,-86,-90,177,-111,-24,209,-66,-111,228,-54,]),'VARIABLE':([4,5,6,10,39,66,69,70,101,102,193,195,],[-111,11,-2,11,-111,-111,11,-13,-17,-19,11,11,]),'FUNCTION':([4,5,6,7,8,9,10,12,13,14,16,20,32,66,72,101,102,106,],[-111,-111,-2,15,-14,-15,-111,15,-4,-5,-16,-3,-6,-111,-10,-17,-19,-9,]),'MAIN':([4,5,6,7,8,9,10,12,13,14,16,20,32,66,72,101,102,106,],[-111,-111,-2,-111,-14,-15,-111,21,-4,-5,-16,-3,-6,-111,-10,-17,-19,-9,]),'LBRACE':([8,9,10,16,22,39,58,66,69,70,79,80,101,102,105,152,174,175,176,191,193,195,206,207,220,224,225,230,],[-14,-15,-111,-16,33,-111,-111,-111,-111,-13,113,-51,-17,-19,142,-111,-111,192,-56,204,-111,-111,-7,-8,-111,229,-55,232,]),'INT':([11,15,17,18,99,100,139,140,181,],[-111,25,25,-18,-111,-111,25,25,25,]),'FLOAT':([11,15,17,18,99,100,139,140,181,],[-111,26,26,-18,-111,-111,26,26,26,]),'CHAR':([11,15,17,18,99,100,139,140,181,],[-111,27,27,-18,-111,-111,27,27,27,]),'BOOLEAN':([11,15,17,18,99,100,139,140,181,],[-111,28,28,-18,-111,-111,28,28,28,]),'VOID':([15,],[24,]),'COMMA':([18,37,38,84,86,87,88,89,90,91,92,93,94,95,96,99,100,107,108,112,120,135,136,137,138,139,140,141,148,149,153,154,155,156,157,161,162,163,164,168,170,171,172,178,179,188,189,194,196,210,217,],[-18,67,-22,-71,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-111,-111,144,-59,-111,-72,159,-74,-76,-77,-111,-111,-23,-111,-63,-80,-82,-84,-86,-90,181,-26,-27,181,-60,187,-111,-70,-75,-28,-69,-64,-25,-24,-111,-68,]),'RPAREN':([18,31,38,84,86,87,88,89,90,91,92,93,94,95,96,99,100,102,107,108,112,115,120,134,135,136,137,138,139,140,141,148,149,151,153,154,155,156,157,161,162,163,164,168,170,171,172,178,179,180,182,188,189,194,196,210,211,214,217,],[-18,39,-22,-71,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-111,-111,-19,143,-59,-111,152,-72,157,158,-74,-76,-77,-111,-111,-23,-111,-63,174,-80,-82,-84,-86,-90,-111,-26,-27,-111,-60,186,-111,-70,-75,-28,193,195,-69,-64,-25,-24,-111,218,221,-68,]),'END':([19,184,],[30,-12,]),'LPAREN':([21,34,35,54,56,57,59,60,61,62,63,64,65,68,75,77,78,80,81,82,85,97,98,112,114,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,148,149,159,165,169,187,190,201,202,203,208,],[31,-111,-111,74,76,-111,-111,82,97,98,99,-11,100,97,97,112,-62,-51,114,97,97,97,97,-111,97,97,-99,-100,97,-91,-92,-93,-94,-95,-96,97,-97,-98,97,-101,-102,97,-63,97,97,97,-111,203,97,-65,97,97,]),'RBRACE':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[-111,72,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,106,-29,-43,-111,-57,-111,-78,173,184,-58,-73,-111,-111,213,-111,219,-52,-61,-67,-50,-44,-111,233,-111,-53,235,-111,-45,-49,]),'RETURN':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[61,61,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,61,-57,61,-78,61,61,-58,-73,61,61,61,-111,61,-52,-61,-67,-50,-44,61,61,61,-53,61,-111,-45,-49,]),'READ':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[54,54,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,54,-57,54,-78,54,54,-58,-73,54,54,54,-111,54,-52,-61,-67,-50,-44,54,54,54,-53,54,-111,-45,-49,]),'FOR':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[56,56,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,56,-57,56,-78,56,56,-58,-73,56,56,56,-111,56,-52,-61,-67,-50,-44,56,56,56,-53,56,-111,-45,-49,]),'DO':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,221,226,227,228,229,231,232,233,234,235,236,237,],[58,58,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,58,-57,58,-78,58,58,-58,-73,58,58,58,-111,58,-52,-61,-67,-50,-111,230,-48,-44,58,58,58,-53,58,-111,-45,-49,]),'WHILE':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,173,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[59,59,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,59,-57,59,-78,59,59,-58,190,-73,59,59,59,-111,59,-52,-61,-67,-50,-44,59,59,59,-53,59,-111,-45,-49,]),'IF':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[60,60,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,60,-57,60,-78,60,60,-58,-73,60,60,60,-111,60,-52,-61,-67,-50,-44,60,60,60,-53,60,-111,-45,-49,]),'PRINT':([33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,71,73,109,113,116,142,145,150,166,167,177,192,204,205,209,212,213,215,216,219,228,229,231,232,233,234,235,236,237,],[62,62,-41,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-41,-29,-43,62,-57,62,-78,62,62,-58,-73,62,62,62,-111,62,-52,-61,-67,-50,-44,62,62,62,-53,62,-111,-45,-49,]),'TIMES':([38,57,88,89,90,91,92,93,94,95,96,141,155,156,157,196,],[-22,-22,132,-85,-87,-88,-89,-107,-108,-109,-110,-23,132,-86,-90,-24,]),'DIVIDE':([38,57,88,89,90,91,92,93,94,95,96,141,155,156,157,196,],[-22,-22,133,-85,-87,-88,-89,-107,-108,-109,-110,-23,133,-86,-90,-24,]),'PLUS':([38,57,87,88,89,90,91,92,93,94,95,96,141,154,155,156,157,196,],[-22,-22,129,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,129,-84,-86,-90,-24,]),'MINUS':([38,57,87,88,89,90,91,92,93,94,95,96,141,154,155,156,157,196,],[-22,-22,130,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,130,-84,-86,-90,-24,]),'LESS':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,122,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,122,-82,-84,-86,-90,-24,]),'GREATER':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,123,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,123,-82,-84,-86,-90,-24,]),'EQUALS':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,124,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,124,-82,-84,-86,-90,-24,]),'NOTEQUAL':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,125,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,125,-82,-84,-86,-90,-24,]),'GREATERTHAN':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,126,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,126,-82,-84,-86,-90,-24,]),'LESSTHAN':([38,57,86,87,88,89,90,91,92,93,94,95,96,141,153,154,155,156,157,196,],[-22,-22,127,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-23,127,-82,-84,-86,-90,-24,]),'AND':([38,57,84,86,87,88,89,90,91,92,93,94,95,96,120,141,153,154,155,156,157,196,],[-22,-22,118,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,118,-23,-80,-82,-84,-86,-90,-24,]),'OR':([38,57,84,86,87,88,89,90,91,92,93,94,95,96,120,141,153,154,155,156,157,196,],[-22,-22,119,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,119,-23,-80,-82,-84,-86,-90,-24,]),'RBRACK':([38,84,86,87,88,89,90,91,92,93,94,95,96,104,120,141,153,154,155,156,157,183,196,],[-22,-71,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,141,-72,-23,-80,-82,-84,-86,-90,196,-24,]),'FROM':([38,84,86,87,88,89,90,91,92,93,94,95,96,120,141,153,154,155,156,157,185,196,197,198,],[-22,-71,-79,-81,-83,-85,-87,-88,-89,-107,-108,-109,-110,-72,-23,-80,-82,-84,-86,-90,-111,-24,208,-47,]),'LBRACK':([38,57,141,],[68,68,165,]),'ASSIGN':([55,57,111,141,146,147,196,],[75,-22,-111,-23,169,-46,-24,]),'NOT':([61,68,75,82,97,98,112,114,148,149,159,165,169,187,201,202,203,208,],[85,85,85,85,85,85,-111,85,85,-63,85,85,85,-111,85,-65,85,85,]),'CTEI':([61,68,75,82,85,97,98,112,114,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,148,149,159,165,169,187,201,202,203,208,],[93,93,93,93,93,93,93,-111,93,93,-99,-100,93,-91,-92,-93,-94,-95,-96,93,-97,-98,93,-101,-102,93,-63,93,93,93,-111,93,-65,93,93,]),'CTEF':([61,68,75,82,85,97,98,112,114,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,148,149,159,165,169,187,201,202,203,208,],[94,94,94,94,94,94,94,-111,94,94,-99,-100,94,-91,-92,-93,-94,-95,-96,94,-97,-98,94,-101,-102,94,-63,94,94,94,-111,94,-65,94,94,]),'CTEC':([61,68,75,82,85,97,98,112,114,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,148,149,159,165,169,187,201,202,203,208,],[95,95,95,95,95,95,95,-111,95,95,-99,-100,95,-91,-92,-93,-94,-95,-96,95,-97,-98,95,-101,-102,95,-63,95,95,95,-111,95,-65,95,95,]),'CTEB':([61,68,75,82,85,97,98,112,114,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,148,149,159,165,169,187,201,202,203,208,],[96,96,96,96,96,96,96,-111,96,96,-99,-100,96,-91,-92,-93,-94,-95,-96,96,-97,-98,96,-101,-102,96,-63,96,96,96,-111,96,-65,96,96,]),'CTES':([98,159,],[137,137,]),'ELSE':([213,],[220,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global_scope':([4,],[5,]),'empty':([4,5,7,10,11,33,34,35,39,57,58,59,66,69,99,100,111,112,113,139,140,142,148,152,161,164,171,174,185,186,187,192,193,195,204,209,210,218,220,221,229,232,235,],[6,9,14,9,18,43,64,64,70,78,80,80,102,9,18,18,147,149,43,163,163,43,172,176,102,102,189,176,198,200,202,43,9,9,43,216,189,223,225,227,43,43,237,]),'var_declarations':([5,10,69,193,195,],[7,16,105,206,207,]),'var_declaration_list':([5,10,69,193,195,],[8,8,8,8,8,]),'var_declaration':([5,10,69,193,195,],[10,10,10,10,10,]),'functions':([7,],[12,]),'function':([7,12,],[13,20,]),'open_var_declaration':([11,99,100,],[17,139,140,]),'main':([12,],[19,]),'function_signature':([15,],[22,]),'simple_type':([15,17,139,140,181,],[23,29,160,160,160,]),'function_body':([22,],[32,]),'variables':([29,67,],[36,103,]),'variable':([29,33,40,61,67,68,74,75,82,85,97,98,113,114,117,121,128,131,142,144,148,150,159,165,166,169,192,201,203,204,205,208,212,229,231,232,234,],[37,55,55,90,37,90,108,90,90,90,90,90,55,90,90,90,90,90,55,168,90,55,90,90,55,90,55,90,90,55,55,90,55,55,55,55,55,]),'statements':([33,113,142,192,204,229,232,],[40,150,166,205,212,231,234,]),'return':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[41,71,41,41,41,41,41,41,41,41,41,41,41,41,]),'statement':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[42,73,42,42,73,73,42,42,73,73,42,73,42,73,]),'read':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'assing_to_call':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'assingation':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'for':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'do_while':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'while':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'if_else':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'invocation':([33,40,75,113,142,150,166,192,204,205,212,229,231,232,234,],[51,51,109,51,51,51,51,51,51,51,51,51,51,51,51,]),'if':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'print':([33,40,113,142,150,166,192,204,205,212,229,231,232,234,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'function_1':([34,35,],[63,65,]),'main_scope':([39,],[69,]),'invocation_1':([57,],[77,]),'breadcrumb':([58,59,],[79,81,]),'expression':([61,68,75,82,97,98,114,148,159,165,169,201,203,208,],[83,104,110,115,134,138,151,171,138,183,185,210,211,214,]),'t_expression':([61,68,75,82,85,97,98,114,148,159,165,169,201,203,208,],[84,84,84,84,120,84,84,84,84,84,84,84,84,84,84,]),'g_expression':([61,68,75,82,85,97,98,114,117,148,159,165,169,201,203,208,],[86,86,86,86,86,86,86,86,153,86,86,86,86,86,86,86,]),'m_expression':([61,68,75,82,85,97,98,114,117,121,148,159,165,169,201,203,208,],[87,87,87,87,87,87,87,87,87,154,87,87,87,87,87,87,87,]),'term':([61,68,75,82,85,97,98,114,117,121,128,148,159,165,169,201,203,208,],[88,88,88,88,88,88,88,88,88,88,155,88,88,88,88,88,88,88,]),'factor':([61,68,75,82,85,97,98,114,117,121,128,131,148,159,165,169,201,203,208,],[89,89,89,89,89,89,89,89,89,89,89,156,89,89,89,89,89,89,89,]),'cte':([61,68,75,82,85,97,98,114,117,121,128,131,148,159,165,169,201,203,208,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'expression_parenthesis':([61,68,75,82,85,97,98,114,117,121,128,131,148,159,165,169,201,203,208,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'close_var_declaration':([66,161,164,],[101,180,182,]),'variable_list':([74,],[107,]),'boolean_operator':([84,120,],[117,117,]),'comparison_operator':([86,153,],[121,121,]),'addition_operator':([87,154,],[128,128,]),'multiplication_operator':([88,155,],[131,131,]),'print_arguments':([98,],[135,]),'print_argument':([98,159,],[136,178,]),'for_1':([111,],[146,]),'invocation_2':([112,],[148,]),'parameters':([139,140,],[161,164,]),'parameter':([139,140,181,],[162,162,194,]),'expressions':([148,],[170,]),'gotof':([152,174,],[175,191,]),'invocation_3':([171,210,],[188,217,]),'for_2':([185,],[197,]),'invocation_5':([186,],[199,]),'invocation_4':([187,],[201,]),'invocation_6':([209,],[215,]),'gotot':([218,],[222,]),'goto':([220,],[224,]),'for_3':([221,],[226,]),'for_4':([235,],[236,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON global_scope var_declarations functions main END','program',8,'p_program','grammar.py',26),
  ('global_scope -> empty','global_scope',1,'p_global_scope','grammar.py',32),
  ('functions -> functions function','functions',2,'p_functions','grammar.py',49),
  ('functions -> function','functions',1,'p_functions','grammar.py',50),
  ('functions -> empty','functions',1,'p_functions','grammar.py',51),
  ('function -> FUNCTION function_signature function_body','function',3,'p_function','grammar.py',56),
  ('function_signature -> simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',61),
  ('function_signature -> VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',62),
  ('function_body -> LBRACE statements return RBRACE','function_body',4,'p_function_body','grammar.py',68),
  ('function_body -> LBRACE statements RBRACE','function_body',3,'p_function_body','grammar.py',69),
  ('function_1 -> empty','function_1',1,'p_function_1','grammar.py',81),
  ('main -> MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE','main',8,'p_main','grammar.py',100),
  ('main_scope -> empty','main_scope',1,'p_main_scope','grammar.py',110),
  ('var_declarations -> var_declaration_list','var_declarations',1,'p_var_declarations','grammar.py',122),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','grammar.py',123),
  ('var_declaration_list -> var_declaration var_declarations','var_declaration_list',2,'p_var_declaration_list','grammar.py',129),
  ('var_declaration -> VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration','var_declaration',6,'p_var_declaration','grammar.py',136),
  ('open_var_declaration -> empty','open_var_declaration',1,'p_open_var_declaration','grammar.py',146),
  ('close_var_declaration -> empty','close_var_declaration',1,'p_close_var_declaration','grammar.py',152),
  ('variables -> variable','variables',1,'p_variables','grammar.py',159),
  ('variables -> variable COMMA variables','variables',3,'p_variables','grammar.py',160),
  ('variable -> ID','variable',1,'p_variable','grammar.py',173),
  ('variable -> ID LBRACK expression RBRACK','variable',4,'p_variable','grammar.py',174),
  ('variable -> ID LBRACK expression RBRACK LBRACK expression RBRACK','variable',7,'p_variable','grammar.py',175),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','grammar.py',184),
  ('parameters -> parameter','parameters',1,'p_parameters','grammar.py',185),
  ('parameters -> empty','parameters',1,'p_parameters','grammar.py',186),
  ('parameter -> simple_type ID','parameter',2,'p_parameter','grammar.py',191),
  ('statements -> statements statement','statements',2,'p_statements','grammar.py',203),
  ('statements -> statement','statements',1,'p_statements','grammar.py',204),
  ('statements -> empty','statements',1,'p_statements','grammar.py',205),
  ('statement -> read','statement',1,'p_statement','grammar.py',210),
  ('statement -> assing_to_call','statement',1,'p_statement','grammar.py',211),
  ('statement -> assingation','statement',1,'p_statement','grammar.py',212),
  ('statement -> for','statement',1,'p_statement','grammar.py',213),
  ('statement -> do_while','statement',1,'p_statement','grammar.py',214),
  ('statement -> while','statement',1,'p_statement','grammar.py',215),
  ('statement -> if_else','statement',1,'p_statement','grammar.py',216),
  ('statement -> invocation','statement',1,'p_statement','grammar.py',217),
  ('statement -> if','statement',1,'p_statement','grammar.py',218),
  ('statement -> return','statement',1,'p_statement','grammar.py',219),
  ('statement -> print','statement',1,'p_statement','grammar.py',220),
  ('assing_to_call -> variable ASSIGN invocation','assing_to_call',3,'p_assing_to_call','grammar.py',225),
  ('do_while -> DO breadcrumb LBRACE statements RBRACE WHILE LPAREN expression RPAREN gotot SEMICOLON','do_while',11,'p_do_while','grammar.py',230),
  ('for -> FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO LBRACE statements RBRACE for_4','for',16,'p_for','grammar.py',235),
  ('for_1 -> empty','for_1',1,'p_for_1','grammar.py',240),
  ('for_2 -> empty','for_2',1,'p_for_2','grammar.py',253),
  ('for_3 -> empty','for_3',1,'p_for_3','grammar.py',281),
  ('for_4 -> empty','for_4',1,'p_for_4','grammar.py',317),
  ('while -> WHILE breadcrumb LPAREN expression RPAREN gotof LBRACE statements RBRACE','while',9,'p_while','grammar.py',361),
  ('breadcrumb -> empty','breadcrumb',1,'p_breadcrumb','grammar.py',367),
  ('if -> IF LPAREN expression RPAREN gotof LBRACE statements RBRACE','if',8,'p_if','grammar.py',373),
  ('if_else -> IF LPAREN expression RPAREN gotof LBRACE statements RBRACE ELSE goto LBRACE statements RBRACE','if_else',13,'p_if_else','grammar.py',379),
  ('gotot -> empty','gotot',1,'p_gotot','grammar.py',385),
  ('goto -> empty','goto',1,'p_goto','grammar.py',391),
  ('gotof -> empty','gotof',1,'p_gotof','grammar.py',397),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','grammar.py',403),
  ('read -> READ LPAREN variable_list RPAREN SEMICOLON','read',5,'p_read','grammar.py',414),
  ('variable_list -> variable','variable_list',1,'p_variable_list','grammar.py',423),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','grammar.py',424),
  ('invocation -> ID invocation_1 LPAREN invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6','invocation',9,'p_invocation','grammar.py',434),
  ('invocation_1 -> empty','invocation_1',1,'p_invocation_1','grammar.py',438),
  ('invocation_2 -> empty','invocation_2',1,'p_invocation_2','grammar.py',445),
  ('invocation_3 -> empty','invocation_3',1,'p_invocation_3','grammar.py',451),
  ('invocation_4 -> empty','invocation_4',1,'p_invocation_4','grammar.py',457),
  ('invocation_5 -> empty','invocation_5',1,'p_invocation_5','grammar.py',463),
  ('invocation_6 -> empty','invocation_6',1,'p_invocation_6','grammar.py',469),
  ('expressions -> expressions COMMA invocation_4 expression invocation_3','expressions',5,'p_expressions','grammar.py',475),
  ('expressions -> expression invocation_3','expressions',2,'p_expressions','grammar.py',476),
  ('expressions -> empty','expressions',1,'p_expressions','grammar.py',477),
  ('expression -> t_expression','expression',1,'p_expression','grammar.py',482),
  ('expression -> NOT t_expression','expression',2,'p_expression','grammar.py',483),
  ('print -> PRINT LPAREN print_arguments RPAREN SEMICOLON','print',5,'p_print','grammar.py',495),
  ('print_arguments -> print_argument','print_arguments',1,'p_print_arguments','grammar.py',500),
  ('print_arguments -> print_arguments COMMA print_argument','print_arguments',3,'p_print_arguments','grammar.py',501),
  ('print_argument -> CTES','print_argument',1,'p_print_argument','grammar.py',513),
  ('print_argument -> expression','print_argument',1,'p_print_argument','grammar.py',514),
  ('assingation -> variable ASSIGN expression SEMICOLON','assingation',4,'p_assingation','grammar.py',540),
  ('t_expression -> g_expression','t_expression',1,'p_t_expression','grammar.py',553),
  ('t_expression -> t_expression boolean_operator g_expression','t_expression',3,'p_t_expression','grammar.py',554),
  ('g_expression -> m_expression','g_expression',1,'p_g_expression','grammar.py',564),
  ('g_expression -> g_expression comparison_operator m_expression','g_expression',3,'p_g_expression','grammar.py',565),
  ('m_expression -> term','m_expression',1,'p_m_expression','grammar.py',575),
  ('m_expression -> m_expression addition_operator term','m_expression',3,'p_m_expression','grammar.py',576),
  ('term -> factor','term',1,'p_term','grammar.py',586),
  ('term -> term multiplication_operator factor','term',3,'p_term','grammar.py',587),
  ('factor -> variable','factor',1,'p_factor','grammar.py',597),
  ('factor -> cte','factor',1,'p_factor','grammar.py',598),
  ('factor -> expression_parenthesis','factor',1,'p_factor','grammar.py',599),
  ('expression_parenthesis -> LPAREN expression RPAREN','expression_parenthesis',3,'p_expression_parenthesis','grammar.py',610),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','grammar.py',617),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','grammar.py',618),
  ('comparison_operator -> EQUALS','comparison_operator',1,'p_comparison_operator','grammar.py',619),
  ('comparison_operator -> NOTEQUAL','comparison_operator',1,'p_comparison_operator','grammar.py',620),
  ('comparison_operator -> GREATERTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',621),
  ('comparison_operator -> LESSTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',622),
  ('addition_operator -> PLUS','addition_operator',1,'p_addition_operator','grammar.py',628),
  ('addition_operator -> MINUS','addition_operator',1,'p_addition_operator','grammar.py',629),
  ('boolean_operator -> AND','boolean_operator',1,'p_boolean_operator','grammar.py',635),
  ('boolean_operator -> OR','boolean_operator',1,'p_boolean_operator','grammar.py',636),
  ('multiplication_operator -> TIMES','multiplication_operator',1,'p_multiplication_operator','grammar.py',642),
  ('multiplication_operator -> DIVIDE','multiplication_operator',1,'p_multiplication_operator','grammar.py',643),
  ('simple_type -> INT','simple_type',1,'p_simple_type','grammar.py',649),
  ('simple_type -> FLOAT','simple_type',1,'p_simple_type','grammar.py',650),
  ('simple_type -> CHAR','simple_type',1,'p_simple_type','grammar.py',651),
  ('simple_type -> BOOLEAN','simple_type',1,'p_simple_type','grammar.py',652),
  ('cte -> CTEI','cte',1,'p_cte','grammar.py',658),
  ('cte -> CTEF','cte',1,'p_cte','grammar.py',659),
  ('cte -> CTEC','cte',1,'p_cte','grammar.py',660),
  ('cte -> CTEB','cte',1,'p_cte','grammar.py',661),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',669),
]
