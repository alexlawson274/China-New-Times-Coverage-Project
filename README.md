# Is China's economy followed closely enough?
China makes up roughly 17% of the world's economy in 2025. Has Western media's coverage of China kept pace with the country's growth? 

##  Methodology
Using the New York Times Article Search API (see source data below), I counted how many articles mention "China" in a given year. I then compared the amount of coverage China receives in the New York Times to that of other major economies. 

 How the New York Times International Coverage Index is Calculated for 2024

Step 1: Count the mentions for each of the top 20 economies in the world (by GDP)

Step 2: Calculate the average of the top 20 country mentions

Step 3: Divide each country's mention count by the average of the top 20

This gives the New York Times International Coverage Index (1= low coverage, 3= high coverage) 

Why use this index? 

Variability in country mentions: Country mentions fluctuate year-to-year. This may be due in part to the structure of the newspaper (how many articles are in the paper, the length, use of newswires, etc). Using an index, rather than a year-to-year count, means that different years can be compared (for example, 2005 and 2024). 

Simplicity: An index of international coverage is easier for readers to grasp (other methods to show international coverage, for example, % of total country mentions, can be confusing)

Other Notes: Take note of the search term for the country. A country search for the country "Turkey" may return articles about Thanksgiving. 


##  Source Data 
Data comes from the Article Search API.T The Api allows users to look up articles by keyword. You can refine your search using filters.
All instructions are available here: https://developer.nytimes.com/docs/articlesearch-product/1/overview

## Dependencies
Before running the script, the following packages need to be installed:.

- `Datetime`
- `Pandas`
- `requests`

##  Output
The calculations were used as part of an article titled "Is China's Economy Followed Closely Enough?"




