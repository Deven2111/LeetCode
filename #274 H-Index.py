#274. H-Index
#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index. According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citation_buckets = [0] * (n+1)
        
        for citation in citations:
            citation_buckets[min(citation,n)] += 1
        
        cumulative_papers = 0
        for h_index in range(n,-1,-1):
            cumulative_papers += citation_buckets[h_index]
            if cumulative_papers >= h_index:
                return h_index