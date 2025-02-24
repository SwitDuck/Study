from typing import Optional
class Formatter:
    def format(self, string: str) -> str:
        pass
def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format а string using the formatter object, which 
    is expected to have а format() method that accepts 
    а string. 
    """
    class DefaultFormatter(Formatter): 
        """Format а string in title case.""" 
        def format(self, string: str) -> str: 
            return str(string).title() 
    if not formatter: 
        formatter = DefaultFormatter() 
    return formatter.format(string) 
hello_string = "hello world, how are you today?" 
print(f"input : {hello_string}") 
print(f"output: {format_string(hello_string)}")