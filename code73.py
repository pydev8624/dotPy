def zarb(x):
    if x%2==0:
        return x

xl=[2,3,4,5]

nl=list(filter(zarb,xl,))

print(nl)

