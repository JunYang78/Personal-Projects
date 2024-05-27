import secrets

# Function to generate a random secret key
def generate_secret_key():
	return secrets.token_hex(16) # 16 bytes (32 hex characters)

# Function to generate a One Time Password (OTP) using the secret key
def generate_otp(secret_key, length=6):
	# Defining the characters allowed in the OTP
	allowed_characters = "0123456789"

	# Generating a random OTP using the secret key and allowed characters
	otp = ''.join(secrets.choice(allowed_characters) for _ in range(length))
	
	return otp

# Example usage
if __name__ == "__main__":
	# Generate a random secret key (this should be kept secure)
	secret_key = generate_secret_key()
	print(secret_key)

	# Simulate sending the OTP to the user
	otp = generate_otp(secret_key)
	print(otp)

	# Simulating user input for OTP verification
	user_input = input("Please enter the received OTP: ")

	# Verify the OTP entered by the user
	if user_input == otp:
		print("OTP verification successful. Access granted!")
	else:
		print("OTP verification failed. Access denied!")
