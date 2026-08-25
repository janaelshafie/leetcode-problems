class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        ate = 0
        n = len(students)

        count_0 = 0
        count_1 = 0

        for s in students:
            if s == 0:
                count_0 += 1
            else:
                count_1 += 1

        for s in sandwiches:
            if s == 0 and count_0 > 0:
                count_0 -= 1
                ate += 1
            elif s == 1 and count_1 > 0:
                count_1 -= 1
                ate += 1

            elif (s == 0 and count_0 == 0) or (s == 1 and count_1 == 0):
                break

        return n - ate
        