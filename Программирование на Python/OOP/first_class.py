class first:
    print('Inter you color: ')
    color = 'red'
    def out(self):
        print(self.color + "!")

obj1 = first()
obj2 = first()

print(obj1.color)
print(obj2.color)

obj1.out()
obj2.out()
