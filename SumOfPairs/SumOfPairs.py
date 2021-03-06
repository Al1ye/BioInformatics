#!usr/bin/python
import array
import numpy

'''
This function reads the aligned sequences from the file 'SumOfPairs_Input.txt' 
The input is a set of aligned sequences
It also reads the standard distribution matrix from the file'PAM250.txt'
Usinf the Pam matrix, it calculates the column wise score for the aligned sequences.
'''
def calculateScore():
    # The score of the aligned sequences will be stored in this variable
    alignmentScore = 0
    invalidInput = False
    
    # Read the sequences to be aligned from the SP_Input.txt
    with open('SumOfPairs_Input.txt') as f:                         
        alignedSequences = [[x for x in ln] for ln in f] 
    for row in alignedSequences:
        if len(row) == len(alignedSequences[0]):
            print ""
        else:
            invalidInput = True   
     
    if invalidInput == False:
        # Load a standard distribution matrix
        with open('pam250.txt') as f:
            Pam250 = [[x for x in ln.split()] for ln in f] 
            Pam250[0] = [0] + Pam250[0] 
            
        # Delete the null entry at the tail of each sequence
        alignedSequences = numpy.delete(alignedSequences,numpy.s_[-1:],1)
        print "The aligned Sequences are:"
        print ""
        print alignedSequences
        print ""
        
        # Calculate the score for every column
        for column in range(0,len(alignedSequences[0])):
            for row in range(0,len(alignedSequences)):
                for index in range(row+1,len(alignedSequences)):
                    alignmentScore = alignmentScore + int(Pam250[Pam250[0].index(alignedSequences[row][column])][Pam250[:][0].index(alignedSequences[index][column])])
        print "Sum of Pairs score:",alignmentScore
    else:
        print "Error: The input sequences need to be aligned to calculate the Sum of pairs score"
    invalidInput = False
    
def main():
    calculateScore();

if __name__ == "__main__":
    main() 
