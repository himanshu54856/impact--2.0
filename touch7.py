""" mutable is a way of saying that the internal state of object is changed """
list_value=[1,2,3]
list_value[0]=5
print(list_value)



"""immutable is a way of saying that the internal state of object is doesn't change once it has been created"""
tuple_value=(10,20,30)
tuple_value[0]=40
print(tuple_value)