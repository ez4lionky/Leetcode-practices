from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for pair in cpdomains:
            num, domain = pair.split(' ')
            num = int(num)
            counter[domain] += num

            while '.' in domain:
                domain = domain[domain.find('.') + 1:]
                counter[domain] += num
        return [f"{c} {s}" for s, c in counter.items()]

