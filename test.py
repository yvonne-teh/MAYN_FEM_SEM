# first, we create a function that turns our class labels, which are string,
# into integers, so we can later use hot end encoding
def get_int_class(long_class: str, allow_other: bool = False) -> int:
    if long_class == 'Component-Whole(e2,e1)' or long_class == 'Component-Whole(e1,e2)':
        return 0
    if long_class == 'Instrument-Agency(e2,e1)' or long_class == 'Instrument-Agency(e1  ,e2)':
        return 1
    if long_class == 'Member-Collection(e1,e2)' or long_class == 'Member-Collection(e2,e1)':
        return 2
    if long_class == 'Cause-Effect(e2,e1)' or long_class == 'Cause-Effect(e1,e2)':
        return 3
    if long_class == 'Entity-Destination(e2,e1)' or long_class == 'Entity-Destination(e1,e2)':
        return 4
    if long_class == 'Content-Container(e2,e1)' or long_class == 'Content-Container(e1,e2)':
        return 5
    if long_class == 'Message-Topic(e2,e1)' or long_class == 'Message-Topic(e1,e2)':
        return 6
    if long_class == 'Product-Producer(e2,e1)' or long_class == 'Product-Producer(e1,e2)':
        return 7
    if long_class == 'Entity-Origin(e2,e1)' or long_class == 'Entity-Origin(e1,e2)':
        return 8
    if long_class == 'Other':
        if allow_other:
          return 9

semeval_tuples = list()
temp_tuple = dict()
with open('TRAIN_FILE.TXT', 'r') as file:
    for index, line in enumerate(file.readlines()):
      # the documents is structured in blocks of 4 lines each so we use % 4
      if index % 4 == 0:
        regex_results = re.search(r"\"(.*)\"", line.strip())
        if regex_results:
          temp_tuple['sentence'] = regex_results.group(1)
      if index % 4 == 1:
        temp_tuple['label'] = get_int_class(line.strip(), allow_other=False)
      if index % 4 == 2:
        semeval_tuples.append(temp_tuple)
        temp_tuple = dict()

df = pd.DataFrame(semeval_tuples)
df = df.dropna()