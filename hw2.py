import sys
import math
import string

alphabet = list(string.ascii_uppercase)


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26
 

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    findings = [0]*26
    num = -1
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            line = line.upper().replace(" ", "")
            characters = list(line)
            #line = line.strip()
            #print(letters)
        for i in alphabet:
            for j in characters:
                if j==i:
                    findings[ord(i) - ord('A')] += 1
                    #print(findings)
                    #print("match", j, i)
        print("Q1")
        for i in alphabet:
            num +=1
            print(alphabet[num], findings[num])
        #print(findings)
        return findings

def compute_q2(findings, e, s):
    # X1 is the count of 'A', which is stored in index 0 (for 'A') of letter_counts
    X1 = findings[0]  # if using dictionary; letter_counts[0] if using list
    
    # e1 and s1 are the probabilities of 'A' in English and Spanish
    e1 = e[0]
    s1 = s[0]
    
    # Compute X1 * log(e1) and X1 * log(s1)
    # Use math.log to compute the natural logarithm
    # Handle the case when e1 or s1 is 0 to avoid log(0)
    X1_log_e1 = X1 * math.log(e1) if e1 > 0 else 0.0
    X1_log_s1 = X1 * math.log(s1) if s1 > 0 else 0.0
    
    # Print Q2 results with four decimal places
    print("Q2")
    print(f"{X1_log_e1:.4f}")
    print(f"{X1_log_s1:.4f}")



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
def main():
    letter_counts = shred("test.txt")
    compute_q2(letter_counts, e.txt, s.txt)


    # Call the main function
if __name__ == "__main__":
    main()