# Cohere API: https://docs.cohere.com/reference/classify

from data import obtain_data
from secret import API_KEY

import cohere
from cohere.responses.classify import Example

# Create a Cohere client using the API key
co = cohere.Client(API_KEY)

# List out the classifications we want
CLASSIFICATIONS = [
    "positive review",
    "neutral review",
    "negative review"
]

# Generate a list of examples for each classification. Each classification must
# have at least 2 examples.
examples=[
    Example("The order came 5 days early", CLASSIFICATIONS[0]),
    Example("The item exceeded my expectations", CLASSIFICATIONS[0]),
    Example("I ordered more for my friends", CLASSIFICATIONS[0]),
    Example("I would buy this again", CLASSIFICATIONS[0]),
    Example("I would recommend this to others", CLASSIFICATIONS[0]),
    Example("This product is awesome", CLASSIFICATIONS[0]),
    Example("The package was damaged", CLASSIFICATIONS[2]),
    Example("The order is 5 days late", CLASSIFICATIONS[2]),
    Example("The order was incorrect", CLASSIFICATIONS[2]),
    Example("I want to return my item", CLASSIFICATIONS[2]),
    Example("The item's material feels low quality", CLASSIFICATIONS[2]),
    Example("The product was okay", CLASSIFICATIONS[1]),
    Example("I received five items in total", CLASSIFICATIONS[1]),
    Example("I bought it from the website", CLASSIFICATIONS[1]),
    Example("I used the product this morning", CLASSIFICATIONS[1]),
    Example("The product arrived yesterday", CLASSIFICATIONS[1])
]

# Obtain our inputs from Google Sheets
inputs1 = obtain_data()

# OR manually list out our inputs
inputs2=[
    "This item was broken when it arrived",
    "The product is very great",
    "The product was not too bad"
]

def print_classifications(input):
    # Note: return type of co.classify() is a Classifications object
    # src: https://github.com/cohere-ai/cohere-python/blob/main/cohere/client.py
    # Classifications reference: https://github.com/cohere-ai/cohere-python/blob/main/cohere/responses/classify.py
    response = co.classify(
        inputs=input,
        examples=examples,
    )

    # Get the counts for each classification
    counts = [0] * len(CLASSIFICATIONS)
    for classification in response:
        for i in range(len(CLASSIFICATIONS)):
            label = CLASSIFICATIONS[i]
            if classification.predictions[0] == label:
                counts[i] += 1

    # For each classifcation, print the percentage
    for i in range(len(CLASSIFICATIONS)):
        print("%s: %f" % (CLASSIFICATIONS[i], counts[i]/len(counts)))

if __name__ == "__main__":
    print_classifications(inputs2)