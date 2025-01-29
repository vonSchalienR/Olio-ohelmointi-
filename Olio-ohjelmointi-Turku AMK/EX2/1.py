# Let us define the list with names: 
queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

queue.pop(0)

queue.insert(queue.index("Ville") +1, "Anni")
queue.remove("Ville")

queue.remove("Jarno")

queue.append("Marjo")

current_index = queue.index("Antti")
new_index = min(current_index + 2, len(queue)) 
queue.pop(current_index)  
queue.insert(new_index, "Antti")

# Is Jenni in the queue and at what position?
is_jenni_in_queue = "Jenni" in queue
jenni_position = queue.index("Jenni") if is_jenni_in_queue else None

# Who is the third last person?
third_last_person = queue[-3]

# Print the results
print(f"Is Jenni in the queue? {is_jenni_in_queue}")
print(f"Jenni's position: {jenni_position if is_jenni_in_queue else 'N/A'}")
print(f"Third last person in the queue: {third_last_person}")
print(f"queue:{queue}")