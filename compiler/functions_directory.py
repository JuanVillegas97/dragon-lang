import copy
from lexer.tokens import reserved
from compiler.interfaces.variable import variable
from constants.constants import *

#VARIABLES AND TEMPORALS
#INT     1000-1999
#FLOAT   2000-2999
#CHAR    2000-2999
#BOOLEAN 3000-3999
#CTES
#INT     4000-4499
#FLOAT   4500-4999
#CHAR    5000-5499
#BOOLEAN 5000-5001

class FunctionsDirectory:
    __instance = None

    @staticmethod
    def get_instance():
        if FunctionsDirectory.__instance is None:
            FunctionsDirectory()
        return FunctionsDirectory.__instance

    def __init__(self):
        if FunctionsDirectory.__instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
        else:
            FunctionsDirectory.__instance = self
            self.__constants_table = {}
            self.__function_dictionary = {}
            self.__current_function_name = None
            self.__current_function_scope = None
            self.__current_function_type = None
            self.__is_variable_declaration = False
            self.__program_name = None
    
    def add_resource(self, ids, resource_type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        for id in ids:
            self.__function_dictionary[self.__current_function_name][RESOURCES][resource_type] +=1

    def set_resource(self, resource_type, num):
            if self.__current_function_name is None:
                raise Exception("No function defined to add variable '{}'".format(id))
            
            self.__function_dictionary[self.__current_function_name][RESOURCES][resource_type] = num

            
    def is_function_name(self,function_name):
        if function_name in self.__function_dictionary:
            return True
        else:
            raise Exception("Function being called does not exist")
        
    def set_program_name(self, name):
        self.__program_name = name
    
    def __check_value_type(self, value):
            if isinstance(value, bool):
                return BOOLEAN
            elif isinstance(value, int):
                return INT
            elif isinstance(value, float):
                return FLOAT
            else:
                return ERROR
        
    def add_constant(self, constant):
        type = self.__check_value_type(constant)
        if type == ERROR:
            raise Exception("Constant is ERRROR type")
        if constant not in self.__constants_table:
            new_variable = variable(constant,type,0)
            self.__constants_table[constant] = new_variable
            
        
    def set_is_variable_declaration_true(self):
        self.__is_variable_declaration = True
        
    def set_is_variable_declaration_false(self):
        self.__is_variable_declaration = False
    
    def get_is_variable_declaration(self):
        return self.__is_variable_declaration
        
    def get_function_dictionary(self):
        return self.__function_dictionary
    
    def get_current_function_name(self):
        return self.__current_function_name
    
    def add_parameters(self, type):
        if type in reserved:
            type = reserved[type]
        self.__function_dictionary[self.__current_function_name]["parameters"].append(type)

    def set_current(self, name, type, scope):
        self.__current_function_name = name
        self.__current_function_type = type
        self.__current_function_scope= scope
    
    def add_function(self, starting_address=None):
        if self.__current_function_name in self.__function_dictionary:
            raise Exception("Function '{}' multiple declaration (functions can only have unique ID)".format(self.__current_function_name))

        if self.__current_function_type in reserved:
            self.__current_function_type = reserved[self.__current_function_type]
        self.__function_dictionary[self.__current_function_name] = {
            "type": self.__current_function_type,
            "scope": self.__current_function_scope,
            "starting_address": starting_address,
            RESOURCES:{
                PARAMETERS : 0,
                VARIABLES : 0,
                TEMPORALS : 0,
            },
            "parameters": [],
            "variable_table": {}
        }
    
    
    def add_variable(self, ids,type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        if type in reserved:
            type = reserved[type]

        for id in ids:
            if id in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                raise Exception("Variable '{}' multiple declaration".format(id))
            new_variable = variable(id,type,0)
            self.__function_dictionary[self.__current_function_name]["variable_table"][id] = new_variable
    
    def get_invocation_type(self,invocation_id):
        return self.__function_dictionary[invocation_id]["type"]
    
    def search_variable(self, ids):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        #? First check for the variable in local scope
        local_variable_table = self.__function_dictionary[self.__current_function_name]["variable_table"]
        
        #? Secondly, check the variable in the constant table
        constant_table = self.__constants_table
        
        #? Lastly, check variables in the global scope (program variable table)
        program_variable_table = self.__function_dictionary[self.__program_name]["variable_table"]
        
        for id in ids:
            if id not in local_variable_table and \
            id not in constant_table and \
            id not in program_variable_table:
                raise Exception("Variable '{}' was not declared".format(id))

    def get_variable(self, function_name, variable_id):
        if function_name not in self.__function_dictionary:
            raise Exception("Function '{}' was not declared".format(function_name))
        
        local_variable_table = self.__function_dictionary[function_name]["variable_table"]
        
        if variable_id in local_variable_table:
            return local_variable_table[variable_id]
        
        constant_table = self.__constants_table
        
        if variable_id in constant_table:
            return constant_table[variable_id]
        
        program_variable_table = self.__function_dictionary[self.__program_name]["variable_table"]
        
        if variable_id in program_variable_table:
            return program_variable_table[variable_id]

        raise Exception("Variable '{}' not found".format(variable_id))

    
    def print_function_dictionary(self):
        for function_name, function_details in self.__function_dictionary.items():
            print("{:15} {:10} {:17} {:8} {:10}  {:25}".format(
            "Function Name", "Type", "Starting Address", "Scope", "Signature",  "Resources"))
            function_type = function_details["type"]
            function_scope = function_details["scope"]
            variable_table = function_details["variable_table"]
            parameters_list = function_details["parameters"]
            starting_address = str(function_details["starting_address"])

            parameters_types = ", ".join(str(types) for types in parameters_list)
            variable_names = ", ".join(str(name) for name in variable_table.keys())
            resources = function_details[RESOURCES]

            # Convert resource values to strings
            resources_str = ", ".join("{}: {}".format(key, value) for key, value in resources.items())

            print("{:15} {:10} {:17} {:8} {:10} {:25}".format(
                function_name, function_type, starting_address, function_scope,
                parameters_types, resources_str))

            print("Variable Table:")
            print("{:10} {:10} {:15}".format("ID", "Type", "Virtual Address"))

            for variable_id, variable in variable_table.items():
                variable_type = variable.type
                virtual_address = str(variable.virtual_address)
                print("{:10} {:10} {:15}".format(variable_id, variable_type, virtual_address))
            print("\n")
        print("\nConstants Table:")
        print("{:10} {:10} {:15}".format("Type", "Constant", "Virtual Address"))

        for constant, variable in self.__constants_table.items():
            constant_type = variable.type
            virtual_address = str(variable.virtual_address)
            print("{:10} {:10} {:15}".format(constant_type, constant, virtual_address))


    def print_current(self):
            print(self.__current_function_type," ",self.__current_function_name," ",self.__current_function_scope)

    


