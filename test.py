import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('ASRL3::INSTR')
#print(inst.query("*IDN?"))
rm.

inst.