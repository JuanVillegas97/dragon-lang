
from compiler.memory_map import MemoryMap
import json
#INT     1000-1999
#FLOAT   2000-2999
#CHAR    3000-3999
#BOOLEAN 4000-4999
class VirtualMachine:
    def __init__(self):
        directory, constant_table, quadruples = self.__deserialize_json_from_file()
        self.__memory = MemoryMap.get_instance(directory)
        self.__constant_table = constant_table
        self.__quadruples = quadruples
        
        self.__execute()        
        
        
    def __execute(self):
        instruction_pointer = 0
        quadruples = self.__quadruples
        print("\n")
        while instruction_pointer < len(quadruples):
            quadruple = quadruples[instruction_pointer]
            operator = quadruple["_Quadruple__operator"]
            left_operand = quadruple["_Quadruple__left_operand"]
            right_operand = quadruple["_Quadruple__right_operand"]
            result = quadruple["_Quadruple__avail"]
            
            # Perform addition
            if operator == 0:
                pass
            # Perform assignation
            elif operator == 13:
                left_side =  self.__get_value(left_operand) # Get the value
                address = result                            # Address where is going to bet set
                type = self.__get_type(address)
                self.__memory.set_value_at_address(type,address,left_side)
            elif operator == 32:
                # Exit the virtual machine
                break

            instruction_pointer += 1
            
        self.__memory.print_memory()

    
    def __get_value(self, address):
        if address > 4999:
            for constant_id, constant_data in self.__constant_table.items():
                virtual_address = constant_data['virtual_address']
                if virtual_address == address:
                    return constant_id
                
        if 1000 <= address < 5000:
            if 1000 <= address <= 1999:
                type =  "INT"
            elif 2000 <= address <= 2999:
                type =  "FLOAT"
            elif 3000 <= address <= 3999:
                type =  "CHAR"
            elif 4000 <= address <= 4999:
                type =  "BOOLEAN"
            value = self.__memory.get_value(type,address)
            return value
        
        return "ERROR"
    

        
    def __deserialize_json_from_file(file_path):
        file_path = "ovejota.json"
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        directory = json_data['directory']
        constant_table = json_data['constant_table']
        quadruples = json_data['quadruples']
        return directory,constant_table,quadruples
    

    
    def __get_type(self, address):
        if address is None:
            print("Hi")
        if 1000 <= address < 5000:
            if 1000 <= address <= 1999:
                return  "INT"
            elif 2000 <= address <= 2999:
                return  "FLOAT"
            elif 3000 <= address <= 3999:
                return "CHAR"
            elif 4000 <= address <= 4999:
                return  "BOOLEAN"

        return "ERROR"
    
    def __get_variable_type(self, variable):
        variable_type = type(variable).__name__
        
        if variable_type == 'bool':
            return 'BOOLEAN'
        elif variable_type == 'str' and len(variable) == 1:
            return 'CHAR'
        elif variable_type == 'float':
            return 'FLOAT'
        elif variable_type == 'int':
            return 'INT'
        else:
            return variable_type.upper()