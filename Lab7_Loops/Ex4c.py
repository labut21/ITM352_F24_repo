def check_fare(fare):
# Checks if the fare is high or low
   if fare > 12:
       return f"{fare}: This fare is high!"
   else:
       return f"{fare}: This fare is low"
  
def test_check_fare():
# Test cases to test the check_fare function
   test_fares = [8.60, 5.75, 13.25, 21.21, 12.00, 12.01]
   expected_results = [
       "8.6: This fare is low",
       "5.75: This fare is low",
       "13.25: This fare is high!",
       "21.21: This fare is high!",
       "12.0: This fare is low",  # Edge case
       "12.01: This fare is high!"
   ]
  
   # Iterate through test cases
   for i, fare in enumerate(test_fares):
       result = check_fare(fare)
       assert result == expected_results[i], f"Test failed for fare {fare}: {result}"


   print("All test cases passed!")


test_check_fare()