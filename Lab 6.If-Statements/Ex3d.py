def determine_progress4(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    progress = {
        0: "Get going!",
        1: "On your way!",
        2: "Almost there!",
        3: "You win!"     
    }

    progress_index =  (hits_spins_ratio > 0)*1 + (hits_spins_ratio >= 0.25)*1 + (hits_spins_ratio >= 0.5 and hits < spins)*1

    return progress[progress_index]

def test_determine_progress(determine_progress):
    # Test "Get going!" cases
     assert determine_progress(0, 0) == "Get going!"
     assert determine_progress(0, 10) == "Get going!"
    
     # Test "On your way!" cases
     assert determine_progress(1, 5) == "On your way!"
     assert determine_progress(3, 15) == "On your way!"

     # Test "Almost there!" cases
     assert determine_progress(4, 10) == "Almost there!"
     assert determine_progress(6, 20) == "Almost there!"

     # Test "You win!" cases
     assert determine_progress(5, 10) == "You win!"
     assert determine_progress(6, 10) == "You win!"

    # Edge cases
     assert determine_progress(10, 10) == "Almost there!"
     assert determine_progress(11, 10) == "Almost there!"
    
     print("All tests passed!")

# Run the tests
test_determine_progress(determine_progress4)