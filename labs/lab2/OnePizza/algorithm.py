def parse_input(test_file_name):
    with open(test_file_name, 'r') as file:
        input = file.read()
    input = input.split("\n")
    total_clients = int(input[0])
    client_likes = []
    client_dislikes = []
    for i in range(1, total_clients + 1, 2):
        parse_client_data([input[i], input[i + 1]])


def parse_client_data(client_data: [str]):
    liked = client_data[0].strip().split(" ")
    disliked = client_data[1].strip().split(" ")
