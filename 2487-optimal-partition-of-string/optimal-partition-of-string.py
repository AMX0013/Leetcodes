class Solution:
    def partitionString(self, s: str) -> int:
        # given a string s

        # create substrings
            # substring rule 1: characters in each substring are uniq (one ocurrence)
            # substring rule 2:
        i = 0
        partition = []
        substr = set()
        while i < len(s):
            
            while i < len(s):
                if s[i] in substr:
                    # substr we had so far, is it
                    partition.append("".join(substr))
                    substr = set()
                    break
                else:
                    # add to substr
                    substr.add(s[i])
                    i+=1
        # add last one
        partition.append("".join(substr))

        print(partition)
        return len(partition)

        # Partition(substrings)
            # substring : substrings, each substring is unique


        # Goal minimize partition size
        # return min no. of sub in such partition
        