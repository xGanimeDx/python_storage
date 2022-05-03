from collections import Counter, defaultdict, namedtuple

my_list = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]

print(Counter(my_list))
print(Counter("aaaaaaaaaadsdsdfsdxcvxcvwe"))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.split()))

c = defaultdict(lambda: 0)
c['correct'] = 100
print(c['wrong'])


Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(5, 'husky', 'sam')
print(sammy.age)
print(sammy.breed)
print(sammy.name)
