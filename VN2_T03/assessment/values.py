def nest_dict(m):
    for val in m.values():
        if isinstance(val,dict):
            yield from nest_dict(val)
        else:
            yield val
        return val
dict={'1':'Harsha','name':{'location':{'bangalore':{'marath','white'},'che':{'1':{'hy','ra'}}}}}
n=nest_dict(dict)
print(val)