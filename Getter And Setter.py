#program using getter and setter method

#defining property name
class property_fun_demo:

    #function to get value
    def get_age(self):
        print("get method called")
        return self._age

    #function to set value
    def set_age(self):
        print("set method called")
        return self._age

    #function to delete value
    def del_age(self):
        del self.age

    #function to delete age
    def del_age(self):
        del self._age

    #calling property() function
    age = property(get_age,set_age,del_age)


#creating object name is mark
mark = property_fun_demo()
mark._age = 14
print(mark._age)
