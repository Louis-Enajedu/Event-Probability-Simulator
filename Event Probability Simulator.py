import numpy as np

# Function to calculate factorial, used in permutations and combinations calculations
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate permutations: nPr = n! / (n-r)!
def permutations(n, r):
    return factorial(n) / factorial(n-r)

# Function to calculate combinations: nCr = n! / (r!(n-r)!)
def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

# Bayes' Theorem: P(A|B) = P(B|A) * P(A) / P(B)
def bayes_theorem(p_a, p_b_given_a, p_b):
    return (p_b_given_a * p_a) / p_b

# Simulates the probability of an event occurring based on user-defined criteria
def simulate_event_probability(n_trials, event_probability):
    successes = 0
    for _ in range(n_trials):
        if np.random.random() < event_probability:
            successes += 1
    return successes / n_trials

# Main interactive loop for the simulator
def main():
    print("Event Probability Simulator")
    while True:
        n_trials = int(input("\nEnter the number of trials (0 to exit): "))
        if n_trials == 0:
            break

        simulation_type = input("Enter simulation type (event/bayes): ").lower()
        if simulation_type == "event":
            event_probability = float(input("Enter the event probability (0-1): "))
            probability = simulate_event_probability(n_trials, event_probability)
            print(f"Simulated Probability: {probability}")
        elif simulation_type == "bayes":
            p_a = float(input("Enter P(A): "))
            p_b_given_a = float(input("Enter P(B|A): "))
            p_b = float(input("Enter P(B): "))
            updated_probability = bayes_theorem(p_a, p_b_given_a, p_b)
            print(f"Updated Probability using Bayes' Theorem: {updated_probability}")
        else:
            print("Invalid simulation type entered.")

if __name__ == "__main__":
    main()
