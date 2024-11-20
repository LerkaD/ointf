import matplotlib.pyplot as plt

y_arr = [0, 4,4, 4,0 ]

q_matrix = [[-2.25,1,0,0,0],[1,-2,1,0,0],[0,1,-2,1,0],[0,0,1,-2,1],[0,0,0,1,-2.25]]

error = 0.0001


def update_matrix(arr, new_arr,w):
    for i in range(len(arr)):
       new_arr[i] = w * new_arr[i] + (1-w)*arr[i]
    return new_arr

def calculate_error(arr,newarr):
    error_list = [0] * 5
    for i in range(len(newarr)):   
        error_list[i] = abs(newarr[i] - arr[i])
    return  max(error_list)
    

def createnewarr(arr):
    newarr = [0]*5
    for i in range(len(arr)):
        for q in range(len(q_matrix)):
            if (i!=q):
                newarr[i] -= arr[q] * q_matrix[i][q]
        newarr[i] += y_arr[i]
        newarr[i] = newarr[i] / q_matrix[i][i]
    return newarr

def printplot(warr,steparray):
    plt.plot(warr, steparray)
    plt.show()

def main():
    warr = [w/10 for w in range(2, 20, 2)]
    steparray = []
    rezxarr = []
    for w in warr:
        step = 0
        x_arr  = [0,0,0,0,0]
        cur_errr = 1
        while cur_errr > error:
            step += 1
            new_x_arr = createnewarr(x_arr)
            cur_errr = calculate_error(x_arr, new_x_arr)
            x_arr = update_matrix(x_arr,new_x_arr,w)       
        steparray.append(step)
        rezxarr.append(x_arr)
        ''''
        print("W = " + str(w) + "\nStep = " + str(step))
        if step < 500:
            print("Rezult = " + str(x_arr))
        print("--------------------------------------------------------------------")
        '''
    print("W for min step = " + str(warr[steparray.index(min(steparray))]))
    print("Minimal step = " + str(min(steparray)))
    print("Rezult: " + str(rezxarr[steparray.index(min(steparray))]))
    printplot(warr,steparray)

if __name__ == "__main__":
    main()