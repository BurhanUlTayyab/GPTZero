from model import GPT2PPL

def test_inference():
    # initialize the model
    model = GPT2PPL()

    sentence = '''Takes in a sentence split by full stop and print the perplexity of the total sentence
                split the lines based on full stop and find the perplexity of each sentence and print
                average perplexity Burstiness is the max perplexity of each sentence'''

    result, out = model(sentence)

    assert out == "The Text is written by Human."