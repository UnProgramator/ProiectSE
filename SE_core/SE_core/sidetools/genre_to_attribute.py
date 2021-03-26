import bd


def transform_gen2att():
    genuri=set()
    for x in bd.knoledge_base:
        y=x["gen"]
        genuri.update(y)

    genuri_list=[]
    for x in genuri:
        d={}
        d[x]=[]
        genuri_list.append(d)
    return genuri_list



if __name__ == "__main__":
    bd.load_db()
    x=transform_gen2att()
    print(x)
    if input() == 'y':
        bd.save_gen_to_att(x)
