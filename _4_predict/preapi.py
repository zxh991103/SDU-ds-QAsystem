


def pre(txt):
    import requests
    r = requests.post(
        "http://127.0.0.1:2020/query",
        json={
            "text": txt})


    import ast

    rdict = ast.literal_eval(r.text)
    if len(rdict['subject'] ) == 0:
        return "noa",rdict['predicate']
    cls = rdict['predicate']
    res = rdict['subject'][0][1]
    return res,cls


