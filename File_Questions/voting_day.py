# On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. 
# Write a program that reads this file as a stream and returns the top 3 candidates at any given time. 
# If you find a voter voting more than once, report this as fraud.

# psudeo code,
# import the file first
# seperate the lines by ()
# take each voter id check the candidate_id 
# sum each time the candidate_id is counted. 
# if voter id == voter_id 
#     Send a message about fruad with the voteer id, don't count this vote'