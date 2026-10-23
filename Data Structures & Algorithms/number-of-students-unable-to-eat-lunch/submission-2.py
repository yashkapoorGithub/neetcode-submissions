class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = j = ctr = 0 
        total = len(students)
        while True and i < len(students):
            if ctr >= len(sandwiches) - j:
                break
            if students[i] == sandwiches[j]:
                students[i] = -1
                sandwiches[j] = -1
                i += 1
                j += 1
                ctr = 0
            
            else:
                students.append(students[i])
                students[i] = -1
                i += 1
                ctr += 1
        
        return len(sandwiches)-j