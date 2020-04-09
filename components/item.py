from types import MethodType


class Item:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, **kwargs):
        if use_function:
            self.use_function = MethodType(use_function, self)
        else:
            self.use_function = None
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.function_kwargs = kwargs
