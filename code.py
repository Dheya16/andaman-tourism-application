import matplotlib.pyplot as plt
import matplotlib.image as mpimg


ch='y'
while(ch=='y'):
    c=int(input("Choice:"))
    if c==1:
        plt.xticks([])
        plt.yticks([])
        img = mpimg.imread("andamanmap.jpg")
        print("The Cellular Jail, also known as Kālā Pānī, was a colonial prison in the Andaman and Nicobar Islands, India. The prison was used by the British for the express purpose of exiling political prisoners to the remote archipelago.")
        plt.imshow(img)
        plt.show()
    elif c==2:
        plt.xticks([])
        plt.yticks([])
        img = mpimg.imread("lakshadweepmap.jpg")
        plt.imshow(img)
        plt.show()
    ch=input("continue:")