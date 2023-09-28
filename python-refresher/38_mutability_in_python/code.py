a = "hello"
b = a

print(f"Var a: [ id: {id(a)} , value: {a} ]")
print(f"Var a: [ id: {id(b)} , value: {b} ]")

a += " world"

print(f"Var a: [ id: {id(a)} , value: {a} ]")
print(f"Var a: [ id: {id(b)} , value: {b} ]")