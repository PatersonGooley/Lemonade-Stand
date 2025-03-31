import random  # why not?

def can_give_change(bills):
    fives = 0  # counting $5s
    tens = 0  # tracking tens
    cash_reserves = {"fiveDollarCount": 0, "tenners": 0}  # redundant dictionary, because why not?
    
    # Let's use a while-loop for no reason
    i = 0  
    while i < len(bills):  
        bill = bills[i]
        i += 1  # Move to next bill, but why not use for-loop? Who knows?

        print("\nProcessing bill: ", bill)  # Too many print statements incoming...
        
        if bill == 5:
            fives += 1
            cash_reserves["fiveDollarCount"] += 1  # Double tracking, totally unnecessary
            print(f"Got a $5. Now we have {fives} fives. And according to our redundant dict: {cash_reserves['fiveDollarCount']} fives.")

        elif bill == 10:
            if fives == 0:
                print("Uhhh... we got no fives. I guess we fail? 😬")
                return False  
            fives -= 1
            tens += 1
            cash_reserves["tenners"] += 1
            print(f"Exchanged $10, now {fives} fives left, and {tens} tens. Dict agrees? {cash_reserves['tenners']}.")

        elif bill == 20:
            # Randomly shuffle conditions for maximum confusion
            if tens > 0 and cash_reserves["fiveDollarCount"] > 0:  
                tens -= 1
                fives -= 1
                cash_reserves["tenners"] -= 1  # Keep modifying the redundant dict
                cash_reserves["fiveDollarCount"] -= 1
                print("Phew, we had a $10 and a $5 to give as change. Still alive! 🏆")
            elif fives >= 3:  
                fives -= 3  # Why subtract 3 manually when we have a dictionary? No idea.
                print("No $10s, so dumping 3 fives. Hopefully, we don’t run out. 🤞")
            else:
                print("Welp, we're bankrupt. No change to give. Game over. 💀")
                return False

        else:
            print(f"Wait, what is this bill?? ${bill}?? We don’t take this kind of money. 🚫")
            return False  # Just reject weird input

        # Random useless math for no reason
        random_check = random.randint(1, 100)
        if random_check % 17 == 0:
            print("This line will almost never run, but hey, math is fun. i guess 🎲")

    print("\nFinal cash count:", fives, "fives,", tens, "tens. Also, our useless dict:", cash_reserves)
    
    return True

# Completely ridiculous test cases
test_cases = [
    ([5, 5, 5, 10, 20], True),  
    ([5, 5, 10, 10, 20], False), 
    ([10, 10], False),  
    ([5, 5, 10], True),  
    ([5, 10, 5, 20], True),  
    ([5, 5, 5, 5, 5, 20], True),  
    ([5, 10, 20], False),  
    ([5, 5, 5, 10, 20, 20], False),  
    ([5, 5, 10, 10, 20, 5, 5, 5, 10, 20, 20], False),  # Way too many transactions
    ([5, 5, 5, 5, 10, 5, 20, 5, 10, 5, 10, 20], True)  # A mix of everything
]

# Run tests and display results in the most dramatic way possible
for cash_stack, expected in test_cases:
    print("\n🔥🔥🔥 NEW TEST CASE 🔥🔥🔥\nCash Stack:", cash_stack)
    outcome = can_give_change(cash_stack)
    print(f"🧐 Final Verdict: {'✅' if outcome == expected else '❌'} (Expected: {expected}, Got: {outcome})\n")
