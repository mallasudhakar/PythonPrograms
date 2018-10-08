def print_details(name,age,*marks):
    print(name)
    print(age)
    print(type(marks))
    for i in marks:
        print(i)
print_details("sudhakar",29,89,99,78,77,34,22)
