from bnunicodenormalizer import Normalizer
import unicodedata

# Create an instance of the Normalizer class
normalizer = Normalizer()

# Example Bangla text with various Unicode representations
text = '''
This café has a great ambiance.
The façade of the building is impressive.
The role of the reëlected president is crucial.
The résumé needs to be updated.
'''

# Normalize the text using NFC normalization form
normalized_text = unicodedata.normalize('NFC', text)

print("Original Text:", text)
print("Normalized Text:", normalized_text)
