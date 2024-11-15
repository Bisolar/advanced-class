# import threading

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# thread = threading.Thread(target=factorial)
# thread.start()


list = ["good", "gentle", "happy", "beautiful" "handsome", "smile", "yes"]



df =  {
    "positive_word": ["like", "yes", "true", "good", "kind", "smile", "beautiful", "right", "gentle", "great", "nice"],
    "negative word": ["dislike", "no", "false", "bad", "wicked", "frown", "ugly", "left", "wrong", "harsh", "poor"],
    "neutral word": ["it", "is", "the", "this", "was", "in", "how", "that", "these", "where", "you", "are"],
}

pos = df["positive_word"]
neos = df["negative word"]
# nos = df["neutral word"]
# for x in pos:
#     print(x)
# print()

user_response = str(input("Enter your comment here: ")).lower().split()
print(user_response)

for x in user_response:
    if x in pos:
        print("positive statement")     
        break
    elif x in neos:
        print("negative statement")
        break
    # elif x in nos:
    #     print("neutral statement")
    #     break
    else:
        print("Unidentified statement")