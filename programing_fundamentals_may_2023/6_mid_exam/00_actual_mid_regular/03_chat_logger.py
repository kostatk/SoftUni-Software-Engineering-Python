
def add_message(existing_log, message):
    existing_log.append(message)
    return existing_log


def delete_message(existing_log, message):
    if message in existing_log:
        existing_log.remove(message)
    return existing_log


def edit_log(existing_log, old_message, new_message):
    for message in existing_log:
        if message == old_message:
            index_of_existing = existing_log.index(old_message)
            existing_log[index_of_existing] = new_message
    return existing_log


def pin_message(existing_log, message):
    if message in existing_log:
        existing_log.append(existing_log.pop(existing_log.index(message)))
    return existing_log


def spamming(existing_log, message):
    for spam in range(1, len(message)):
        existing_log.append(message[spam])
    return existing_log


chat_log = []
while True:
    action_description = input().split()
    if action_description[0] == "end":
        break
    elif action_description[0] == "Chat":
        chat_log = add_message(chat_log, action_description[1])
    elif action_description[0] == "Delete":
        chat_log = delete_message(chat_log, action_description[1])
    elif action_description[0] == "Edit":
        chat_log = edit_log(chat_log, action_description[1], action_description[2])
    elif action_description[0] == "Pin":
        chat_log = pin_message(chat_log, action_description[1])
    elif action_description[0] == "Spam":
        chat_log = spamming(chat_log, action_description)
for item in chat_log:
    print(item)
