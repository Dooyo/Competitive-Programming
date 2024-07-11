# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def getFreqArray(self,string):
        freq = [0]*26
        for character in string:
            freq[ord(character)-97] += 1
        return freq
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freq_arr = self.getFreqArray(string);
                
            #if frequency array in dictionary append it to it's members
            freq_tuple = tuple(freq_arr)
            if freq_tuple in anagrams:
                anagrams[freq_tuple].append(string)
            
            #else create new array with that anagram
            else:
                anagrams[freq_tuple] = [string]
            
        # return all the list in the dictionary
        return anagrams.values()
            