import csv
import os

#Path to collect data from the resource folder 
election_data_csv = os.path.join("Resources", "election_data_csv")
election_data_csv

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes= {} # dictionary

# Winning candidate and Winning Count Tracker

winning_candidate= ""

winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open ("Resources/election_data.csv") as election_data:
    reader= csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Run the loader animation
        #print(".",end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 

        # (In a way, our loop is "discovering" candidates as it goes)

    # If the candidate does not match any existing candidate...
      # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name]= 0

        # Then add a vote to that candidate's count
            candidate_votes[candidate_name]=candidate_votes[candidate_name] + 1


    #Print the results and export the data to our text file
    with open("output.txt","w") as txt_file:

        #Print the final vote count (to terminal)
        election_results = (
            f"\n\nElection Results\n"
            f"-------------------\n"
            f"Total Votes: {total_votes}\n"
            f"----------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

        # Determine the winner by looping through the counts
        for candidate in candidate_votes:

            # Retrieve vote count and percentage
            votes=candidate_votes.get(candidate)

            vote_percentage = float(votes) / float(total_votes)*100

        # Determine winning vote count and candidate
            if (votes>winning_count):
                winning_count = votes
                winning_candidate = candidate

            # Print each candidate's voter count and percentage (to terminal)
            voter_output = f"{candidate}:{vote_percentage:.3f}% ({votes})\n"
            print(voter_output, end="")

            # Save each candidate's voter count and percentage to the text file
            txt_file.write(voter_output)

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
          f"-----------------\n"
          f"Winner:{winning_candidate}\n"
          f"--------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)