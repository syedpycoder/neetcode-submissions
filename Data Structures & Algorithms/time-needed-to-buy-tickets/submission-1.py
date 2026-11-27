class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        timeTaken = 0
        ticket = tickets[k]
        modifiedTickets = []
        numDict = {}

        for pos,value in enumerate(tickets):
            modifiedTickets.append((value, pos))
            numDict[pos] = value
        

        while numDict[k] > 0:
            val = modifiedTickets.pop(0)
            ticket = val[0]
            pos = val[1]
            ticket -= 1
            numDict[pos] = ticket
            timeTaken += 1
            if ticket != 0:
                modifiedTickets.append((ticket, pos))

        return timeTaken    

        