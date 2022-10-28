import random

# time signature
top = random.randrange(2, 5)
print(f"top: {top}")

bottom_list = [4, 8, 16]
bottom = random.choice(bottom_list)
print(f"bottom: {bottom}")

# tempo
print(f"speed: {random.randrange(70, 150)}")

# chords
chords_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

chord_progression = []
for i in range(4):
  chord_progression.append(random.choice(chords_list))

print(chord_progression)
