import onadata as ona

ona.list_sets()

email_edgelist =  ona.email_edgelist()
email_vertices = ona.email_vertices()

# URL of the CSV file
url = 'https://ona-book.org/daya/email_edgelist.csv'

# Read the CSV file from the URL
df = pd.read_csv(url)

print(email_edgelist.info())