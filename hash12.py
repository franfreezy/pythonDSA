
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
        print('HERE')
        i=0
        
        while i!=3:
            for array in self.inmatrix:
                print(array[i] , end=' ')
                
            print('space')
            i+=1
        
            

if __name__=='__main__':
    inmatrix= [[1,2,3],[4,5,6],[7,8,9]]
    item=matrixRotation(inmatrix)
    item.rotate()