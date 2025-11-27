def identify_intruders(attempts,authorised):
    c=set()
    for i in attempts:
        if i not in authorised:
            c.add(i)
    return c
attempts= ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
authorised={"alice", "bob", "frank", "grace"}
print( identify_intruders(attempts,authorised))
