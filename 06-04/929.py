from typing import *


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            items = email.split('@')
            local_name, domain_name = items[0], items[1]
            pos = email.find('+')
            if pos != -1:
                local_name = email[:pos]
            local_name = local_name.replace('.', '')
            res.add(local_name + '@' + domain_name)
        return len(res)


if __name__ == "__main__":
    sol = Solution()
    # emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    # emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    print(sol.numUniqueEmails(emails))

