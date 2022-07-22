 def splitString(self, s: str) -> bool:
        def find_split(cur_idx, n_splits, target):
            if cur_idx == len(s) and n_splits >= 2:
                return True

            val = 0
            for i in range(cur_idx, len(s)):
                val = val * 10 + int(s[i])
                if target is None and val == 0:  # Skip leading 0s.
                    continue
                if target is None or val == target:
                    if find_split(i + 1, n_splits + 1, val - 1):
                        return True
                if target and val > target:  # Early break.
                    break

            return False
    
        return find_split(0, 0, None)
