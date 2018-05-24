'''
Created on May 21, 2018

@author: ju
'''


class LevenshteinDistance:
    '''
    LevenshteinDistance is a helper class to compute the distanse between two given strings
    '''

    def __init__(self):
        '''
        Constructor
        '''

    # recursive version
    def getDistance(self, str1, str2):
        len_str1 = len(str1);
        len_str2 = len(str2);
        
        if min([len_str1, len_str2]) == 0:
            value = max([len_str1, len_str2])
        else:
            val_1 = self.getDistance(str1[1:], str2) + 1
            val_2 = self.getDistance(str1, str2[1:]) + 1
            val_3 = self.getDistance(str1[1:], str2[1:]) + self.getCharDistance(str1[0], str2[0])
            value = min([val_1, val_2, val_3])
        
        print("value of '{0}', '{1}' is: {2}".format(str1, str2, str(value)))
        return value
    
    def getCharDistance(self, c1, c2):
        if c1 == c2: return 0
        else: return 1;
