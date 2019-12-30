from time import sleep
print"noise _list"
noise_list=["is","a","this","..."]
print noise_list
sleep(2)
def _remove_noise(input_text):
    print "original text : ",input_text
    sleep(3)
    print"Tokenization "
    words=input_text.split()
    print words
    noise_free_words=[word for word in words if word not in noise_list]
    sleep(3)
    print "noise_free_words",noise_free_words
    noise_free_text=" ".join(noise_free_words)
    return noise_free_text
print"I am _remove_noise method for tes processing"
sleep(2)
print _remove_noise("this is a sample text")




