class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []
list_of_sent = []

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    list_of_emails.append(email)

list_of_sent = [int(index) for index in input().split(", ")]

for email in list_of_emails:
    if list_of_emails.index(email) in list_of_sent:
        email.send()
    print(email.get_info())
