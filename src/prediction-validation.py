def reader(n):
    list = open(n,"r")
    list = [line.rstrip('\n') for line in list]
    for i in range(len(list)):
        list[i] = list[i].split("|")
    return list

def nested_Dict(list,max):
    a = {}
    for k in range(1,max+1):
        a[k]={}
        for i in range(len(list)):
            if(int(list[i][0])==k):
                a[k][(list[i][1])] = [list[i][2]]
    return a

def error_List(a,b,max):
    x = []
    for i in range(1,max+1):
        x.append([abs(float(a[i][key][0])-float(b[i][key][0])) 
        for key in a[i] if key in b[i]])
    
    return x

def average_Error(a,window,max):
    for k in range(1,max+1):
        numerator = 0
        denominator = 0
        if(k+(window-1)<=max):
            for i in range(k,k+(window)):
                numerator += sum(a[i-1])
                denominator += len(a[i-1])
            if denominator == 0:
                file.write("{}|{}|{}\n".format(k,k+(window-1),"NA"))
            else:
                file.write("{}|{}|{}\n".format(k,k+(window-1),
                   round(numerator/float(denominator),2)))
    return
    
                
file = open('out.txt', 'w')
window = 4

actual = reader("act.txt")

predict = reader("pred.txt")

max = int(predict[-1][0])

act = nested_Dict(actual,max)

pred = nested_Dict(predict,max)

error = error_List(act,pred,max)

average_Error(error,window,max)

