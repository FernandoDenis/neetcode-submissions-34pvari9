class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_letters = Counter(s1)

        for idx,letter in enumerate(s2):
            if idx + len(s1) > len(s2):
                break

            if letter in dict_letters:
                copy_dict = dict_letters.copy()
                is_Permutation = True

                for i in range(idx, idx + len(s1)):
                    if s2[i] in copy_dict and copy_dict[s2[i]] > 0:
                        copy_dict[s2[i]] -= 1
                    else:
                        is_Permutation = False
                        break

                if is_Permutation:
                    return True

        return False
        