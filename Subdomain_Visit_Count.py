# https://leetcode.com/problems/subdomain-visit-count/

from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        hash_map = defaultdict(int)

        for domain in cpdomains:
            count, domain_node = domain.split(" ")
            domain_list = domain_node.split(".")
            # print(domain_list)
            prev_domain = ''
            for domain_idx in range(len(domain_list) - 1, -1, -1):
                prev_domain = ".".join(domain_list[domain_idx:])
                hash_map[prev_domain] += int(count)

        return [str(value) + " " + key for key, value in hash_map.items()]


if __name__ == "__main__":
    obj = Solution()
    print(obj.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))