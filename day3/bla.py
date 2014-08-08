txt = "hola mundo! como estas? Bien. Y tu."
print txt
tmp = txt.replace("?", "?\n")
tmp2 = txt.replace("?", ".")
print tmp
print tmp2
tmp = tmp.replace("!", "!\n")
tmp2 = tmp2.replace("!", ".")
print tmp
print tmp2
tmp = tmp.replace(".", ".\n")
print tmp
print tmp2
sentences = tmp.split("\n")
orig_sentences = tmp2.split(".")
print sentences
print orig_sentences

def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
    
  tmp = txt.replace("?", " ?\n")
  tmp = tmp.replace("!", " !\n")
  tmp = tmp.replace(".", " .\n")
  sentences = tmp.split("\n")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  print sentences
  
  for sentence in sentences:
    words = sentence.split()
    print words
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
      print reversed_sentence
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      #new_text += "."
      
  print reversed_sentences
  new_text = new_text.replace("? ", "?")
  new_text = new_text.replace("! ", "!")
  new_text = new_text.replace(". ", ".")
    
  return new_text
  
ex = "HelLo darling! How are you?"
print reversewords(ex)
#print len(sentences)
#sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
#print sentences

#last_sentence = sentences[len(sentences) - 1]
#print last_sentence
#print len(last_sentence)
#if last_sentence[len(last_sentence) - 1] == ".":
	#sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
#print sentences

  #tmp = txt.replace("?", ".")
  #punct = tmp.index(".")
  #tmp = tmp.replace("!", ".")
  #sentences = tmp.split(".")
  #sentences = [s.strip() for s in sentences if len(s.strip()) > 0]