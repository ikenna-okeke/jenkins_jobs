import fire

def hello(name="World"):
    return "hello " + name

if __name__ =="__main__":
    fire.Fire(hello)