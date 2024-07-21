class ON:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "on": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "on"
    CATEGORY = "LogicGates"

    def on(self, on):
        return(on,)
    
class CreateBYTE:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "1": ("BOOLEAN", {"default": False}),
                "2": ("BOOLEAN", {"default": False}),
                "4": ("BOOLEAN", {"default": False}),
                "8": ("BOOLEAN", {"default": False}),
                "16": ("BOOLEAN", {"default": False}),
                "32": ("BOOLEAN", {"default": False}),
                "64": ("BOOLEAN", {"default": False}),
                "128": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN",)
    FUNCTION = "CreateBYTE"
    CATEGORY = "LogicGates"

    def CreateBYTE(self, one, two, three, four, five, six, seven, eight):
        return(one, two, three, four, five, six, seven, eight,)

class ByteToBits:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "byte": ("STRING", {"forceInput": True}),
            },
        }
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN",)
    FUNCTION = "ByteToBits"
    CATEGORY = "LogicGates"

    def ByteToBits(self, byte):
        bits = [bool(int(bit)) for bit in byte]
        return(bits[0], bits[1], bits[2], bits[3], bits[4], bits[5], bits[6], bits[7],)

class BitMemory:
    def __init__(self):
        self.bit = False

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "write": ("BOOLEAN", {"forceInput": True}),
                "read": ("BOOLEAN", {"forceInput": True}),
                "input": ("BOOLEAN", {"forceInput": True}),
            },
        }
    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "BitMemory"
    CATEGORY = "LogicGates"

    def BitMemory(self, write, read, input):
        output = False
        if write:
            self.bit = input
        if read:
            output = self.bit
        return(output,)

class ByteMemory: #Bytes are strings for easy testing right now, may use ints in the future
    def __init__(self):
        self.byte = "00000000"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "write": ("BOOLEAN", {"forceInput": True}),
                "read": ("BOOLEAN", {"forceInput": True}),
                "input": ("String", {"forceInput": True}),
            },
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "ByteMemory"
    CATEGORY = "LogicGates"

    def ByteMemory(self, write, read, input):
        output = False
        if write:
            self.byte = input
        if read:
            output = self.byte
        return(output,)

class NAND:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "NAND"

    CATEGORY = "LogicGates"

    def NAND(self, one, two):
        return((not(one and two)),)

class AND:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "AND"

    CATEGORY = "LogicGates"

    def AND(self, one, two):
        return((one and two),)
    
class OR:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "OR"

    CATEGORY = "LogicGates"

    def OR(self, one, two):
        return((one or two),)

class NOR:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "NOR"

    CATEGORY = "LogicGates"

    def NOR(self, one, two):
        return((not(one or two)),)
    
class NOT:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "NOT"

    CATEGORY = "LogicGates"

    def NOT(self, one):
        return((not(one)),)

class XOR:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "XOR"

    CATEGORY = "LogicGates"

    def XOR(self, one, two):
        return((True if one != two else False),)
    
class XNOR:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "two": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "XNOR"

    CATEGORY = "LogicGates"

    def XNOR(self, one, two):
        return((not(True if one != two else False)),)
    
class SWITCH:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "enable": ("BOOLEAN", {"forceInput": True}),
                "one": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "SWITCH"

    CATEGORY = "LogicGates"

    def SWITCH(self, enable, one):
        return((one if enable else None),)

class BoolToString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("BOOLEAN", {"forceInput": True}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "BoolToString"
    CATEGORY = "LogicGates"

    def BoolToString(self, input):
        result = "True" if input else "False"
        return(result,)
    
    
NODE_CLASS_MAPPINGS = {
    "ON": ON,
    "CreateByte": CreateBYTE,
    "NAND": NAND,
    "AND": AND,
    "OR": OR,
    "NOR": NOR,
    "NOT": NOT,
    "XOR": XOR,
    "XNOR": XNOR,
    "SWITCH": SWITCH,
    "BitMemory": BitMemory,
    "ByteMemory": ByteMemory,
    "ByteToBits": ByteToBits,
    "BoolToString": BoolToString,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ON": "ON",
    "CreateBYTE": "CreateBYTE",
    "NAND": "NAND",
    "AND": "AND",
    "OR": "OR",
    "NOR": "NOR",
    "NOT": "NOT",
    "XOR": "XOR",
    "XNOR": "XNOR",
    "SWITCH": "SWITCH",
    "BitMemory": "BitMemory",
    "ByteMemory": "ByteMemory",
    "ByteToBits": "ByteToBits",
    "BoolToString": "BoolToString",
}