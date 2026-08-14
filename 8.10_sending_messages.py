# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


def show_messages(msgs):
    for msg in msgs:
        print(msg)


def send_messages(old_msgs, new_msgs):
    while old_msgs:
        temp_msg = old_msgs.pop()
        print(temp_msg)
        new_msgs.append(temp_msg)

list_msg = ['Hello', 'Hi', 'Up', 'legit nga guys!']
sent_msgs = [ ]
print("\nBEFORE:")
print(f"old list: {list_msg}")
print(f"new list: {sent_msgs}")
send_messages(list_msg, sent_msgs)
print("\nAFTER:")
print(f"old list: {list_msg}")
print(f"new list: {sent_msgs}")


