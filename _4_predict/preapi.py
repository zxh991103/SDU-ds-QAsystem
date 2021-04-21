

path = "http://121.5.144.6:2020/query"
def pre(txt):
    import requests
    r = requests.post(
        path,
        json={
            "text": txt})


    import ast

    rdict = ast.literal_eval(r.text)
    cls = rdict['predicate']
    res = rdict['subject']
    return res,cls



