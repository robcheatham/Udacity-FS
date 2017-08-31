# Import Postgre dbapi
import psycopg2

# Database Name and Queries to be passed to Log functions
DBNAME = "news"
query_one = "select title, views from article_views limit 3"
query_two = """select authors.name, sum(article_views.views) as popularity
               from article_views, authors
               where authors.id = article_views.author
               group by authors.name order by popularity desc"""
query_three = "select date, error_rate from error_log where error_rate > 1"


# Function to connect to the database that takes a query as an argument
def db_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    output = c.fetchall()
    db.close()
    return output


# Main function that is called when the program runs to print the Logs
def main():
    # Query One to log top three articles
    print("\n" + "Top Three Articles of All Time")
    log_one = db_query(query_one)
    for i in log_one:
        print('"' + i[0] + '" -- ' + str(i[1]) + ' views')

    # Query Two to log most popular authors
    print("\n" + "Most Popular Authors of All Time")
    log_two = db_query(query_two)
    for i in log_two:
        print(i[0] + " -- " + str(i[1]) + " views")

    # Query Three to log days with errors over 1 percent
    print("\n" + "Days with over 1% of Errors on Requests")
    log_three = db_query(query_three)
    for i in log_three:
        print(str(i[0]) + " -- " + str(i[1]) + "% errors")
    print("\n")

if __name__ == "__main__":
    main()
