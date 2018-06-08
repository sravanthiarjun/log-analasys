# log-analasys
firstly to create a views after that we can implement the python code 
i will create 3 views in that first one is 
*create view common_view as select title,author,count(title)as views from articles,log where log.path like concat('%',articles.slug)group by articles.title,articles.author order by views desc;
*create view single_views as select name,count(articles.author)as views from articles, log where log.path like concat('%',articles.slug)and articles.author=author.id group by authors.name order by views desc;
in that way i have create after that i will written python code in that python code i declare 3 functions and in that functuions we have to implement the code like print statement and for loop and finally call the 3 functions.
finally check my code through the python filenem.py
it will be execute properly 
and i login my accont and then upload my files 
and it will be check into pep8online it will be most proparly run this code it will be execute.
