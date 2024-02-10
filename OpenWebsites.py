import webbrowser

# List of social media URLs
socialMedia = ["instagram", "twitter", "reddit", "youtube"]

# Open a new text file in write mode ('w')
with open("Social media address.txt", 'w') as smAddress:
    # The list is joined to be a string as the write only takes strings as a whole
    socialMediaString = "\n".join(socialMedia)
    # Write the string to the file
    smAddress.write(socialMediaString)

# Open each URL in a web browser
for name in socialMedia:
    # Construct the complete URL
    url = "https://www." + name + ".com"
    # Open the URL in the default web browser
    webbrowser.open(url)
    
