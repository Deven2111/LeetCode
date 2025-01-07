#1408. String Matching in an Array
#Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order. A substring is a contiguous sequence of characters within a string

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []

        for current_word_index in range (len(words)):
            for other_word_index in range (len(words)):
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break
        return matching_words