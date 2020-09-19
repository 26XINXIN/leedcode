class Solution:
    def nextClosestTime(self, time: str) -> str:
        def time_diff(h1, m1, h2, m2):
            if h1 < h2:
                if m1 <= m2:
                    time_diff = (h2 - h1) * 60 + (m2 - m1)
                else:
                    time_diff = (h2 - h1 - 1) * 60 + (m2 + 60 - m1)
            elif h1 == h2:
                if m1 <= m2:
                    time_diff = m2 - m1
                else:
                    time_diff = 23 * 60 + (m2 + 60 - m1)
            else:
                if m1 <= m2:
                    time_diff = (h2 + 24 - h1) * 60 - (m2 - m1)
                else:
                    time_diff = (h2 + 24 - h1 - 1) * 60 + (m2 + 60 - m1)
            return time_diff
        
        def is_valid_time(h, m):
            return 0 <= h < 24 and 0 <= m < 60
        
        h, m = time.split(':', 1)
        digits = set(h + m)
        h = int(h)
        m = int(m)
        closest_time = 24 * 60
        closest_h = None
        closest_m = None
        for a in digits:
            for b in digits:
                for c in digits:
                    for d in digits:
                        hh = int(a + b)
                        mm = int(c + d)
                        
                        if is_valid_time(hh, mm):
                            td = time_diff(h, m, hh, mm)
                            if td == 0: continue
                            if td < closest_time:
                                closest_time = td
                                closest_h = hh
                                closest_m = mm
        return "{:02}:{:02}".format(closest_h, closest_m)
        