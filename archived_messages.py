#THIS MODULE IS A COPY OF 8.11, WHICH WILL BE USED FOR 8.16
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
# tion send_messages() with a copy of the list of messages. After calling the func-
# tion, print both of your lists to show that the original list has retained its messages.


def show_messages(msgs):
    for msg in msgs:
        print(msg)

def send_messages(old_msgs, new_msgs):
    while old_msgs:
        temp_msg = old_msgs.pop()
        print(temp_msg)
        new_msgs.append(temp_msg)
        

# if __name__ == "__main__":
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




