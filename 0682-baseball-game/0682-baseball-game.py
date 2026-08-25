class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        records = []
        for op in operations:
            if op not in ['C', '+', 'D']:
                records.append(int(op))

            elif op == '+':
                records.append(records[-1] + records[-2])

            elif op == 'D':
                records.append(records[-1] * 2)

            elif op == 'C':
                records.pop()
        
        return sum(records)
         
        