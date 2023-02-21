import echo_service

# understanding behaviour of python interpreter

print("Hello")

x = echo_service.echo_name("Aditya")
print(x


def local_echo(name: str) -> str:
    return name + "hello


def local_echo2(name: str) -> str:
    return name + "hello2

# make AST of the current file
# then when the import statement is encountered : make AST of those dependencies

# try putting the import statement not at the top line but somewhere in the middle

# AST is made by python in interpreted way : that is line by line manner

# 1st AST of the current file is made and then the current file is executed
# while making the AST if there are any errors then control will not go to
# the run phase at all , the error would be reported in AST phase itself

# now if we have two errors then : when the 1st error is encountered while
# making the AST : then that error is reported without parsing the AST further down

# so we can divide the execution process in Python into 2 phases : 1st generation of
# AST (line by line) , next executing the AST line by line



