class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        timeTaken = 0
        modifiedTickets = []
        numDict = {}

        for pos, val in enumerate(tickets):
            modifiedTickets.append((val, pos))
            numDict[pos] = val

        while numDict[k] > 0:
            value = modifiedTickets.pop(0)
            ticket = value[0]
            pos = value[1]
            ticket -= 1
            timeTaken += 1
            numDict[pos] = ticket
            if ticket != 0:
                modifiedTickets.append((ticket, pos))

        return timeTaken        

        