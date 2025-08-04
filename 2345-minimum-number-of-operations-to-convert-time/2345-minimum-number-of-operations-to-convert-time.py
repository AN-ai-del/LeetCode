class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        s = 0
        current_hours = int(current[0])*10 + int(current[1])
        correct_hours = int(correct[0])*10 + int(correct[1])
        current_mins = int(current[3])*10 + int(current[4])
        correct_mins = int(correct[3])*10 + int(correct[4])
        diff = (correct_hours*60 + correct_mins) - (current_hours*60 + current_mins)
        print(diff)
        for op in [60, 15, 5, 1]:
            if diff>=op:
                s+=diff//op
                diff-=op*(diff//op)
                
        return s