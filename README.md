# Simple_Friend_Recommendation_Program

This code implements a friend recommendation system for a social network. It allows users to input a social network graph and provides recommendations for new friends based on common connections.

## How it Works

1. The program prompts the user to enter a filename for the social network graph file. It keeps asking until a valid filename is provided.

2. The `create_network()` function reads the input file and constructs a dictionary representing the social network. Each key in the dictionary represents a user, and the corresponding value is a list of that user's friends.

3. The `calc_similarity_scores()` function calculates a similarity matrix for all users in the network. The similarity between two users is determined by the number of common friends they have.

4. The main loop of the program allows the user to enter a member ID within the valid range of the network. The `recommend()` function suggests a friend for the given member based on the similarity matrix and the member's existing friends. The suggestion is a user who is not already a friend, has a higher number of common friends, and is not the member themself.

5. The program displays the suggested friend ID to the user and asks if they want to continue. If the user enters 'y' or 'Y', the loop repeats for another member.

## Usage

1. Run the script.

2. Enter the filename of the social network graph file when prompted. The file should follow the specified format:
```
<number_of_users>
<friend_a> <friend_b>
<friend_c> <friend_d>
...
```

- `<number_of_users>`: An integer representing the total number of users in the network.
- `<friend_a> <friend_b>`: Pairs of integers representing connections between users. Each pair denotes that `friend_a` and `friend_b` are friends.

3. After providing the filename, the program will ask for a member ID to get friend recommendations for. Enter an integer between 0 and `number_of_users - 1`.

4. The program will display the suggested friend ID for the member. It will then ask if you want to continue recommending friends for other members. Enter 'y' or 'Y' to continue or any other key to exit the program.
