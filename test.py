def Process(t):
    i = 0
    while t[i] != ' ':
        i+=1
    return t[i+1:len(t)]
f = open('settings.txt','r')


HEIGHT = int(Process(f.readline()))
WIDTH = int(Process(f.readline()))
ACC = float(Process(f.readline()))
FPS = int(Process(f.readline()))
f.close()