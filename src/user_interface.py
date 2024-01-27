from abc import ABC, abstractmethod
from prettytable import PrettyTable

class User_Interface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass


class Console_User_Interface(User_Interface):
    def display_contacts(self):
        # if not self.data:
        #     return "The address book is empty."

        # table = PrettyTable(['Name', 'Phones', 'Birthday', 'Email'])
        # table.align = 'l'

        # total_contacts = len(self.data)

        # for idx, (name, record) in enumerate(self.data.items()):
        #     phones = "\n".join(map(str, record.phones))
        #     birthday = record.birthday if record.birthday else ""
        #     email = record.email if record.email else ""
        #     table.add_row([name, phones, birthday if birthday != "" else None, email if email != "" else None])

        #     # Add separator line if it's not the last contact
        #     if idx < total_contacts - 1:
        #         table.add_row(["-" * 20, "-" * 20, "-" * 20, "-" * 20])

        # return str(table)
        pass
    
    def display_notes(self):
        # self.print_notes()
        pass

class Web_User_Interface(User_Interface):
    def display_contacts(self, contacts):
        # Логіка виведення контактів на веб-сторінці
        pass

    def display_notes(self, notes):
        # Логіка виведення нотаток на веб-сторінці
        pass

    
