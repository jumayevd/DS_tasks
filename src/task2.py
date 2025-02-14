def typeBasedTransformer(**kwargs):

    changed = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            changed[key] = value ** 2
        elif isinstance(value, str):
            changed[key] = value[::-1]
        elif isinstance(value, bool):
            changed[key] = not value
        elif isinstance(value, (list, tuple)):
            changed[key] = value[::-1]
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value):
                changed[key] = {v:k for k, v in value.items()}
            else:
                changed[key] = value

    return changed

if __name__ == "__main__":

    res = typeBasedTransformer(
        num=4,
        pi=3.14,
        text="Hello",
        flag=True,
        items=[1, 2, 3],
        tpl=(10, 20, 30),
        data={"a": 1, "b": 2},
        mixed_set={1, 2, 3} 
    )
    print(res)