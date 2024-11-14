#  The Love Calculator❤️ playfully measures the chemistry between you and your crush.Enter your names to see if you're a sweet match or an explosive combo like Coke and Mentos!💥.

print("💖 Welcome to the Love Calculator! 💖")
print("Let's see if you're destined for romance or just some friendly bickering!😆\n")

name1 = input("Enter your name, lovebird 🐦 : ")
name2 = input("Enter your crush's name (no peeking! 😜) : ")
combine_string = name1 + name2
lowercase_string = combine_string.lower()

t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')
true = t + r + u + e

l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Love Score between {name1} ❤️  {name2} is {love_score}.\n🔥 You two go together like Coke and Mentos – explosive chemistry! 💥")
elif 40 <= love_score <= 50:
    print(f"Love Score between {name1} ❤️  {name2} is {love_score}.\n😊 You’re alright together – a cozy blend like tea and biscuits! 🍪☕")
elif 10 <= love_score < 40:
    print(f"Love Score between {name1} ❤️  {name2} is {love_score}.\n🤔 It’s a bit like pineapple on pizza – not everyone’s taste, but who knows? 🍍🍕")
else:
    print(f"Love Score between {name1} ❤️  {name2} is {love_score}.\n❤️ It’s the start of something sweet, like peanut butter and jelly! 🥜🍓")

print("\n💘 Thank you for trying the Love Calculator! 💘")
