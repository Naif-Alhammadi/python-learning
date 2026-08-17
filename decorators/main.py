def add_sp(func):
    @wapper
    def wapper(*args, **kwargs):
        print("you add spr")
        func(*args)
        print(*kwargs)
    return wapper

@add_sp
def get_ice(flav, name="hi"):
    print(f"here is your {flav} {name} ice cream")

get_ice('ch', name="naif")