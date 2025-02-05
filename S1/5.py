def remove_duplicates(input_list):
    return list(set(input_list))


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print("Original list:", sample_list)
    print("List after removing duplicates:", remove_duplicates(sample_list))