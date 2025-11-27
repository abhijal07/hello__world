def updat_links_set(visited,new):
    visited=set(visited)
    new=set(new)
    o=visited.copy()
    for i in new:
        visited.add(i)
        a=new.difference(o) 
    return visited,len(a)
visited = {'http://example.com','http://google.com', 'http://test.com'}
new=['http://google.com', 'http://python.org', 'http://example.com/about','http://test.com']
print(updat_links_set(visited,new))