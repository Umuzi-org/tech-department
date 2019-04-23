import pandas as pd

####### read in multiple files and Concatenate #######
#get list of all csv files in folder
csv_files = glob.glob('*.csv')

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

######### explore data #############
df.info()
df.describe()
df.value_counts(dropna = FALSE)
df.columns
df.shape
df.isnull().sum()


##### use assert to check data ##############

####### concat and merge ###################

# Concatenate column-wise (for row-wise axis = 0)
ebola_tidy = pd.concat([ebola_melt, status_country], axis = 1)

#change variable type
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors= 'coerce')
tips['sex'] = tips['sex'].astype("category")

######### reshape ###########################
#melt
airquality_melt = pd.melt(airquality, id_vars = [‘Month’, ‘Day’], var_name = ‘measurement’, value_name = ‘reading’)
#optional: specify value_vars = [] to only melt certain variables

# Pivot airquality_melt: airquality_pivot
airquality_pivot = pd.pivot_table(airquality_melt, index=['Month', 'Day'], columns= 'measurement', values= 'reading')

# Pivot airquality_dup: airquality_pivot
airquality_pivot = pd.pivot_table(airquality_dup, index=['Month', 'Day'], columns= 'measurement', values= 'reading', aggfunc= np.mean)

############# splitting columns #############################

#to split/splice columns with multiple pieces of info in one:
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

# Create the 'gender' column by extracting first character in string in column ‘variable’
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column by extracting the rest of the characters of the string in column ‘variable’
tb_melt['age_group'] = tb_melt.variable.str[1:]

#split at delimiter
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name= 'type_country', value_name= 'counts')

# Create the 'str_split' column by splitting at underscore
ebola_melt['str_split'] = ebola_melt.type_country.str .split('_')

# Create the 'type' column, at index 0 in str_split column
ebola_melt['type'] = ebola_melt.str_split.str .get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str .get(1)

### regular expressions ###############
import re
#re.findall (string, pattern)
#pattern.match(string)

###slicing ######

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:"Obama"]

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,"Obama":"winner"]

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,"Romney":]

# filtering ######################################
#create filter for low margin
too_close = election.margin < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.winner[too_close] = np.nan

# Drop rows in df with how='any' and print the shape
print(df.dropna(how = "any").shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how = "all").shape)

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())
