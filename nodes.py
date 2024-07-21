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
    CATEGORY = "TuringComplete"

    def on(self, on):
        return(on,)
    
class BYTE:
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
    FUNCTION = "BYTE"
    CATEGORY = "TuringComplete"

    def BYTE(self, one, two, three, four, five, six, seven, eight):
        return(one, two, three, four, five, six, seven, eight,)

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

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

    def NOT(self, one):
        return((not(one)),)

class XOR:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "one": ("BOOLEAN", {"forceInput": True}),
                "one": ("BOOLEAN", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "XOR"

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

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

    CATEGORY = "TuringComplete"

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
    CATEGORY = "TuringComplete"

    def BoolToString(self, input):
        result = "True" if input else "False"
        return(result,)
    
    
NODE_CLASS_MAPPINGS = {
    "ON": ON,
    "Byte": BYTE,
    "NAND": NAND,
    "AND": AND,
    "OR": OR,
    "NOR": NOR,
    "NOT": NOT,
    "SWITCH": SWITCH,
    "BoolToString": BoolToString,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ON": "ON",
    "BYTE": "BYTE",
    "NAND": "NAND",
    "AND": "AND",
    "OR": "OR",
    "NOR": "NOR",
    "NOT": "NOT",
    "SWITCH": "SWITCH",
    "BoolToString": "BoolToString",
}