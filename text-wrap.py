import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    string_wrapper = wrapper.wrap(text=string)

    text = [ ]
    for i in string_wrapper :
        text.append(i)
    
    
    text1 = [text1 for text1 in text]
    text2 = "\n".join(text1)
    return text2 


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)