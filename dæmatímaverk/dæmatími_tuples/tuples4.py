def get_emails():
    emails = []
    while True:
        user_input = input("Email address: ")
        if user_input == "q":
            break
        emails.append(user_input)
    return emails

def get_names_and_domains(email_list):            
    names_n_domains = [tuple(i.split("@")) for i in email_list]
    return names_n_domains

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)