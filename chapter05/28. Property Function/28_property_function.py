class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name")
        self._name = value

    def del_name(self):
        print("Deleting name")
        del self._name

    # Create property using property() function
    # fget: A function for getting the attribute value.
    # fset: A function for setting the attribute value.
    # fdel: A function for deleting the attribute value.
    #  doc: A string that contains the documentation for the attribute.
    name = property(get_name, set_name, del_name, "This is the 'name' property")

def main():
    # Usage
    p = Person("John")
    print(p.name)       # Getting name -> John
    p.name = "Jane"     # Setting name
    print(p.name)       # Getting name -> Jane
    del p.name          # Deleting name

    # add new property to person p
    p.friends = []
    p.friends.append("Bob")
    p.friends.append("Alice")

    print(f"\nPrinting friends:")
    for friend in p.friends:
        print(f" - {friend}")
    print()

if __name__ == "__main__":
    main()

