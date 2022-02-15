from pyjavaproperties import Properties

p_file=Properties()
p_file.load(open("config.properties"))

value=p_file["ITO"]
print(p_file.items()) # display all entries
#print(p_file.__dict__)
print(value)
print(type(value))