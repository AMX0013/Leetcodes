class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res= []
        lineWords = []
        line = ""

        # minSpace = 1*" "
        # print("minspace:", minSpace)

        linelen = 0

        # Note: Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.

        for wordIdx in range(len(words)):
            word = words[wordIdx]

            if linelen +len(lineWords) + len(word) > maxWidth :
              
                # Adjust line with equal padding
                    # first we find no. of words

                # print(res)
                print("lineWords",lineWords)

                gaps = max(len(lineWords)-1 , 1)

                # there are "gaps" single spaces
                # now we extend these single spaces evenly

                spacesLeft = maxWidth - (linelen)

                evenspace = spacesLeft//gaps
                remainder = spacesLeft % gaps

                for i in range( max( 1 , len(lineWords)-1 ) ):
                    lineWords[i] += " " * evenspace
                    if remainder:
                        lineWords[i] += " "
                        remainder -=1

                res.append("".join(lineWords))

                # clear variables
                lineWords = []
                line = ""
                linelen = 0

            # dont forget to add
            # add words to curr line's words
            lineWords.append(word)
            # adjust line's min len with 1 space
            linelen += len(word)

            if wordIdx == len(words) -1:
                # reached last element
                # current line must be left -justified
                for i in range(len(lineWords)-1):
                    line += lineWords[i]
                    line+=" "
                line+=lineWords[-1]
                # find rest of the space
                leftoverspace = maxWidth - len(line)
                line+= " "*leftoverspace
                res.append(line)
                return res
