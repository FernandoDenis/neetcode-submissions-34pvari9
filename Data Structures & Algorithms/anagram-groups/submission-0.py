class Solution:

    # dictWords {act:[act, cat], pots:[pots, tops, stop], aht: [hat]}
    #       i
    # srt ["act","pots","tops","cat","stop","hat"]
    # act


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictWords = {}

        for i in strs:
            sortedWord = "".join(sorted(i))
            if sortedWord in dictWords:
                dictWords[sortedWord].append(i)
            else:
                dictWords[sortedWord] = [i]

        res = []

        for key, val in dictWords.items():
            res.append(val)

        return res
        