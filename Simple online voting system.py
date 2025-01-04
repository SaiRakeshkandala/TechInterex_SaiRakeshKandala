Simple Online Voting System - Python Project
Source Code

# Simple Online Voting System
# Developed in Python

# Data structures to store candidates and voters
candidates = {'Candidate 1': 0, 'Candidate 2': 0, 'Candidate 3': 0}
voters = set()

# Function to display the list of candidates
def display_candidates():
    print("\nAvailable Candidates:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to allow users to vote
def vote(voter_id):
    if voter_id in voters:
        print("You have already voted.")
        return
    print("\nPlease choose a candidate to vote for:")
    display_candidates()
    choice = input("Enter the candidate name: ").strip()
    if choice in candidates:
        candidates[choice] += 1
        voters.add(voter_id)
        print(f"Thank you for voting! Your vote for '{choice}' has been recorded.")
    else:
        print("Invalid candidate. Please try again.")

# Function to view results (admin only)
def view_results():
    print("\nCurrent Voting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to reset votes (admin only)
def reset_votes():
    global candidates, voters
    for candidate in candidates:
        candidates[candidate] = 0
    voters.clear()
    print("\nVoting system has been reset.")

# Main program loop
def main():
    while True:
        print("\n=== Simple Online Voting System ===")
        print("1. Vote")
        print("2. View Results (Admin Only)")
        print("3. Reset Votes (Admin Only)")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            voter_id = input("Enter your Voter ID: ").strip()
            vote(voter_id)
        elif choice == '2':
            admin_password = input("Enter admin password: ").strip()
            if admin_password == "admin123":  # Replace with a secure password
                view_results()
            else:
                print("Incorrect admin password.")
        elif choice == '3':
            admin_password = input("Enter admin password: ").strip()
            if admin_password == "admin123":  # Replace with a secure password
                reset_votes()
            else:
                print("Incorrect admin password.")
        elif choice == '4':
            print("Exiting the voting system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()


