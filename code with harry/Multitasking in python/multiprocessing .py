# if I have multiple processor then I can use multiple processor but in threading threads are spawned easily in low time
import requests
import multiprocessing 
from  concurrent.futures import ProcessPoolExecutor

def download_file(url,name):
    print(f"Started downloading {name}")
    r=requests.get(url)
    # I will store it in files folder 
    open(f"files1/File{name}.jpg","wb").write(r.content)    # --> If I download using same file name then It replaces the file by new file
    print(f"{name} is downloaded")

url="https://picsum.photos/2000/3000"   # --> If I increase the resolution it started to take time
pros=[]
if __name__=='__main__':

# Using multiprocessing method:-
    for i in range(5):  
        p=multiprocessing.Process(target=download_file,args=[url,i]) #<-- args must in []
        #--> How many arguments function contains it will have that much args=[]
        p.start()
        pros.append(p)  #--> we are using for so every loop I have to append in a blank list. 

    # After running the loop I can iterate the fils and join them
    for p in pros:
        p.join()
# Using threadpool.executor:-
    with ProcessPoolExecutor() as executor:
        l1=[url for i in range(5)]
        l2=[i for i in range(5)]
        results=executor.map(download_file,l1,l2)   #<-- map function contains list for both
        for r in results:
            print(r)

print("I put the downloading in the background")   # when I use join it stops then execute

""" Using multiprocessing it thorough's the function in the background and continue the program """

