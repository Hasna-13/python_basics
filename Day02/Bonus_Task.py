q1 = input("1) What work style do you prefer?\n(a) Creative and open-ended\n(b) Problem-solving and analytical\n(c) Helping and guiding others\nYour choice: ").lower()

q2 = input("\n2) What work environment do you see yourself in?\n(a) Flexible, with space for innovation\n(b) Fast-paced, tech-driven\n(c) Community-focused or people-oriented\nYour choice: ").lower()

q3 = input("\n3) What's your main career goal?\n(a) Express creativity and originality\n(b) Build or improve systems/technology\n(c) Make a positive social impact\nYour choice: ").lower()

if q1 == 'a' and q2 == 'a' and q3 == 'a':
    career = "Designer."
elif q1 == 'b' and q2 == 'b' and q3 == 'b':
    career = "Software Engineer."
elif q1 == 'c' and q2 == 'c' and q3 == 'c':
    career = "Teacher ."
else:
    career = "You have strengths in multiple areas."

print("\nSuggested Career Path:", career)
