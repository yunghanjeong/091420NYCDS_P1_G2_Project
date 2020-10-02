# Film Industry Analysis for Novel Title Direction for Microsoft Movie Studio
091420NYCDS Phase 1 Group 2 EDA Project

## Overview
This project seeks to identify the success parameters of the recently released film titles for consulting and directing the creation of a novel title for the client: Microsoft Movie Studios.

## Business Problem

![img](https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE2qVsJ?ver=3f74)

<br>
Microsoft sees all the big companies creating original video content, and they want to get in on the fun. They have decided to create a new movie studio, but the problem is they don’t know anything about creating movies. They have hired you to help them better understand the movie industry. Your team is charged with exploring what type of films are currently doing the best at the box office. You must then translate those findings into actionable insights that the head of Microsoft's new movie studio can use to help decide what type of films to create.


## Repository Structure

All data sets can be found in `/data` folder.
All plots and locally saved images can be found in `/images` folder.

## Analysis Focus

1. This analysis focuses on wholistic data available from past decade (2010 and beyond).
2. This analysis focuses on films that have made profit in either domestic and/or worldwide market.

## Analysis

### Profitability and Trends of Film Genres

Overall frequency of the genres according to IMDB was sorted and plotted separated by years. Note the scale on y-axis for comparison of each subplots, the most frequent genres are located on the left with reducing frequency in subsquent plots.

![genre_popular_stack](https://github.com/yunghanjeong/091420NYCDS_P1_G2_Project/blob/master/images/genre_peryear_stacked.png?raw=true)<br>

Most notable trend is that Mystery and Sports are in sharp decline, while Documentary saw an upward trend. Among the mmost pouplar genres Thriller and Crime had slight downard trends, while Action and Adventure showed consistant popularity. Animation and Sci-Fi, although not most popular, also showed consistent popularity.

The gross profit and profit per title of each genre were following:

![genre_profit](https://github.com/yunghanjeong/091420NYCDS_P1_G2_Project/blob/master/images/norm_gross_sbs_profit_genre.png?raw=true)<br>

Action and Adventure scored highest gross profit, but they were also amoing the most popular genres. Sci-Fi and Animation had clear high profit per title compared to other genres. Adventure was also a high performing category. Comedy and Drama performed well in gross profit analysis, but fell in ranks quickly when profit per title was used as a metric. This is most likely due to cultural and ideal differences in humor and drama between the domestic and internatinal market. 

### Profitability and Budget

There was a medium corrleation (~0.6) between the budget and profit with clear cluster around sub $100 million budget and sub $25 million profit. 

![budget_v_profit](https://github.com/yunghanjeong/091420NYCDS_P1_G2_Project/blob/master/images/budget_profit.png?raw=true)<br>

When the data was narrowed within 4 standard deviation from center on the profit (to filter box office "flops" and "bombs") and the correlation was reduced slightly. Also it displayed clear break-off pount in the budget greater than $75 million. 

The data was narrowed further to visualize the profitabilty of films with budgets greater than $75 million. This dataset had lowest correlation between the budget and the profit. However, this dataset also contained all films that made over $1 billion in profit.

In addition, top 5 of highest grossing film were categorize as Action/Adventure/Sci-Fi films. 3 out of top 5 of highest profit/budget ratio films were Animations while other 2 films were Action/Adventure/Sci-Fi films. 

### Profitability of Film Release Date

May, June, July, and December are generally conisidered as the best month to release any film. However, when the two most promising genres; Animation and Sci-Fi, May and June were the best month to release the these films. 

![release_date_profit](https://github.com/yunghanjeong/091420NYCDS_P1_G2_Project/blob/master/images/avg_month_profit.png?raw=true)

## Summary
- Animation films have the highest profit margins.

- May/June is the best month to release an Animation film.

## Top Performing Animation or Sci-Fi films for reference
Despicable Me 2, Ice Age: Continental Drift, The Hunger Games, Jurassic World


## Contributors
[Cierra Andaur](https://github.com/cierra4prez)
<br>
[Yung Han Jeong](https://github.com/yunghanjeong)