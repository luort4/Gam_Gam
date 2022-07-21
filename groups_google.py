import pandas as pd
import os
import sys

def user2group(df_users, df_groups):
    # head = headers
    # ind = indexes for rows
    # col = is the entire row, use head with col to extract that information

    # Since we are using iterrows it pulls the information like it was a small
    # dataframe. that is why using the 'Users' header works here and doesn't
    # require an index.
    global which_gam
    which_gam = '[ENTER LOCATION OF GAM BINARY]' # type "which gam" and place that location in here
    stax_alias = strip_stax(df_users)
    for head in df_users:
        for ind, col in df_users.iterrows():
            user = col['Users']
            if col[head] == 'x':
                for x, v in enumerate(df_groups['email']):
                    if df_groups['name'][x] == head:
                        if sys.argv[-1] == "execute" or sys.argv[-1] == "exec":
                            os.system(f'{which_gam} update group {v} add member {user}')
                        else:
                            print(f'{which_gam} update group {v} add member {user}')
                        #print(f'{which_gam} update alias {stax_alias[ind]} user {user}')
                        #os.system(f'{which_gam} group {v} print users fields name')
            else:
                continue
    set_alias(df_users, stax_alias)

def strip_stax(df_users):
    # update the Email Alias of the user
    stax_alias = []
    for i in df_users['Users']:
        first_last = i.split("@")
        stax_alias.append(first_last[0] + "@staxpayments.com")
    return stax_alias

def update_phone(df_phone):
    # update gam with phone numbers if applicable
    for i, j in enumerate(df_phone['Users']):
        if sys.argv[-1] == "execute" or sys.argv[-1] == "exec":
            os.system(f"{which_gam} update user {j} phone type work value {df_phone['PhoneNumber'][i]} primary")
        else:
            print(f"{which_gam} update user {j} phone type work value {df_phone['PhoneNumber'][i]} primary")

def set_alias(df_users, stax_alias):
    # set the stax alias
    for ix, jx in enumerate(df_users['Users']):
        if sys.argv[-1] == "execute" or sys.argv[-1] =="exec":
            os.system(f'{which_gam} update alias {stax_alias[ix]} user {jx}')
        else:
            print(f'{which_gam} update alias {stax_alias[ix]} user {jx}')

def main():
    # set the dataframe. this time using two sheets, one for users and the
    # other for groups.
    goo = pd.ExcelFile('db/goo_groups.xlsx')
    df_users = pd.read_excel(goo, 'Users')
    df_groups = pd.read_excel(goo, 'Groups')
    df_phone = pd.read_excel(goo, 'Phone')
    user2group(df_users, df_groups)
    update_phone(df_phone)

main()
