#import library
import pandas as pd

#This function search each dataframe by provided column name and looks for a common value provided in a list
#If the associated year matches then the dataframes are joined and concatednated
def searchbytitle(df1, df1_title_col, df2, df2_title_col, titles: list):
#this is redudant. Just pass the list with df[df[column].isin(list)]
    pass

#EXPECTING ["genre1,genre2,genre3", "genre2,genre4", "genre2,genre5"...]
def unpack_genre(genrelist): 
    genre_dict = {} #initialize output
    list_of_genre = [] #initilize unpacked list
    for genres in genrelist: #unpack elements: genres is "genre1,genre2,genre3,..."
        for genre in genres.split(","): #split elements by comma: genre is "grenre1" while split method provide ["genre1", "gnenre2", "genre3"]
            list_of_genre.append(genre.lower()) #append each genre as an element to list_of_genres
    checking_genre = set(list_of_genre) #checking list is a unique set of list_of_genre
    for check in checking_genre: #for a unique gerne in unique set of genres
        genre_dict[check] = list_of_genre.count(check) #get how many times the genre appear on the list_of_genres
    genre_dict = {k: v for k, v in sorted(genre_dict.items(), key=lambda item: item[1])} #sort and output key value pair of genre:# of appearance
    
    return genre_dict #output dictionary of genre counts

#Count how many common items are in each list
def common_in_list(list1: list, list2: list):
    counter1 = counter2 = 0
    for item in list1:
        if item in list2:
            counter1 += 1
    return counter1

#return common elements between 2 lists. uses 1st argument as the iterator and 2nd argument as the comparator 
def common_titles(title_list1: list, title_list2: list):
    return [title for title in title_list1 if title in title_list2]

#this function updates the strings value dollar sign to numbers.
#Expected input: $425,112,413
#Output: 425112413 
def dollar_str_to_num(num_str: str):
    return int("".join(digit for digit in num_str if digit.isnumeric()))

#get the date_string and check the first string for month
def get_month(date_string):
    month = date_string.split()[0]
    
    if month == "Jan":
        num_month = 1
    elif month == "Feb":
        num_month = 2
    elif month == "Mar":
        num_month = 3
    elif month == "Apr":
        num_month = 4
    elif month == "May":
        num_month = 5
    elif month == "Jun":
        num_month = 6
    elif month == "Jul":
        num_month = 7
    elif month == "Aug":
        num_month = 8
    elif month == "Sep":
        num_month = 9
    elif month == "Oct":
        num_month = 10
    elif month == "Nov":
        num_month = 11
    else:
        num_month = 12
    
    return num_month

#assign season values depending on month
def get_season(month_num):
    if month_num in [12,1,2]:
        return "Winter"
    elif month_num in [3,4,5]:
        return "Spring"
    elif month_num in [6,7,8]:
        return "Summer"
    else:
        return "Fall"