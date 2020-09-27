#import library
import pandas as pd

#This function search each dataframe by provided column name and looks for a common value provided in a list
def searchbytitle(df1, df1_title_col, df2, df2_title_col, titles: list):
#get a combined(merge) dataframe by a list of titles
#technically you can combine any column if they have the same information   
 
    #initialize return dataframe
    combine_df = pd.DataFrame()
    #for loop to 
    for i, title in enumerate(titles):
        # grab subset by the columns and value specified
        df1_subset = df1[df1[df1_title_col] == title]
        df2_subset = df2[df2[df2_title_col] == title]
        
        #reset the index for join
        df1_subset.set_index(df1_title_col, inplace = True)
        df2_subset.set_index(df2_title_col, inplace = True)
        
        #set combine_df for return
        combine_df = pd.concat([combine_df, df1_subset.join(df2_subset)])
        
    return combine_df

#EXPECTING ["genre1,genre2,genre3", "genre2,genre4", "genre2,genre5"...]
def unpack_genre(genrelist): 
    genre_dict = {} #initialize output
    list_of_genre = [] #initilize unpacked list
    for genres in genrelist: #unpack elements
        for genre in genres.split(","): #split elements by comma
            list_of_genre.append(genre.lower()) #append all strings
    checking_genre = set(list_of_genre) #checking list is the set of above
    for check in checking_genre: #check how many times check
        genre_dict[check] = list_of_genre.count(check) #appears on the list and put it as key:value pair
    genre_dict = {k: v for k, v in sorted(genre_dict.items(), key=lambda item: item[1])} #sort
    
    return genre_dict #return