import yaml

with open("./data.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("类型：",type(data))
    print("值：",data)