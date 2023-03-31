from address import Address

class Person:
    def __init__(self, first_name, last_name, dob, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []

        '''The user can pass only one address object as address parameters or a list of address objects since one person
        might have multiple addresses. Check for both options.'''
        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Exception("Invalid Address! Provide an instance of the Address class or a list of instances.")
            self.addresses = address
        else:
            raise Exception("Invalid Address! Provide an instance of the Address class or a list of instances.")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise Exception("Invalid Address! Provide an instance of the Address class or a list of instances.")
        self.addresses.append(address)


