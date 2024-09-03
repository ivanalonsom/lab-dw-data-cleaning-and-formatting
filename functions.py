import pandas as pd

def ini_dataframe_csv(url):

    df = pd.read_csv(url)
    return df

def change_cols_names(df):

    df.columns = ["Customer", 'ST', 'GENDER', 'Education', 'Customer Lifetime Value', 'Income', 'Monthly Premium Auto', 'Number of Open Complaints', 'Policy Type', 'Vehicle Class', 'Total Claim Amount']

    for x in df.columns:
        df.rename(columns={x: x.lower().replace(" ", "_")}, inplace=True)

    df.rename(columns={'st': 'state'}, inplace=True)

    return df



def fix_gender(x):
    if x == "Male":
        return "M"
    elif x == "Femal":
        return "F"
    elif x == "female":
        return "F"
    else:
        return x


def replace_state(df):
    reemplazos = {"AZ": "Arizona", "Cali": "California", "WA": "Washington"}
    return df["st"].replace(reemplazos)

df["education"] = df["education"].str.replace("Bachelors", "Bachelor")

df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")

replaced_car = {"Sports Car" : "Luxury", "Luxury SUV" : "Luxury", "Luxury Car" : "Luxury"}

df["vehicle_class"] = df["vehicle_class"].replace(replaced_car)












# Your code here

df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(float)

def fix_open_complaints(x):

    if pd.isnull(x) or '/' not in x:
        return x
    elif '/' in x:
        x_splitted = x.split("/")
        return x_splitted[1]


df["number_of_open_complaints"] = df["number_of_open_complaints"].apply(fix_open_complaints)





# Your code here

df.isnull().apply(lambda x: x.value_counts())  

df.dropna(inplace=True)         # If one cell is empty, it drops the row. We lose about 60 rows of a total of 1071 so it´s not a big problem to handle the data this way

df.isnull().apply(lambda x: x.value_counts())  








print(f"Before: {df.duplicated(subset=["state", "income"]).sum()}")
       
df.drop_duplicates(subset=["state", "income"], keep='last', inplace=True)          # By default, it keeps the first occurence

print(f"After: {df.duplicated(subset=["state", "income"]).sum()}")




df.reset_index(drop=True, inplace=True)     # drop True elimina el índice original y se reemplaza con uno nuevo que empieza de 0. Con False (por defecto) crea una nueva col con los índices nuevos

df.to_csv('ex5_file.csv', index=True) 
