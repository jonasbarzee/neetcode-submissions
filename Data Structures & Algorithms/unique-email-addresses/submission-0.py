class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = {}
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            clean = local + "@" + domain
            if clean not in seen:
                seen[clean] = True
        print(seen)
        return len(seen)

        