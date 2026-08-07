def calculate_fare(base_distance: float, traffic_multiplier: float, is_peak_hour: bool) -> float:
    # Phase 1: Compute standard baseline distance cost
    usr_fare = base_distance * 15.0 * traffic_multiplier
    
    # Phase 2: Add independent surge premiums if flags are active
    if is_peak_hour: # Note: '== True' is redundant for booleans!
        usr_fare = usr_fare + 50.0
        
    # Phase 3: Enforce platform system safety limits globally
    if usr_fare < 60.0:
        usr_fare = 60.0
        
    # Phase 4: Communicate the finalized data result back to the caller
    return usr_fare

# --- Verification Test Suite ---
print(calculate_fare(2, 1.0, False)) # Outputs: 60.0 (Floor limit override caught)
print(calculate_fare(5, 1.2, True))  # Outputs: 140.0 (Standard peak calculation verified)
print(calculate_fare(0.5, 1.0, True)) # Outputs: 60.0 (Peak premium factored, floor enforced)