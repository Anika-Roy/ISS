import re
import csv
import sqlite3

stack_connection = sqlite3.connect("Record.db")
stack_cursor = stack_connection.cursor()
# stack_cursor.execute("DROP TABLE Ticker") 
# (use when running multiple times)
stack_cursor.execute('''CREATE TABLE Ticker(
                    Date varchar(20),
                    `Company Name` varchar(50),
                    Industry varchar(40),
                    `Previous Day Price` varchar(40),
                    `Current Price` float,
                    `Change in Price` float,
                    Confidance varchar(20),
                    PRIMARY KEY(Date,`Company Name`));''')
# putting the tag conditions in multiple lists for easy access
low_ind = []
med_ind = []
high_ind = []
control = open('Control/control-table.csv', 'r')
row = csv.reader(control)
header = next(row)
for line in row:
    tag = line[2].strip("'")
    if(tag == "Low"):
        low = float(line[1].strip("' &><=%"))
        low_ind.append(low)
    elif(tag == "Medium"):
        [lower, upper] = re.split('&', line[1])
        up = float(upper.strip(" ><=%"))
        low = float(lower.strip(" ><=%"))
        med_ind.append([low, up])
    elif(tag == "High"):
        high = float(line[1].strip("' &><=%"))
        high_ind.append(high)

""" this function returns a string "tag" according to the change in
    price and industry criteria"""


def get_tag(industry, change_in_price):
    Tag = ""
    if(industry == "Finance - General"):
        if(change_in_price < med_ind[0][0]):
            Tag = "Low"
        elif(change_in_price > med_ind[0][1]):
            Tag = "High"
        else:
            Tag = "Medium"

    elif(industry == "Auto Ancillaries"):
        if(change_in_price < med_ind[1][0]):
            Tag = "Low"
        elif(change_in_price > med_ind[1][1]):
            Tag = "High"
        else:
            Tag = "Medium"
    else:
        if(change_in_price < med_ind[2][0]):
            Tag = "Low"
        elif(change_in_price > med_ind[2][1]):
            Tag = "High"
        else:
            Tag = "Medium"
    return Tag


# file for 20 may
path = 'Record/2021113008-20-05-2022.csv'
file1 = open(path, 'r')
row = csv.reader(file1)
header = next(row)
for line in row:
    company_name = line[0].strip("'")  # removes the starting & ending quotes
    industry = line[1].strip("'")
    last_price = line[2].strip("'")
    stack_cursor.execute(
        f'''INSERT INTO Ticker VALUES('20-May-2022','{company_name}','{industry}',
            'NA','{last_price}','NA','listed new')''')
    stack_connection.commit()


# files from now will have the same structure just different days
path = 'Record/2021113008-21-05-2022.csv'
file2 = open(path, 'r')
row = csv.reader(file2)
header = next(row)
for line in row:
    company_name = line[0].strip("'")
    industry = line[1].strip("'")
    last_price = line[2].strip("'")
    stack_cursor.execute(
        f'''SELECT `Current Price` from Ticker 
            where `Company Name`='{company_name}' and Date="20-May-2022"''')
    prev_day_price = stack_cursor.fetchall()[0][0]  # getting the price for the previous day
    change_in_price = round(             # calculating percentage change and rounding it off
        ((float(last_price) - float(prev_day_price)) / float(prev_day_price)) * 100, 5)
    Tag = get_tag(industry, change_in_price)

    stack_cursor.execute(
        f'''INSERT INTO Ticker VALUES('21-May-2022','{company_name}','{industry}',
            '{prev_day_price}','{last_price}','{change_in_price}','{Tag}')''')
    stack_connection.commit()

file1.close()


path = 'Record/2021113008-22-05-2022.csv'
file3 = open(path, 'r')
row = csv.reader(file3)
header = next(row)
for line in row:
    company_name = line[0].strip("'")
    industry = line[1].strip("'")
    last_price = line[2].strip("'")
    stack_cursor.execute(
        f"SELECT `Current Price` from Ticker where `Company Name`='{company_name}' and Date='21-May-2022'")
    prev_day_price = stack_cursor.fetchall()[0][0]
    change_in_price = round(
        ((float(last_price) - float(prev_day_price)) / float(prev_day_price)) * 100, 5)
    Tag = get_tag(industry, change_in_price)

    stack_cursor.execute(
        f'''INSERT INTO Ticker VALUES('22-May-2022','{company_name}','{industry}',
            '{prev_day_price}','{last_price}','{change_in_price}','{Tag}')''')
    stack_connection.commit()


file2.close()

path = 'Record/2021113008-23-05-2022.csv'
file4 = open(path, 'r')
row = csv.reader(file4)
header = next(row)
for line in row:
    company_name = line[0].strip("'")
    industry = line[1].strip("'")
    last_price = line[2].strip("'")
    stack_cursor.execute(
        f"SELECT `Current Price` from Ticker where `Company Name`='{company_name}' and Date='22-May-2022'")
    prev_day_price = stack_cursor.fetchall()[0][0]
    change_in_price = round(
        ((float(last_price) - float(prev_day_price)) / float(prev_day_price)) * 100, 5)
    Tag = get_tag(industry, change_in_price)

    stack_cursor.execute(
        f'''INSERT INTO Ticker VALUES('23-May-2022','{company_name}','{industry}',
            '{prev_day_price}','{last_price}','{change_in_price}','{Tag}')''')
    stack_connection.commit()

