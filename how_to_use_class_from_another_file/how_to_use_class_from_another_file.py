# this is example of how to use classes from other files
# path to the file should be [folder.folder.file]
from another_file import person

human = person("test", 18)

print(person.getPopulation())
print(person.isAdult(17))
print(human.getAge())
print(human.getName())