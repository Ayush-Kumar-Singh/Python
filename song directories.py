Song= {"Song":"No Brainer","Year":"2018","1":0}
while(True):
    print("which song you want to play")
    ayush= str(input())
    if ayush == "1":
        Song[ayush] +=1
        print(Song)
    else:
        print("Song Not Available")
    