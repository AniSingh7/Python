def get_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_values(v)
        else:
            yield v


a = {'1':'Harsha','name':{'location':{'bangalore':{'marath','white'},'che':{'1':{'hy','ra'}}}}}

print(list(get_values(a)))

