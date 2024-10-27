def prime_factorization(n):
    """
    Performs prime factorization of a given integer.
    
    Args:
        n: Integer to factorize
        
    Returns:
        List of tuples (prime_factor, exponent)
    """
    if n <= 1:
        return []
    
    factors = []
    curr_factor = 2
    
    while n > 1:
        if n % curr_factor == 0:
            # Count the exponent of current prime factor
            exponent = 0
            while n % curr_factor == 0:
                exponent += 1
                n //= curr_factor
            factors.append((curr_factor, exponent))
        
        # Move to next potential prime factor
        if curr_factor == 2:
            curr_factor = 3
        else:
            curr_factor += 2
            
        # Optimization: If curr_factor^2 > n, then n is prime
        if curr_factor * curr_factor > n and n > 1:
            factors.append((n, 1))
            break
    
    return factors