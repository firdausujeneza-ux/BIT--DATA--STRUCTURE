# ==== import libraries======
import array

# List that contains the Peer Review Scores
peer_review_scores = [78, 85, 92, 67, 88, 73, 90, 81, 95]

#Generate Report using f-strings
report = (
    f" The report of Peer Review Scores is {peer_review_scores} \n"
    f" The Total of Peer Review Scores is:  {sum(peer_review_scores)} \n"
    f" The Average of Peer Review Scores is:  {round(sum(peer_review_scores) / len(peer_review_scores), 2)} \n"
    f" The Minimum of Peer Review Scores is:  {min(peer_review_scores)} \n"
    f" The Maximum of Peer Review Scores is:  {max(peer_review_scores)} \n"
)
print(report)

# Threshold condition (Booleans)
average = sum(peer_review_scores) / len(peer_review_scores)
percentage = round(average * 100, 2)
threshold = 75
if percentage > threshold and max(peer_review_scores) > 80:
    print(f" The average exceeds the threshold: {round(average, 2)} -> Above Standard")
else:
    print(f" The average exceeds the threshold: {round(average, 2)} -> Below Standard")

# Maintain list: Add, Remove, Sort
append_score = 87
peer_review_scores.append(append_score)
print(f"\n You already appended {append_score} in this array {peer_review_scores} on your Peer Review Scores log.")

# Remove a score if it is less than or equal to 70
for score in peer_review_scores:
    if score <= 70:
        peer_review_scores.remove(score)
        print(f" Removed {score} from your Peer Review Scores log.")
        break

print(f"\nPeer Review Scores log before sort: {peer_review_scores}")
peer_review_scores.sort()
print(f" Sorted Peer Review Scores log: {peer_review_scores}")

# Arrays - Fixed-size Subset
peer_review_array = array.array('i', peer_review_scores[:6])  # First 6 scores
array_sum = sum(peer_review_array)
list_sum = sum(peer_review_scores)

print(f"\nArray Sum (first 6 Peer Review Scores): {array_sum}")
print(f"List Sum (all Peer Review Scores): {list_sum}")

if array_sum == list_sum:
    print("All Peer Review Scores are equal")
else:
    print("All Peer Review Scores are different")

#Dictionaries: Manage Peer Review Records
peer_review_log = [
    {'id': 1, 'name': 'Team Alpha', 'value': 82},
    {'id': 2, 'name': 'Team Beta', 'value': 77},
    {'id': 3, 'name': 'Team Gamma', 'value': 89},
    {'id': 4, 'name': 'Team Delta', 'value': 75}
]

# Update one record
for record in peer_review_log:
    print(f"{record}")
    if record['id'] == 3:
        record['value'] = 95
        print(f"\n Updated Record: {record} \n")

# Delete one record
peer_review_log = [record for record in peer_review_log if record['id'] != 2]

# Compute total value from remaining logs
total_value = sum(record['value'] for record in peer_review_log)
print("Total value of Peer Review Records:", total_value)
