from typing import List

"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in words[0]:
            if all(i in j for j in words):
                res.append(i)
                words = [j.replace(i, '', 1) for j in words]
        return res


print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool", "lock", "cook"]))


