# Athens Airbnb Data Analysis

The goal of the project is to analyze my country's Airbnb data set. Also, a simple implementation 
of a recommendation system based on the description of each Airbnb using 
**Term Frequency–Inverse Document Frequency** and **Cosine Similarity** metric.

### Data sets

I downloaded the data sets for my country from [here](http://insideairbnb.com/get-the-data.html). 
You can do the same for your own or for any other country you want to analyze.

There are 3 datasets:

* listings.csv
* calendar.csv
* reviews.csv

The **whole procedure of each notebook** consists of:

1. Loading data sets.
2. Droping any rows that have a nan value

* **word_cloud.ipynb**

3. Merging data sets
4. Text preprocessing
5. Generating Word Clouds

* **recommendation.ipynb**

3. Concatenating name and description columns
4. Text preprocessing
5. TF-IDF vectorization
6. Calculating the similarity of each Airbnb with the others
7. Storing 100 most similar Airbnbs for each one (Linear time)

* **listings.ipynb**

3. Cleaning price column
4. Data analysis

* **calendar.ipynb**

3. Cleaning price column and separating date to year, month and day columns
4. Data analysis

## Word Clouds

<h2 align="center"> Description </h2>

![description](https://user-images.githubusercontent.com/48658768/90988607-c4584700-e59c-11ea-9341-a2c14ad835c2.png)

<h2 align="center"> Last Review </h2>

![last review](https://user-images.githubusercontent.com/48658768/90988608-c5897400-e59c-11ea-8872-8bed9ce63bb3.png)

<h2 align="center"> Neighbourhood </h2>

![neighbourhood](https://user-images.githubusercontent.com/48658768/90988609-c6220a80-e59c-11ea-8ac8-1ca9d7610b2f.png)

<h2 align="center"> Transit </h2>

![transit](https://user-images.githubusercontent.com/48658768/90988610-c6baa100-e59c-11ea-9297-3e42255904df.png)