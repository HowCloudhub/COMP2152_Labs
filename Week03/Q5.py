contacts = {
    "Alice": "555-1234",
    "Bob": "555-1246",
    "Reiner": "545-4568"
}

print(f"Alice's number: {contacts['Alice']}")

contacts["Diana"] = "555-1512"
print(f"Contacts after adding Diana:{contacts} ")

contacts["Bob"] = "555-4444"
print(f"Conacts after updating Bob: {contacts}")
del contacts["Reiner"]
print(f"Contacts after deleting Reiner: {contacts}")
print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total Contacts: {len(contacts)}")
