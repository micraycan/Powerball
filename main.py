from bs4 import BeautifulSoup
import requests

r = requests.get("http://powerball-megamillions.com/past-results?game_id=MUPB&game=Powerball")
data = r.text

soup = BeautifulSoup(data, "html.parser")

table = soup.find_all('tr')[2:-5]

all_nums = []
all_pb = []

for row in table:
    # just in case date is needed in the future
    # date = row.get_text()[0:16]
    num = row.get_text()[16:31]
    pb = row.get_text()[31:]

    num_list = num.split()
    all_nums.append(num_list)

    all_pb.append(pb)

# create dictionary to count most common numbers
num_counter = {}

for numbers in all_nums:
    for n in numbers:
        if n in num_counter:
            num_counter[n] += 1
        else:
            num_counter[n] = 1

# create another dictionary for powerball numbers
pb_counter = {}

for ball in all_pb:
    for p in ball:
        if p in pb_counter:
            pb_counter[p] += 1
        else:
            pb_counter[p] = 1

# sort the dictionary keys by value in descending order
ordered_num = sorted(num_counter, key = num_counter.__getitem__, reverse = True)
ordered_pb = sorted(all_pb, reverse = True)

# time to spit out those magic numbers (sorted for aesthetics)
print('Most picked white numbers:', sorted(ordered_num[:5]))
print('Most picked powerball:', ordered_pb[0])