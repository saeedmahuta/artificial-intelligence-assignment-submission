import sys

# --- PART 1: The Scale Simulator ---
class BalanceScale:
    def __init__(self, fake_coin, is_heavy):
        self.fake_coin = fake_coin
        self.is_heavy = is_heavy
        self.weighs_used = 0

    def weigh(self, left, right):
        self.weighs_used += 1
        if self.weighs_used > 3:
            raise Exception("FAIL: Exceeded 3 weighs limit!")
        
        # Calculate weight: Normal=0, Heavy=1, Light=-1
        l_sum = sum([1 if c == self.fake_coin and self.is_heavy else 
                    -1 if c == self.fake_coin and not self.is_heavy else 0 for c in left])
        r_sum = sum([1 if c == self.fake_coin and self.is_heavy else 
                    -1 if c == self.fake_coin and not self.is_heavy else 0 for c in right])
        
        # Returns: -1 (Left < Right), 0 (Equal), 1 (Left > Right)
        if l_sum < r_sum: return -1
        if l_sum > r_sum: return 1
        return 0

# --- PART 2: Algorithm 1 (Adaptive / Decision Tree) ---
def solve_adaptive(scale):
    # Weigh 1
    w1 = scale.weigh([1, 2, 3, 4], [5, 6, 7, 8])
    
    if w1 == 0:
        # Fake is in 9-12
        w2 = scale.weigh([1, 2, 3], [9, 10, 11]) # 1,2,3 are Real
        if w2 == 0:
            w3 = scale.weigh([1], [12])
            return "12 is " + ("Light" if w3 > 0 else "Heavy")
        else:
            is_heavy = (w2 < 0) # If Real(L) < Target(R), Target is Heavy
            w3 = scale.weigh([9], [10])
            if w3 == 0: return f"11 is {'Heavy' if is_heavy else 'Light'}"
            if is_heavy: return "9 is Heavy" if w3 > 0 else "10 is Heavy"
            else:        return "9 is Light" if w3 < 0 else "10 is Light"

    elif w1 > 0: # Left Heavy
        w2 = scale.weigh([1, 2, 5], [3, 6, 12])
        if w2 == 0:
            w3 = scale.weigh([7], [8])
            if w3 == 0: return "4 is Heavy"
            return "7 is Light" if w3 < 0 else "8 is Light"
        elif w2 > 0:
            w3 = scale.weigh([1], [2])
            if w3 == 0: return "6 is Light"
            return "1 is Heavy" if w3 > 0 else "2 is Heavy"
        else:
            w3 = scale.weigh([3], [12])
            return "3 is Heavy" if w3 > 0 else "5 is Light"
            
    else: # Right Heavy
        w2 = scale.weigh([1, 2, 5], [3, 6, 12])
        if w2 == 0:
            w3 = scale.weigh([7], [8])
            if w3 == 0: return "4 is Light"
            return "7 is Heavy" if w3 > 0 else "8 is Heavy"
        elif w2 < 0:
            w3 = scale.weigh([1], [2])
            if w3 == 0: return "6 is Heavy"
            return "1 is Light" if w3 < 0 else "2 is Light"
        else:
            w3 = scale.weigh([3], [12])
            return "3 is Light" if w3 < 0 else "5 is Heavy"

# --- PART 3: Algorithm 2 (Non-Adaptive / Vector) ---
def solve_vector(scale):
    # Static Weighing Schedule (Decided upfront)
    left_1, right_1 = [1, 2, 3, 4],  [5, 6, 7, 8]
    left_2, right_2 = [1, 2, 9, 10], [3, 4, 5, 6]
    left_3, right_3 = [1, 3, 5, 9],  [2, 4, 11, 12] 
    
    # Perform all weighs blindly
    r1 = scale.weigh(left_1, right_1)
    r2 = scale.weigh(left_2, right_2)
    r3 = scale.weigh(left_3, right_3)
    
    syndrome = (r1, r2, r3)
    
    # Check which coin matches this vector
    for coin in range(1, 13):
        # Calculate theoretical vector if this coin was Heavy
        s1 = 1 if coin in left_1 else (-1 if coin in right_1 else 0)
        s2 = 1 if coin in left_2 else (-1 if coin in right_2 else 0)
        s3 = 1 if coin in left_3 else (-1 if coin in right_3 else 0)
        
        if syndrome == (s1, s2, s3): return f"{coin} is Heavy"
        if syndrome == (-s1, -s2, -s3): return f"{coin} is Light"
            
    return "Error"

# --- PART 4: Execution / Testing ---
print(f"{'SCENARIO':<20} | {'ALGORITHM 1 (Tree)':<25} | {'ALGORITHM 2 (Vector)':<25}")
print("-" * 75)

# Test every coin (1-12) being Heavy, then Light
for coin in range(1, 13):
    for weight in ["Heavy", "Light"]:
        is_heavy = (weight == "Heavy")
        
        # Test Algo 1
        s1 = BalanceScale(coin, is_heavy)
        res1 = solve_adaptive(s1)
        
        # Test Algo 2
        s2 = BalanceScale(coin, is_heavy)
        res2 = solve_vector(s2)
        
        # Print Result
        scenario_name = f"Coin {coin} is {weight}"
        print(f"{scenario_name:<20} | {res1:<25} | {res2:<25}")

# --- PART 5: Single Run Execution ---

# 1. HIDE THE COIN (You choose the mystery here)
target_coin = 7          # Change this to any number 1-12
target_is_heavy = False  # True for Heavy, False for Light

print(f"HIDDEN TRUTH: Coin {target_coin} is {'Heavy' if target_is_heavy else 'Light'}")
print("-" * 50)

# 2. Run Algorithm 1 (The Tree)
# We create a new scale instance with the hidden truth
scale_1 = BalanceScale(target_coin, target_is_heavy) 
result_1 = solve_adaptive(scale_1)
print(f"Algorithm 1 found: {result_1}")

# 3. Run Algorithm 2 (The Vector)
scale_2 = BalanceScale(target_coin, target_is_heavy)
result_2 = solve_vector(scale_2)
print(f"Algorithm 2 found: {result_2}")

