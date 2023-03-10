class Language:
    def __init__(self, level, lang_type):
        self.level = level
        self.lang_type = lang_type


class Python(Language):
    def write_function(self, func_name, arg):
        return f"def {func_name}({arg}):"

    def create_variable(self, var_name, value):
        if isinstance(value, str):
            return f"{var_name} = '{value}'"
        else:
            return f"{var_name} = {value}"


class JavaScript(Language):
    def write_function(self, func_name, arg):
        return f"function {func_name}({arg}) {{ }};"

    def create_variable(self, var_name, value):
        if isinstance(value, str):
            return f"let {var_name} = '{value}';"
        else:
            return f"let {var_name} = {value};"


py = Python('Intermediate', 'Backend')
print(py.write_function('get_code', 'a'))
print(py.create_variable('name', 'John'))

js = JavaScript('Advanced', 'Frontend')
print(js.write_function('validate', 'form'))
print(js.create_variable('password', 'john@123'))
