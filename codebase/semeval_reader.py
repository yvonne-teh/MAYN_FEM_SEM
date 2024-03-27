def parse_file_to_list(filename):
    entries = []
    entry = {}
    count = 0

    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:
            line = line.strip()

            if count % 4 == 0:  # satz
                entry['sentence'] = line
                # entry['sentence'] = line[6:-1]
            if count % 4 == 1:  # semantische relation
                entry['sem_rel'] = line
            if count % 4 == 2:  # kommentar
                entry['comment'] = line[8:-1]
            if count % 4 == 3:  # leerzeile
                if entry['sem_rel'] == 'Entity-Destination(e1,e2)' or entry['sem_rel'] == 'Entity-Destination(e2,e1)':
                    entries.append(entry)
                entry = {}

            count += 1

    return entries


# Example usage (assuming the content is in 'input_file.txt'):
entries = parse_file_to_list('semeval/training/TRAIN_FILE.TXT')
