"""Lab 08.

Use the split() method to process the following files: gdp.txt and split.txt.
Examine each file and determine how best to separate the various elements to
accomplish the assigned task.

In the first file, each record has three elements:
  * country name,
  * gross domestic product (GDP) in millions of dollars, and
  * total population.
Your job is to calculate the GDP per person for each country and
print out country and GDP/person in descending order of per-capita GDP.
Format the results for a professional look.

In the second file, determine how many words there are in the file and
how many of those words are unique.
Then print out each word in ascending order.
Be sure to change every alphabetic character to one case and
remove/replace all punctuation.
"""

from string import punctuation

# Use the split() method to process the following files: gdp.txt and split.txt.
gdp_fin = open('./Python II Data/gdp.txt', 'r')  # comma separated
split_fin = open('./Python II Data/split.txt', 'r')  # ^M separated

gdp_lst = []
split_str = split_fin.read().lower()


## In the first file
## calculate the GDP per person for each country and
for line in gdp_fin:
    country, gdp, population = line.split(',')
    gdp = float(gdp)*1000000  # orig data in millions
    population = int(population)

    gdp_lst.append([gdp/population, country])


# print out country and GDP/person in descending order of per-capita GDP.
# Format the results for a professional look.
for gdppp, country in reversed(sorted(gdp_lst)):
    print "{0:25s} {1:5,.0f}".format(country, gdppp)


## In the second file
# determine how many words there are in the file and
for x in punctuation:
    if x in split_str:
        split_str = split_str.replace(x, ' ')

split_lst = split_str.split()
print "{} Words in File".format(len(split_lst))

# how many of those words are unique.
split_set = set(split_lst)
print "{} Unique Words in File".format(len(split_set))

# Then print out each word in ascending order.
# Be sure to change every alphabetic character to one case and
# remove/replace all punctuation.
print sorted(split_lst)
