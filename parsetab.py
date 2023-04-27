
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOLEAN CHAR COLON COMMA COMMENT CTEB CTEC CTEF CTEI CTES DIVIDE ELSE END EQUALS FALSE FLOAT FUNCTION GREATER ID IF INT LBRACE LBRACK LESS LPAREN MAIN MINUS NOTEQUAL OR PLUS PRINT PROGRAM RBRACE RBRACK RETURN RPAREN SEMICOLON STRING THEN TIMES TRUE VARIABLE WHILE\n    program : PROGRAM ID SEMICOLON var_declaration functions MAIN body END\n    \n    functions : functions function\n                    | function\n    \n    function : FUNCTION simple_type ID LPAREN parameters RPAREN body\n            | empty\n    \n    parameters : parameter_list\n                | empty\n    \n    parameter_list : parameter\n                    | parameter_list COMMA parameter\n    \n    parameter : simple_type ID \n    \n    body : LBRACE statement RBRACE\n    \n    statement : assingation\n            | empty\n    \n    assingation : variable ASSIGN expression SEMICOLON\n    \n    var_declaration : VARIABLE simple_type variables SEMICOLON\n                    | empty\n    \n    variables : variables COMMA variable\n            | variable\n    \n    variable : ID\n            | ID LBRACK expression RBRACK\n            | ID LBRACK expression RBRACK LBRACK expression RBRACK\n    \n    simple_type : INT\n                | FLOAT\n                | CHAR\n                | STRING\n                | BOOLEAN\n    \n    expression : t_expression \n            | t_expression ASSIGN t_expression\n    \n    t_expression : g_expression \n                | g_expression AND g_expression\n                | g_expression OR  g_expression\n    \n    g_expression : m_expression \n                | m_expression LESS     m_expression\n                | m_expression GREATER  m_expression\n                | m_expression EQUALS   m_expression\n                | m_expression NOTEQUAL m_expression\n    \n    m_expression : term \n                | term PLUS term\n                | term MINUS term\n    \n    term : factor \n        | factor TIMES factor\n        | factor DIVIDE factor\n    \n    factor : variable\n        | cte\n        | LPAREN expression RPAREN \n    \n    cte : CTEI\n        | CTEF\n        | CTEC\n        | CTES\n        | CTEB\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,30,],[0,-1,]),'ID':([2,12,13,14,15,16,17,20,25,28,29,45,52,53,59,60,61,62,63,64,65,66,67,68,69,75,],[3,23,-22,-23,-24,-25,-26,26,23,23,23,23,23,72,23,23,23,23,23,23,23,23,23,23,23,23,]),'SEMICOLON':([3,21,22,23,36,38,39,40,41,42,43,44,46,47,48,49,50,58,71,76,77,78,79,80,81,82,83,84,85,86,87,92,],[4,27,-18,-19,-17,-27,-29,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,88,-28,-30,-31,-33,-34,-35,-36,-38,-39,-41,-42,-45,-21,]),'VARIABLE':([4,],[6,]),'FUNCTION':([4,5,7,8,9,11,19,27,51,89,],[-51,10,-16,10,-3,-5,-2,-15,-11,-4,]),'MAIN':([4,5,7,8,9,11,19,27,51,89,],[-51,-51,-16,18,-3,-5,-2,-15,-11,-4,]),'INT':([6,10,35,74,],[13,13,13,13,]),'FLOAT':([6,10,35,74,],[14,14,14,14,]),'CHAR':([6,10,35,74,],[15,15,15,15,]),'STRING':([6,10,35,74,],[16,16,16,16,]),'BOOLEAN':([6,10,35,74,],[17,17,17,17,]),'LBRACE':([18,73,],[25,25,]),'COMMA':([21,22,23,36,55,57,58,72,90,92,],[28,-18,-19,-17,74,-8,-20,-10,-9,-21,]),'ASSIGN':([23,34,38,39,40,41,42,43,44,46,47,48,49,50,58,77,78,79,80,81,82,83,84,85,86,87,92,],[-19,52,59,-29,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-30,-31,-33,-34,-35,-36,-38,-39,-41,-42,-45,-21,]),'TIMES':([23,42,43,44,46,47,48,49,50,58,87,92,],[-19,68,-43,-44,-46,-47,-48,-49,-50,-20,-45,-21,]),'DIVIDE':([23,42,43,44,46,47,48,49,50,58,87,92,],[-19,69,-43,-44,-46,-47,-48,-49,-50,-20,-45,-21,]),'PLUS':([23,41,42,43,44,46,47,48,49,50,58,85,86,87,92,],[-19,66,-40,-43,-44,-46,-47,-48,-49,-50,-20,-41,-42,-45,-21,]),'MINUS':([23,41,42,43,44,46,47,48,49,50,58,85,86,87,92,],[-19,67,-40,-43,-44,-46,-47,-48,-49,-50,-20,-41,-42,-45,-21,]),'LESS':([23,40,41,42,43,44,46,47,48,49,50,58,83,84,85,86,87,92,],[-19,62,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-38,-39,-41,-42,-45,-21,]),'GREATER':([23,40,41,42,43,44,46,47,48,49,50,58,83,84,85,86,87,92,],[-19,63,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-38,-39,-41,-42,-45,-21,]),'EQUALS':([23,40,41,42,43,44,46,47,48,49,50,58,83,84,85,86,87,92,],[-19,64,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-38,-39,-41,-42,-45,-21,]),'NOTEQUAL':([23,40,41,42,43,44,46,47,48,49,50,58,83,84,85,86,87,92,],[-19,65,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-38,-39,-41,-42,-45,-21,]),'AND':([23,39,40,41,42,43,44,46,47,48,49,50,58,79,80,81,82,83,84,85,86,87,92,],[-19,60,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-33,-34,-35,-36,-38,-39,-41,-42,-45,-21,]),'OR':([23,39,40,41,42,43,44,46,47,48,49,50,58,79,80,81,82,83,84,85,86,87,92,],[-19,61,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-33,-34,-35,-36,-38,-39,-41,-42,-45,-21,]),'RBRACK':([23,37,38,39,40,41,42,43,44,46,47,48,49,50,58,76,77,78,79,80,81,82,83,84,85,86,87,91,92,],[-19,58,-27,-29,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,-20,-28,-30,-31,-33,-34,-35,-36,-38,-39,-41,-42,-45,92,-21,]),'RPAREN':([23,35,38,39,40,41,42,43,44,46,47,48,49,50,54,55,56,57,58,70,72,76,77,78,79,80,81,82,83,84,85,86,87,90,92,],[-19,-51,-27,-29,-32,-37,-40,-43,-44,-46,-47,-48,-49,-50,73,-6,-7,-8,-20,87,-10,-28,-30,-31,-33,-34,-35,-36,-38,-39,-41,-42,-45,-9,-21,]),'LBRACK':([23,58,],[29,75,]),'END':([24,51,],[30,-11,]),'RBRACE':([25,31,32,33,88,],[-51,51,-12,-13,-14,]),'LPAREN':([26,29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[35,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'CTEI':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'CTEF':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'CTEC':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CTES':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CTEB':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'var_declaration':([4,],[5,]),'empty':([4,5,8,25,35,],[7,11,11,33,56,]),'functions':([5,],[8,]),'function':([5,8,],[9,19,]),'simple_type':([6,10,35,74,],[12,20,53,53,]),'variables':([12,],[21,]),'variable':([12,25,28,29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[22,34,36,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'body':([18,73,],[24,89,]),'statement':([25,],[31,]),'assingation':([25,],[32,]),'expression':([29,45,52,75,],[37,70,71,91,]),'t_expression':([29,45,52,59,75,],[38,38,38,76,38,]),'g_expression':([29,45,52,59,60,61,75,],[39,39,39,39,77,78,39,]),'m_expression':([29,45,52,59,60,61,62,63,64,65,75,],[40,40,40,40,40,40,79,80,81,82,40,]),'term':([29,45,52,59,60,61,62,63,64,65,66,67,75,],[41,41,41,41,41,41,41,41,41,41,83,84,41,]),'factor':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[42,42,42,42,42,42,42,42,42,42,42,42,85,86,42,]),'cte':([29,45,52,59,60,61,62,63,64,65,66,67,68,69,75,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'parameters':([35,],[54,]),'parameter_list':([35,],[55,]),'parameter':([35,74,],[57,90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON var_declaration functions MAIN body END','program',8,'p_program','parser_1.py',6),
  ('functions -> functions function','functions',2,'p_functions','parser_1.py',13),
  ('functions -> function','functions',1,'p_functions','parser_1.py',14),
  ('function -> FUNCTION simple_type ID LPAREN parameters RPAREN body','function',7,'p_function','parser_1.py',19),
  ('function -> empty','function',1,'p_function','parser_1.py',20),
  ('parameters -> parameter_list','parameters',1,'p_parameters','parser_1.py',25),
  ('parameters -> empty','parameters',1,'p_parameters','parser_1.py',26),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','parser_1.py',31),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','parser_1.py',32),
  ('parameter -> simple_type ID','parameter',2,'p_parameter','parser_1.py',37),
  ('body -> LBRACE statement RBRACE','body',3,'p_body','parser_1.py',42),
  ('statement -> assingation','statement',1,'p_statement','parser_1.py',47),
  ('statement -> empty','statement',1,'p_statement','parser_1.py',48),
  ('assingation -> variable ASSIGN expression SEMICOLON','assingation',4,'p_assingation','parser_1.py',53),
  ('var_declaration -> VARIABLE simple_type variables SEMICOLON','var_declaration',4,'p_var_declaration','parser_1.py',58),
  ('var_declaration -> empty','var_declaration',1,'p_var_declaration','parser_1.py',59),
  ('variables -> variables COMMA variable','variables',3,'p_variables','parser_1.py',65),
  ('variables -> variable','variables',1,'p_variables','parser_1.py',66),
  ('variable -> ID','variable',1,'p_variable','parser_1.py',72),
  ('variable -> ID LBRACK expression RBRACK','variable',4,'p_variable','parser_1.py',73),
  ('variable -> ID LBRACK expression RBRACK LBRACK expression RBRACK','variable',7,'p_variable','parser_1.py',74),
  ('simple_type -> INT','simple_type',1,'p_simple_type','parser_1.py',80),
  ('simple_type -> FLOAT','simple_type',1,'p_simple_type','parser_1.py',81),
  ('simple_type -> CHAR','simple_type',1,'p_simple_type','parser_1.py',82),
  ('simple_type -> STRING','simple_type',1,'p_simple_type','parser_1.py',83),
  ('simple_type -> BOOLEAN','simple_type',1,'p_simple_type','parser_1.py',84),
  ('expression -> t_expression','expression',1,'p_expression','parser_1.py',91),
  ('expression -> t_expression ASSIGN t_expression','expression',3,'p_expression','parser_1.py',92),
  ('t_expression -> g_expression','t_expression',1,'p_t_expression','parser_1.py',97),
  ('t_expression -> g_expression AND g_expression','t_expression',3,'p_t_expression','parser_1.py',98),
  ('t_expression -> g_expression OR g_expression','t_expression',3,'p_t_expression','parser_1.py',99),
  ('g_expression -> m_expression','g_expression',1,'p_g_expression','parser_1.py',104),
  ('g_expression -> m_expression LESS m_expression','g_expression',3,'p_g_expression','parser_1.py',105),
  ('g_expression -> m_expression GREATER m_expression','g_expression',3,'p_g_expression','parser_1.py',106),
  ('g_expression -> m_expression EQUALS m_expression','g_expression',3,'p_g_expression','parser_1.py',107),
  ('g_expression -> m_expression NOTEQUAL m_expression','g_expression',3,'p_g_expression','parser_1.py',108),
  ('m_expression -> term','m_expression',1,'p_m_expression','parser_1.py',113),
  ('m_expression -> term PLUS term','m_expression',3,'p_m_expression','parser_1.py',114),
  ('m_expression -> term MINUS term','m_expression',3,'p_m_expression','parser_1.py',115),
  ('term -> factor','term',1,'p_term','parser_1.py',120),
  ('term -> factor TIMES factor','term',3,'p_term','parser_1.py',121),
  ('term -> factor DIVIDE factor','term',3,'p_term','parser_1.py',122),
  ('factor -> variable','factor',1,'p_factor','parser_1.py',128),
  ('factor -> cte','factor',1,'p_factor','parser_1.py',129),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser_1.py',130),
  ('cte -> CTEI','cte',1,'p_cte','parser_1.py',136),
  ('cte -> CTEF','cte',1,'p_cte','parser_1.py',137),
  ('cte -> CTEC','cte',1,'p_cte','parser_1.py',138),
  ('cte -> CTES','cte',1,'p_cte','parser_1.py',139),
  ('cte -> CTEB','cte',1,'p_cte','parser_1.py',140),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',146),
]
