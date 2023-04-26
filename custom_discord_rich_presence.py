import time  # Import the time module to work with time-related functions
from pypresence import Presence  # Import the Presence class from the pypresence module

client_id = ''  # Add your client_id here
RPC = Presence(client_id)  # Create an instance of the Presence class with your client_id
RPC.connect()  # Connect to Discord with the given client_id

start_time = time.time()  # Get the current time in seconds since the epoch
duration_seconds = float('inf')  # Set the duration_seconds to infinity

while True:  # Create an infinite loop
    end_time = start_time + duration_seconds  # Calculate the end_time by adding duration_seconds to start_time
    # Update the Discord Rich Presence status with the given details, state, and large_image
    RPC.update(details="add_detail", state="what_your_state", large_image="your_large_image_key_here", start=start_time)
    time.sleep(1)  # Wait for 1 second before updating the status again
