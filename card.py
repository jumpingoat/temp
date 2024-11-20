from faker import Faker

# Initialize faker
faker = Faker()

class BaseContact:
    """personal contact card."""
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def contact(self):
        """ personal phone number."""
        print(f"Dialing {self.phone} and calling {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        """Returns the length of the full name."""
        return len(self.first_name) + len(self.last_name) + 1  # Include space

class BusinessContact(BaseContact):
    """a business contact card."""
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        """business phone number."""
        print(f"Dialing {self.business_phone} and calling {self.first_name} {self.last_name} at work")

def create_contacts(contact_type, quantity):
    """
    random contact cards.
    :param contact_type: Type of contact ('BaseContact' or 'BusinessContact').
    :param quantity: Number of contacts to generate.
    :return: List of contact instances.
    """
    contacts = []
    for _ in range(quantity):
        first_name = faker.first_name()
        last_name = faker.last_name()
        phone = faker.phone_number()
        email = faker.email()
        if contact_type == "BaseContact":
            contacts.append(BaseContact(first_name, last_name, phone, email))
        elif contact_type == "BusinessContact":
            position = faker.job()
            company = faker.company()
            business_phone = faker.phone_number()
            contacts.append(BusinessContact(first_name, last_name, phone, email, position, company, business_phone))
    return contacts

# Generate 5 random business cards and display their content
contact_list = create_contacts("BusinessContact", 5)

# Print first name, last name, and email for each contact
for contact in contact_list:
    print(f"{contact.first_name} {contact.last_name}, {contact.email}")

# Example: Test the `contact` method and dynamic `label_length` attribute
print("\nContacting and showing label lengths:")
for contact in contact_list:
    contact.contact()
    print(f"Label length: {contact.label_length}")
