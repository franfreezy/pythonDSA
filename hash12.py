
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D 
# matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

class matrixRotation:
    def __init__(self, inmatrix):
        self.inmatrix=inmatrix

    def rotate(self):
        self.inmatrix=self.inmatrix[::-1] #reverses order
        
        i=0
        oldarr=[]
        while i!=3:
            newarr=[]
            for array in self.inmatrix:
                newarr.append(array[i])
                
                
            oldarr.append(newarr)
            print(oldarr)
            i+=1
        
            

if __name__=='__main__':
    inmatrix= [[1,2,3],[4,5,6],[7,8,9]]
    item=matrixRotation(inmatrix)
    item.rotate()