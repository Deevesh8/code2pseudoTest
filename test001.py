unicode_text = "Hello, world! 🌎"

utf8_bytes = codecs.encode(unicode_text, 'utf-8')
print("Encoded UTF-8 bytes:", utf8_bytes)

decoded_text = codecs.decode(utf8_bytes, 'utf-8')
print("Decoded Unicode text:", decoded_text)
