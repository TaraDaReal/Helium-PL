# REGISTERS AND FLAGS

a = 0 # Accumulator
pc = 0 # Program counter
sp = 0 # Stack pointer
x, y = 0, 0 # Index registers

address = 0

memory = [0] * 0x10000

N = 0 # Negative flag
V = 1 # Overflow flag
B = 3 # Break flag
D = 4 # Decimal flag
I = 5 # Interrupt disable flag
Z = 6 # Zero flag
C = 7 # Carry flag

FLAGS = [0, 0, 0, 0, 0, 0, 0, 0]

def read_byte(addr) -> int: return memory[addr]

def write_byte(addr, value) -> None: memory[addr] = value

