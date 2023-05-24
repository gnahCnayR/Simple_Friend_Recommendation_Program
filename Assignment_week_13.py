# NAME: Ryan Chang # ID: 1765407533
# DATE: 2023-04-10
# DESCRIPTION: <>
from typing import IO, List, Dict


def open_file() -> IO:
    """
    Returns a filepointer to the designated file and keeps asking until filename is valid.
    """
    filepointer = None
    # Continuously checks if the file was a valid one, otherwise output the error message.
    while filepointer is None:
        file = input("Enter a filename: ")
        try:
            filepointer = open(file, "r")
        except IOError:
            print("Error in filename.")

    return filepointer


def create_network(fp: IO) -> Dict[int, List[int]]:
    """
    Returns a dictionary with the key being the user and the values being the user's friends.
    """
    size = int(fp.readline())
    network = {}

    # Initialize the network dictionary with keys for each user and empty lists
    for i in range(size):
        network[i] = []

    # Read in each line from the inputted file which are pairs of connections and add them to the network
    for line in fp:
        friend_a, friend_b = map(int, line.strip().split())
        network[friend_a].append(friend_b)
        network[friend_b].append(friend_a)

    return network


def init_matrix(size: int) -> List[List[int]]:
    """
    Initializes and returns a matrix of size all initialized to 0.
    """
    # Initialize a matrix of size n
    matrix = []
    for i in range(size):
        # Set all values to 0
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)
    return matrix


def common_degree(list1: List, list2: List) -> int:
    """
    Returns an int of the number of common items between two lists.
    """
    count = 0

    # Iterate over both lists and check for similarities, increment if they are similar
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1
    return count


def calc_similarity_scores(network: Dict[int, List[int]]) -> List[List[int]]:
    """
    Returns an n x n similarity matrix for all the users in the network
    """

    # Initialize a matrix of to the len of the network dictionary
    similarity_matrix = init_matrix(len(network))
    for i in range(len(network)):
        for j in range(len(network)):
            # Find the number of common degrees between the two users and set the value of similarity matrix to that
            comde = common_degree(network[i], network[j])
            similarity_matrix[i][j] = comde
    return similarity_matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    """
    Returns the index of the recommended friend, which is not themself, not already in the friend list,
    and has a higher number of matches that the previous person.
    """
    recommend_id = -1
    recommend_value = -1

    # Loops through the similarity matrix
    for i in range(len(similarity_list)):
        # Only change values if the user is not already a friend, not themselves, and has more mutual friends with each
        # other than the last.
        if i not in friend_list and i != member_id and similarity_list[i] > recommend_value:
            recommend_id = i
            recommend_value = similarity_list[i]
    return recommend_id


def main():
    print("Facebook friend recommendation.")
    # Generate the social network and similarity matrix
    network = create_network(open_file())
    similarity_matrix = calc_similarity_scores(network)

    # Go the n - 1 since dictionaries, and most other data structures are zero-based indexing.
    n = len(network) - 1
    response = "Y"
    while response.upper() == "Y":
        member_id = input(f"Enter an integer in the range 0 to {n}: ")
        if not member_id.isdigit() or not (0 <= int(member_id) <= n):
            print(f"Error: input must be an int between 0 and {n}")
        else:
            member_id = int(member_id)
            suggested_friend_id = recommend(member_id, network[member_id], similarity_matrix[member_id])
            print(f"The suggested friend for {member_id} is {suggested_friend_id}")
            response = input("Do you want to continue (enter y for yes)?").strip().lower()


if __name__ == "__main__":
    main()
