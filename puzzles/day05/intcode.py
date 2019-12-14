class UnknownOpcodeException(Exception):
    pass

class DiagnosticFailedException(Exception):
    pass


class Day5IntcodeComputer(object):
    POSITION_MODE = "0"
    IMMEDIATE_MODE = "1"
    
    ADD_OPCODE = "01"
    MULT_OPCODE = "02"
    MATH_OPCODES = (ADD_OPCODE, MULT_OPCODE)
    STORE_OPCODE = "03"
    RETURN_OPCODE = "04"
    TERMINATE_OPCODE = "99"
    
    OPCODE_LENGTH = 2

    EXPECTED_DIAGNOSTIC_CODE = 0

    def __init__(self, memory, input_=None, debug=False):
        self._memory = memory
        self.input = input_
        self.pointer_address = 0
        self.return_value = None
        self._debug = debug

    @property
    def DEBUG(self):
        return self._debug

    @DEBUG.setter
    def DEBUG(self, value):
        if not isinstance(value, bool):
            raise TypeError("DEBUG setting must be a boolean!")
        self._debug = value

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        self.pointer_address = 0
        self.return_value = None
        self._memory = value

    def run_diagnostic(self):
        while True:
            opcode, parameter_modes = self.parse_instruction()
            if opcode == self.TERMINATE_OPCODE:
                diagnostic_code = self.return_value
                self.assert_passed_diagnostic_test(diagnostic_code)
                return diagnostic_code
            self.execute_instruction(opcode, parameter_modes)

    def assert_passed_diagnostic_test(self, diagnostic_code):
        expected_code = self.EXPECTED_DIAGNOSTIC_CODE
        if not diagnostic_code == expected_code:
            raise DiagnosticFailedException(
                    f"Diagnostic expected code {expected_code}, "
                    f"returned {diagnostic_code} instead!")

    def read_memory(self, address, mode):
        if mode == self.POSITION_MODE:
            position = self.memory[address]
            value = self.memory[position]
        elif (mode == self.IMMEDIATE_MODE) or (not mode):
            value = self.memory[address]
        return value

    def write_memory(self, address, value):
        if self.DEBUG:
            print(f'Updating memory at {address}:', value)
        self.memory[address] = int(value)

    def write_return_value(self, value):
        if self.DEBUG:
            print(f'Updating return value:', value)
        self.return_value = int(value)

    def move_pointer_to_next_address(self):
        self.pointer_address += 1

    def read_and_move_pointer(self, mode=None):
        memory_value = self.read_memory(self.pointer_address, mode)
        self.move_pointer_to_next_address()
        return memory_value

    def add_op(self, mode0, mode1):
        x = self.read_and_move_pointer(mode0)
        y = self.read_and_move_pointer(mode1)
        return x + y

    def multiply_op(self, mode0, mode1):
        x = self.read_and_move_pointer(mode0)
        y = self.read_and_move_pointer(mode1)
        return x * y

    def store_op(self, address):
        self.write_memory(address, self.input)

    def return_op(self, value):
        self.write_return_value(value)
        self.move_pointer_to_next_address()

    def lpad_zeroes(self, value, min_num_digits):
        num_zeroes = min_num_digits - len(value)
        return ("0" * num_zeroes) + value

    def parse_instruction(self):
        first_value = str(self.read_and_move_pointer())
        opcode = self.lpad_zeroes(
            first_value, 
            self.OPCODE_LENGTH
        )[-self.OPCODE_LENGTH:]
        min_first_value_num_digits = 5
        padded_first_value = self.lpad_zeroes(
            first_value, 
            min_first_value_num_digits
        )
        # parameters are read in reverse order
        parameter_modes = padded_first_value[::-1][self.OPCODE_LENGTH:]

        return opcode, parameter_modes

    def execute_instruction(self, opcode, parameter_modes):
        if self.DEBUG:
            print(f"Pointer: {self.pointer_address-1} | Opcode: {opcode} | Parameter modes: {parameter_modes}")
        if opcode == self.ADD_OPCODE:
            parameters = parameter_modes[:2]
            value = self.add_op(*parameters)
            self.write_memory(self.read_and_move_pointer(), value)
        elif opcode == self.MULT_OPCODE:
            parameters = parameter_modes[:2]
            value = self.multiply_op(*parameters)
            self.write_memory(self.read_and_move_pointer(), value)
        elif opcode == self.STORE_OPCODE:
            self.store_op(self.read_and_move_pointer())
        elif opcode == self.RETURN_OPCODE:
            parameter = parameter_modes[0]
            self.return_op(parameter)
        else:
            import pdb; pdb.set_trace()
            raise UnknownOpcodeException(
                f"Encountered unknown opcode: {opcode}")