path = 'Record/2021113008-24-05-2022.csv'
file5 = open(path, 'r')
row = csv.reader(file5)
header = next(row)
for line in row:
    company_name = line[0].strip("'")
    industry = line[1].strip("'")
    last_price = line[2].strip("'")
    stack_cursor.execute(
        f"SELECT `Current Price` from Ticker where `Company Name`='{company_name}' and Date='23-May-2022'")
    prev_day_price = stack_cursor.fetchall()[0][0]
    change_in_price = round(
        ((float(last_price) - float(prev_day_price)) / float(prev_day_price)) * 100, 5)
    Tag = get_tag(industry, change_in_price)

    stack_cursor.execute(
        f'''INSERT INTO Ticker VALUES('24-May-2022','{company_name}','{industry}',
            '{prev_day_price}','{last_price}','{change_in_price}','{Tag}')''')
    stack_connection.commit()

file4.close()
file5.close()

# METRIC TABLE
# stack_cursor.execute("DROP TABLE Metrics")
# (use when running multiple times)
stack_cursor.execute('''CREATE TABLE Metrics(
                        KPIs varchar(40),
                        Metrics varchar(40));''')
# counting the number of highs per industry
fin_count = 0       # FINANCE - GENERAL
stack_cursor.execute(
    f"SELECT Confidance from Ticker WHERE `Industry`='Finance - General';")
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'High'):
        fin_count += 1
auto_count = 0      # AUTO-ANCILLARIES
stack_cursor.execute(
    f'SELECT Confidance from Ticker WHERE `Industry`="Auto Ancillaries";')
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'High'):
        auto_count += 1
cer_count = 0       # CERAMICS AND GRANITE
stack_cursor.execute(
    f'SELECT Confidance from Ticker WHERE `Industry`="Ceramics & Granite";')
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'High'):
        cer_count += 1
# comparing the frequency of highs per industry to find the best listed industry
if(fin_count > auto_count and fin_count > cer_count):
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Best listed Industry','Finance - General');")

elif(auto_count > fin_count and auto_count > cer_count):
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Best listed Industry','Auto Ancillaries');")

else:
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Best listed Industry','Ceramics & Granite');")
stack_connection.commit()

# counting the number of lows per industry to find the worst listed industry
fin_count = 0
stack_cursor.execute(
    f"SELECT Confidance from Ticker WHERE `Industry`='Finance - General';")
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'Low'):
        fin_count += 1

auto_count = 0
stack_cursor.execute(
    f'SELECT Confidance from Ticker WHERE `Industry`="Auto Ancillaries";')
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'Low'):
        auto_count += 1

cer_count = 0
stack_cursor.execute(
    f'SELECT Confidance from Ticker WHERE `Industry`="Ceramics & Granite";')
list = stack_cursor.fetchall()
for tupple in list:
    if(tupple[0] == 'Low'):
        cer_count += 1


# calculating gain%
stack_cursor.execute(
    f'SELECT `Company Name`,`Current Price` from Ticker WHERE Date="24-May-2022";')
list = stack_cursor.fetchall()
# creating a dictionary that would store company name as key and a list with prices on 2 dates
gain_percent = {}
for i in list:
    gain_percent[i[0]] = [i[1], 0]   # initialising price for 20 may as 0 for now

stack_cursor.execute(
    f'SELECT `Company Name`,`Current Price` from Ticker WHERE Date="20-May-2022";')
list = stack_cursor.fetchall()
for i in list:
    gain_percent[i[0]][1] = i[1]    # putting the correct value for company in the list

gain_array = []  # stores lists containing change %,exact change in INR,Company name

for i in gain_percent:
    company_name = i
    price_24 = gain_percent[i][0]
    price_20 = gain_percent[i][1]
    gain = round((price_24 - price_20) * 100 / price_20, 5)
    gain_array.append([gain, price_24 - price_20, i])
companies_tie = []   # contains names of companies with the max gain% and max increment value
companies_tie_loss = []  # contains names of companies with the max loss% and max decrement value
max_values = [max(gain_array)[0], max(gain_array)[1]]
min_values = [min(gain_array)[0], min(gain_array)[1]]
for i in gain_array:
    if(i[0] == max_values[0] and i[1] == max_values[1]):
        companies_tie.append(i[2])
    elif(i[0] == min_values[0] and i[1] == min_values[1]):
        companies_tie_loss.append(i[2])

# sorting list of company names in lexicographic order
companies_tie.sort()
companies_tie_loss.sort()
stack_cursor.execute(
    f"INSERT INTO Metrics VALUES('Best listed Company','{companies_tie[0]}');")
stack_cursor.execute(
    f"INSERT INTO Metrics VALUES('Gain%','{max_values[0]}');")

# comparing the number of lows per industry to find the worst performing industry
if(fin_count > auto_count and fin_count > cer_count):
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Worst listed Industry','Finance - General');")

elif(auto_count > fin_count and auto_count > cer_count):
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Worst listed Industry','Auto Ancillaries');")

else:
    stack_cursor.execute(
        f"INSERT INTO Metrics VALUES('Worst listed Industry','Ceramics & Granite');")
stack_connection.commit()
# inserting the worst company and its loss percent into table metrics
stack_cursor.execute(
    f"INSERT INTO Metrics VALUES('Worst listed Company','{companies_tie_loss[-1]}');")
stack_cursor.execute(
    f"INSERT INTO Metrics VALUES('Loss%','{-1*min_values[0]}');")
stack_connection.commit()

stack_connection.close()
