def scale_resolution(resolution,fact):
    L=[]
    for i,j in resolution:
        a=int(i*fact)
        b=int(j*fact)
        L.append((a,b))
    return L
resolution= [
 (1920, 1080),
 (1280, 720),
 (2560, 1440)
 ]
fact = 0.5
print(scale_resolution(resolution,fact))