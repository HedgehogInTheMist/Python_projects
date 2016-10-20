# Challenge #1 from www.pythonchallenge.com
# http://www.pythonchallenge.com/pc/def/274877906944.html or http://www.pythonchallenge.com/pc/def/map.html


strs = 'abcdefghijklmnopqrstuvwxyz'  # use a string like this, instead of ord()


def shifttext(shift):
    inp = raw_input('Input text here: ')
    data = []
    for i in inp:  # iterate over the text not some list
        if i.strip() and i in strs:  # if the char is not a space ""
            data.append(strs[(strs.index(i) + shift) % 26])
        else:
            data.append(i)  # if space the simply append it to data
    output = ''.join(data)
    return output

print(shifttext(2))

# as a rezult applying 'ocr' to the url
