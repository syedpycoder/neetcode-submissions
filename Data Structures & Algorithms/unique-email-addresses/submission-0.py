class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        uniqueEmail = set()

        for email in emails:
            split_email = email.split('@')
            localName = split_email[0]
            domainName = split_email[1]

            if '.' in localName and '+' in localName:
                localPlusSplit = localName.split('+')
                if '.' in localPlusSplit[0]:
                    localDotSplit = localPlusSplit[0].split('.')
                    filteredLocal = ''.join(localDotSplit)
                else:
                    filteredLocal = localPlusSplit[0]    
            elif '.' in localName:
                localDotSplit = localName.split('.')
                filteredLocal = ''.join(localDotSplit)
            elif '+' in localName:
                localPlusSplit = localName.split('+')
                filteredLocal = localPlusSplit[0]  
            else:
                filteredLocal = localName
            
            finalEmail = filteredLocal + '@' + domainName
            uniqueEmail.add(finalEmail)

        return len(uniqueEmail)    