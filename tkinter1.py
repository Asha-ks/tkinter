from tkinter import Tk, Label, IntVar, Button, Entry
window = Tk()
window.title("Matrix")
window.geometry("650x500+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

# callback function to get your StringVars
def get_mat():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())
    print("matrix=",matrix)
    

    neighbours= lambda x,y:[(x2,y2) for x2 in range(x-1, x+2) 
                            for y2 in range(y-1, y+2) 
                            if(-1< x <rows and 
                               -1< y <cols and 
                               (x!=x2 or y!=y2) and 
                               (0<=x2<rows) and 
                               (0<=y2<cols))]
    def find_neighbour(z):
        l1=len(z)
        list1=[]
        list2=[]
        for i in range(0,l1):
            k=z[i][0]
            h=z[i][1]
            a=matrix[k][h]
            list1.append(a)
        max1=max(list1)
        print("neighbour values are:", list1)
        for j in range(0,l1):
            m=z[j][0]
            n=z[j][1]
            if matrix[m][n]==max1:
                list2.append((m,n))
        print("index of highest value:",list2)
        print("highest value is:", max1)
        list3.append(max1)
        return list2


    x=0
    y=0
    list3=[]
    totalvalue=0
    l=len(matrix)
    matrix[x][y]=0
    for s in range(0,l*l):
        z=neighbours(x,y)
        v=find_neighbour(z)
        for g in range(0,len(v)):
            x=v[0][0]
            y=v[0][1]
            matrix[x][y]=0

    print(matrix)
    for h in range(0,len(list3)):
        totalvalue+=list3[h]
    print("total count of highest values:",totalvalue)
Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), 
      bg="bisque2").place(x=20, y=20)

x2 = 0
y2 = 0
rows, cols = (5,5)


for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(IntVar())
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=60 + x2, y=50 + y2)
        x2 += 30

    y2 += 30
    x2 = 0
button= Button(window,text="Submit", bg='bisque3', width=15, command=get_mat)
button.pack(pady=180)
window.mainloop()