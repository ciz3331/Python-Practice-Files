# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
# tion send_messages() with a copy of the list of messages. After calling the func-
# tion, print both of your lists to show that the original list has retained its messages.


def show_messages(msgs):
    """Show messages from  a list."""
    for msg in msgs:
        print(msg)


def send_messages(old_msgs, new_msgs):
    """Transfers all elements from old_msgs to new_msgs"""
    while old_msgs:
        temp_msg = old_msgs.pop()
        print(temp_msg)
        new_msgs.append(temp_msg)


list_msg = ['Hello', 'Hi', 'Up', 'legit nga guys!']
sent_msgs = [ ]

print("\nBEFORE:")
print(f"old list: {list_msg}")
print(f"new list: {sent_msgs}")

send_messages(list_msg[:], sent_msgs)
print("\nAFTER:")
print(f"old list: {list_msg}")
#sent_msgs.reverse()
print(f"new list: {sent_msgs}")


