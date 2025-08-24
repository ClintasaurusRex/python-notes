def convert_to_uppercase(strings):
    # Use map() with a lambda function to convert strings to uppercase
    uppercase_strings = map(lambda i: i.upper(), strings)
    
    # Return the list of uppercase strings
    return list(uppercase_strings)

print(convert_to_uppercase(["hello", "world", "python"]))

def calculate_lengths(words):
    # Use map() with a lambda function to calculate the length of each word
    word_lengths = map(lambda i: len(i), words)
    
    # Return the list of word lengths
    return list(word_lengths)
print(calculate_lengths(["apple","banana","cherry","date","fig"]))
print("------------------------------------------------------------------------------------------------------------------------------")

def get_long_strings(strings):
    # Use filter() with a lambda function to select strings with length greater than 5
    long_strings = filter(lambda i: len(i)) > 5, strings
    
    # Return the list of selected strings
    return list(long_strings)
# print(get_long_strings(['apple', 'banana', 'cherry', 'dragonfruit']))
print("------------------------------------------------------------------------------------------------------------------------------")

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
   

def get_prime_numbers(numbers):
  prime_nums = filter(lambda i: is_prime(i), numbers)
  return list(prime_nums)

print(get_prime_numbers([2,3,4,5,10,11,13,17,18,19]))

print("------------------------------------------------------------------------------------------------------------------------------")
email_list = ['Test@EXAMPLE.com',  'invalid.email',  'user@domain@.com',   'space@email.com'  ,  'valid@domain.com']
def clean_email_list(emails):
    # Convert emails to lowercase and strip whitespace
    standardized_emails = map(lambda email: email.strip().lower(), emails)
    
    # Filter valid emails
    valid_emails = filter(
        lambda email: email.count("@") == 1 and email.split("@")[0] and email.split("@")[1],
        standardized_emails
    )
    
    # Return the list of valid emails
    return list(valid_emails)

print(clean_email_list(email_list)) 

print("------------------------------------------------------------------------------------------------------------------------------")
pro_nums = [-4, 0, 5, 2, 8, -3, 7]
def process_numbers(numbers):
  no_negs = filter(lambda nums: nums > 0, numbers)
  processed_numbers = map(lambda nums: nums * 2 if nums % 2 == 0 else nums * 3, no_negs)
  
  return list(processed_numbers)

print(process_numbers(pro_nums))

print("------------------------------------------------------------------------------------------------------------------------------")
contacts = [{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]

def organize_contacts(contact_list):
    def is_valid_email(email):
        return '@' in email and '.' in email and " " not in email
    
    def clean_phone(phone):
        digits = ''.join(filter(str.isdigit, phone))
        return digits if len(digits) == 10 else None
    
    def clean_contact(contact):
        return {
            'name': contact['name'],
            'email': contact['email'].lower(),
            'phone': clean_phone(contact['phone'])
        }

    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()
    
    for contact in contact_list:
        cleaned = clean_contact(contact)
        if not is_valid_email(cleaned['email']) or cleaned['phone'] is None:
            continue
        if cleaned['email'] in seen_emails or cleaned['phone'] in seen_phones:
            continue
        seen_emails.add(cleaned['email'])
        seen_phones.add(cleaned['phone'])
        cleaned_contacts.append(cleaned)
    
    return cleaned_contacts

# Example usage
contacts = [
    {"name": "Test User", "email": "test@test.com", "phone": "1234567890"},
    {"name": "Test User 2", "email": "TEST@TEST.COM", "phone": "1234567890"},
    {"name": "Test User 3", "email": "test@test.com", "phone": "9876543210"}
]

cleaned_contacts = organize_contacts(contacts)
print(cleaned_contacts)
print("------------------------------------------------------------------------------------------------------------------------------")

some_text = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"

def analyze_text(text):
    sorted_lists = {}
    occurrences_of_each_word = {}
    palindromes = set()  
    
    punctuation = ".,!?;:'\"()[]{}<>-/\\|@#$%^&*_+=~`"
    cleaned = text.lower()
    for char in punctuation:
        cleaned = cleaned.replace(char, "")
    
    cleaned = cleaned.split()
    
    unique_words = set(cleaned)
    total_unique_words = len(unique_words)
    sorted_lists['unique_count'] = total_unique_words
    
    # Count occurrences of each word
    for word in cleaned:
        if word in occurrences_of_each_word:
            occurrences_of_each_word[word] += 1
        else: 
            occurrences_of_each_word[word] = 1
    
    repeated_words = [word for word, count in occurrences_of_each_word.items() if count > 1]
    sorted_lists['repeated_words'] = sorted(repeated_words)  # Sort alphabetically

    # Check for palindromes in the cleaned words
    for word in unique_words:  # Use unique words to avoid duplicates
        if word == word[::-1]:  # Remove len(word) > 1 to include single-character words
            palindromes.add(word)
    
    sorted_lists['palindromes'] = sorted(palindromes)  # Sort alphabetically
    
    return sorted_lists

# Example Input
some_text = "Madam saw a racecar. Dad said hello hello to mom."

# Example Output
print(analyze_text(some_text))
print("------------------------------------------------------------------------------------------------------------------------------")

data = [
    {"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}
    ]

def transform_dataset(data):
    # Your solution here
    avg_grade = []
    
    # Step 1: Calculate average grade for each student and filter qualified students

    for student in data:
        avg = round(sum(student['grades']) / len(student['grades']), 2)
        avg_grade.append(avg)
        
    # (students with all grades above 70)
    def above_70(data):
        return filter(lambda student: all(grade > 70 for grade in student['grades']), data)
    
    
    
    # Step 2: Create a summary of subjects taken by qualified students
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary
    
print(transform_dataset(data))