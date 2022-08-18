def add_all(*args): # *args defaults to tuple when returned/printed, can call it #stuff, if you want
    print(args)
    # print(*args) # didn't work
    print(type(args))
    # print(type(*args)) # didn't work

# splat can pack all args into tuple AND unpack args

add_all("Happy", 100, True) # prints tuple -- (,,,), which is immutable because that is how splat args works
# things should be immutable by default

def add_one(one):
    print(one)
    print(type(one))

add_one(1)


# like this, power and weakness throw TypeError - unexpected argument keyword
# def make_hero(name, hero_stuff):
#     print(name, hero_stuff)

# make_hero("Super Git", power="time travel", weakness="ultra-large files")


# like this, power and weakness DO NOT TypeError
def make_hero(name, **hero_stuff):
    print(name, hero_stuff)

make_hero("Super Git", power="time travel", weakness="ultra-large files")


# convention
def make_hero(name, **kwargs):
    print(name, kwargs)

# ORDER matters
make_hero("Super Git", power="time travel", weakness="ultra-large files", is_happy=True)



def make_hero(*name, **kwargs):
    print(name, kwargs)

make_hero("Super Git", "hello", "bye", power="time travel", weakness="ultra-large files", is_happy=True)
