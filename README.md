# **Data Extraction Task**
# **Task Description**
The objective of this task is to efficiently extract various types of data from messy API responses using regular expressions. We have identified specific patterns that can be used to match and extract the following data types:

**Restaurant Data:** Extract restaurant names and cuisines in the format "Name - Cuisine."

**Ingredient Lists:** Extract comma-separated ingredient lists like "ingredient1, ingredient2, ingredient3."

**RGB Colors:** Extract RGB colors in the format "rgb(255, 255, 255)" with three numeric values.

**Social Media Usernames:** Extract usernames in the format "@username," where the username can consist of letters and numbers.

**Product Codes:** Extract product codes in the format "ABC123," where A, B, and C are letters, and 1, 2, and 3 are digits.

**News Headlines:** Extract news headlines in the pattern "Headline: Subheader," where both parts are arbitrary strings.

**Event Dates/Times:** Extract event dates and times following the pattern "MMM DD, YYYY - hh:mm AM/PM" with standard date and 12-hour time formatting.

**Email Addresses:** Extract email addresses in the common format "name@domain.com."

## **Implementation**
To accomplish this task, a Python package has been created containing the necessary scripts to extract data based on the specified patterns. Users can import and utilize these functions as needed for their data extraction requirements.

Additionally, a user-friendly command-line interface (CLI) program has been developed to streamline the data extraction process. Users can run the scripts from the command line, providing the file containing the raw API response data as a command-line argument. The program will then prompt the user to select the specific type of data they want to extract and guide them through the extraction process.

This approach ensures that data extraction is efficient, customizable, and user-friendly.

## **Getting Started**
Clone this repository to your local machine.

Install the necessary dependencies if any (specified in the package documentation).

Use the provided scripts or the CLI program to extract data from your raw API responses.

## **Feedback and Contributions**
Your feedback and contributions to improve these data extraction scripts are highly encouraged. Please feel free to submit issues, feature requests, or pull requests as needed.

Happy data extraction!
