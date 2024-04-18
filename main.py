import secrets
import string

def generate_secure_password(length=20, include_uppercase=True, include_digits=True, include_special=True):
    # Define possible character pools
    character_pools = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }

    # Always include lowercase letters for basic security
    chosen_characters = character_pools['lowercase']

    # Optionally include other character types
    if include_uppercase:
        chosen_characters += character_pools['uppercase']
    if include_digits:
        chosen_characters += character_pools['digits']
    if include_special:
        chosen_characters += character_pools['special']

    # Generate a random password using cryptographically secure random generator
    password = ''.join(secrets.choice(chosen_characters) for _ in range(length))

    # Ensure the password meets all criteria
    if include_uppercase:
        password = ensure_character(password, character_pools['uppercase'], length)
    if include_digits:
        password = ensure_character(password, character_pools['digits'], length)
    if include_special:
        password = ensure_character(password, character_pools['special'], length)

    return password

def ensure_character(password, pool, length):
    # Randomly insert at least one character from the pool if not present
    while any(c in pool for c in password) is False:
        position = secrets.randbelow(length)
        password = password[:position] + secrets.choice(pool) + password[position + 1:]
    return password

# Example usage
password = generate_secure_password(length=24, include_uppercase=True, include_digits=True, include_special=True)
print("Generated Password:", password)
